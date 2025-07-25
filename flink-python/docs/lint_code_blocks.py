#!/usr/bin/env python3
"""
Script to lint Python code blocks in RST files using Ruff.

This script:
1. Extracts Python code blocks from RST files
2. Lints them using Ruff
3. Reports issues found
4. Optionally fixes issues that can be auto-fixed and writes back to files
"""

import re
import subprocess
import tempfile
import os
import sys
from pathlib import Path
from typing import List, Tuple, Dict


def extract_python_blocks(rst_file: Path) -> List[Tuple[int, int, str, str, str]]:
    """
    Extract Python code blocks from an RST file.
    
    Returns:
        List of tuples: (start_line, end_line, block_content, block_type, file_path)
    """
    blocks = []
    content = rst_file.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    in_code_block = False
    block_start = 0
    block_content = []
    block_type = None
    
    for i, line in enumerate(lines):
        # Check for code block start
        if line.startswith('.. code-block:: python'):
            in_code_block = True
            block_start = i
            block_content = []
            block_type = 'code-block'
            continue
        elif line.startswith('.. testcode::'):
            in_code_block = True
            block_start = i
            block_content = []
            block_type = 'testcode'
            continue
        elif '.. literalinclude::' in line and line.endswith('.py'):
            # Handle literalinclude of Python files
            match = re.search(r'\.\. literalinclude:: (.*\.py)', line)
            if match:
                include_path = match.group(1)
                # Resolve relative to rst file
                full_path = rst_file.parent / include_path
                if full_path.exists():
                    blocks.append((i, i, full_path.read_text(encoding='utf-8'), 'literalinclude', str(full_path)))
            continue
        
        # Check for code block end
        if in_code_block:
            if line.strip() == '' or line.startswith('.. ') or (line.startswith('   ') and not line.strip()):
                # End of code block
                if block_content:
                    block_end = i - 1
                    blocks.append((block_start, block_end, '\n'.join(block_content), block_type, None))
                in_code_block = False
                block_content = []
                block_type = None
            elif line.startswith('   '):
                # Code line
                block_content.append(line[3:])  # Remove 3-space indentation
            elif line.strip() and in_code_block:
                # Code line without proper indentation (common in docs)
                block_content.append(line.strip())
    
    # Handle code block that ends at end of file
    if in_code_block and block_content:
        block_end = len(lines)
        blocks.append((block_start, block_end, '\n'.join(block_content), block_type, None))
    
    return blocks


def lint_python_code(code: str, fix: bool = False) -> Tuple[bool, str, str]:
    """
    Lint Python code using Ruff.
    
    Args:
        code: Python code to lint
        fix: Whether to auto-fix issues
    
    Returns:
        Tuple of (success, output, fixed_code)
    """
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        temp_file = f.name
    
    try:
        cmd = ['ruff', 'check']
        if fix:
            cmd.append('--fix')
        cmd.append(temp_file)
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return True, "No issues found", code
        
        # Read the fixed code if --fix was used
        fixed_code = code
        if fix:
            try:
                with open(temp_file, 'r') as f:
                    fixed_code = f.read()
            except:
                pass
        
        return False, result.stdout + result.stderr, fixed_code
    finally:
        os.unlink(temp_file)


def apply_fixes_to_rst_file(rst_file: Path, blocks: List[Tuple[int, int, str, str, str]], fixed_blocks: List[str]) -> bool:
    """
    Apply fixes back to the RST file by replacing code blocks with fixed versions.
    
    Args:
        rst_file: Path to RST file
        blocks: Original blocks with line numbers
        fixed_blocks: List of fixed code content
    
    Returns:
        True if file was modified
    """
    content = rst_file.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    # Sort blocks by start line in reverse order to avoid line number shifts
    sorted_blocks = sorted(zip(blocks, fixed_blocks), key=lambda x: x[0][0], reverse=True)
    
    modified = False
    for (start_line, end_line, original_code, block_type, file_path), fixed_code in sorted_blocks:
        if original_code != fixed_code:
            if block_type == 'literalinclude' and file_path:
                # Fix the external Python file
                try:
                    python_file = Path(file_path)
                    python_file.write_text(fixed_code, encoding='utf-8')
                    print(f"    Fixed external file: {file_path}")
                    modified = True
                except Exception as e:
                    print(f"    Error fixing {file_path}: {e}")
            elif block_type in ['code-block', 'testcode']:
                # Convert fixed code back to RST format with proper indentation
                fixed_lines = fixed_code.split('\n')
                indented_lines = ['   ' + line for line in fixed_lines]
                replacement = '\n'.join(indented_lines)
                
                # Replace the lines in the file
                lines[start_line:end_line] = [replacement]
                modified = True
    
    if modified:
        rst_file.write_text('\n'.join(lines), encoding='utf-8')
    
    return modified


def lint_rst_file(rst_file: Path, fix: bool = False) -> Dict[str, List[str]]:
    """
    Lint all Python code blocks in an RST file.
    
    Args:
        rst_file: Path to RST file
        fix: Whether to auto-fix issues
    
    Returns:
        Dictionary of issues by block type
    """
    issues = {
        'code-block': [],
        'testcode': [],
        'literalinclude': []
    }
    
    blocks = extract_python_blocks(rst_file)
    fixed_blocks = []
    
    for start_line, end_line, code, block_type, file_path in blocks:
        if not code.strip():
            fixed_blocks.append(code)
            continue
            
        success, output, fixed_code = lint_python_code(code, fix)
        fixed_blocks.append(fixed_code)
        
        if not success:
            if file_path:
                issues[block_type].append(f"Line {start_line} ({file_path}): {output}")
            else:
                issues[block_type].append(f"Line {start_line}: {output}")
    
    # Apply fixes back to the file if requested
    if fix:
        apply_fixes_to_rst_file(rst_file, blocks, fixed_blocks)
    
    return issues


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Lint Python code blocks in RST files')
    parser.add_argument('--fix', action='store_true', help='Auto-fix issues where possible')
    parser.add_argument('--files', nargs='*', help='Specific RST files to check')
    args = parser.parse_args()
    
    # Find RST files to check
    if args.files:
        rst_files = [Path(f) for f in args.files if Path(f).exists()]
    else:
        rst_files = list(Path('.').rglob('*.rst'))
        # Exclude auto-generated files
        rst_files = [f for f in rst_files if 'reference/api' not in str(f)]
    
    total_issues = 0
    all_issues = []
    
    for rst_file in rst_files:
        print(f"\nChecking {rst_file}...")
        
        issues = lint_rst_file(rst_file, args.fix)
        
        file_has_issues = False
        for block_type, block_issues in issues.items():
            if block_issues:
                file_has_issues = True
                print(f"  {block_type} blocks:")
                for issue in block_issues:
                    print(f"    {issue}")
                    total_issues += 1
                    all_issues.append((str(rst_file), block_type, issue))
        
        if not file_has_issues:
            print("  ✓ No issues found")
    
    print(f"\nTotal issues found: {total_issues}")
    
    if total_issues > 0:
        print("\nSummary of all issues:")
        for file, block_type, issue in all_issues:
            print(f"{file} [{block_type}]: {issue}")
        sys.exit(1)


if __name__ == '__main__':
    main() 
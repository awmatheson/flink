..  Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

..    http://www.apache.org/licenses/LICENSE-2.0

..  Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

============
Preparation
============

This page shows you how to install PyFlink using pip, conda, uv, installing from the source, etc.

.. note::
   This guide focuses on PyFlink-specific installation and environment setup. For comprehensive Flink
       installation instructions,
   including system requirements, configuration, and troubleshooting, please refer to the
   `Flink Installation Guide <https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/overview/>`_.

Python Version Supported
------------------------

.. list-table::
   :widths: 25 50
   :header-rows: 1

   * - PyFlink Version
     - Python Version Supported
   * - PyFlink 2.0
     - Python 3.8 to 3.11
   * - PyFlink 1.20
     - Python 3.8 to 3.11
   * - PyFlink 1.19
     - Python 3.8 to 3.11
   * - PyFlink 1.18
     - Python 3.7 to 3.10
   * - PyFlink 1.17
     - Python 3.6 to 3.10
   * - PyFlink 1.16
     - Python 3.6 to 3.9
   * - PyFlink 1.15
     - Python 3.6 to 3.8
   * - PyFlink 1.14
     - Python 3.6 to 3.8

You could check your Python version as following:

.. code-block:: bash

    python3 --version


Create a Python virtual environment
-----------------------------------

A virtual environment gives you the ability to isolate the Python dependencies of different projects by creating a
separate environment for each project. It is a directory tree which contains its own Python executable files and the
installed Python packages.

It is useful for local development to create a standalone Python environment and also useful when deploying a PyFlink
job to production when there are Python dependencies. Python virtual environments are supported in PyFlink jobs,
see :ref:`archives <user_guide/dependency_management:archives>` for more details.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a virtual environment using uv, run:

.. code-block:: bash

    # Install uv (if not already installed)
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Create a new virtual environment
    uv venv

    # Activate the virtual environment
    source .venv/bin/activate

Alternatively, you can create a virtual environment with a specific Python version:

.. code-block:: bash

    # Create a virtual environment with Python 3.11
    uv venv --python 3.11

    # Activate the virtual environment
    source .venv/bin/activate

Create a virtual environment using virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a virtual environment using virtualenv, run:

.. code-block:: bash

    python3 -m pip install virtualenv

    # Create Python virtual environment under a directory, e.g. venv
    virtualenv venv

    # You can also create Python virtual environment with a specific Python version
    virtualenv --python /path/to/python/executable venv

The virtual environment needs to be activated before to use it. To activate the virtual environment, run:

.. code-block:: bash

    source venv/bin/activate

That is, execute the activate script under the bin directory of your virtual environment.


Create a virtual environment using conda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a virtual environment using conda (suppose miniconda), run:

.. code-block:: bash

    # Download and install miniconda, the latest miniconda installers are available in https://repo.anaconda.com/minicon
        da/

    # Suppose the name of the downloaded miniconda installer is miniconda.sh
    chmod +x miniconda.sh
    # install miniconda
    ./miniconda.sh -b -p miniconda

    # Activate the miniconda environment
    source miniconda/bin/activate

    # Create conda virtual environment under a directory, e.g. venv
    conda create --name venv python=3.8 -y


The conda virtual environment needs to be activated before to use it. To activate the conda virtual environment, run:

.. code-block:: bash

    conda activate venv


Install PyFlink
---------------

You could then install the latest PyFlink package into your virtual environment. Note that the Flink version and PyFlink
version need to be consistent. For example, if you are using Flink 2.1, then you should use PyFlink 2.1

Installing using PyPI
~~~~~~~~~~~~~~~~~~~~~

PyFlink could be installed using `PyPI <https://pypi.org/project/apache-flink/>`_ as following:

.. code-block:: bash

    python3 -m pip install apache-flink


~~~~~~~~~~~~~~~~~~~

PyFlink could be installed using `uv <https://docs.astral.sh/uv/>`_ as following:

.. code-block:: bash

    # Install PyFlink using uv
    uv add apache-flink

    # Or install a specific version
    uv add apache-flink==2.0


Installing from Source
~~~~~~~~~~~~~~~~~~~~~~

To install PyFlink from source, you could refer to `Build PyFlink <https://nightlies.apache.org/flink/flink-docs-stable/docs/flinkdev/building/#build-pyflink>`_.


Check the installed package
---------------------------

You could then perform the following checks to make sure that the installed PyFlink package is ready for use:

.. code-block:: bash

    curl -L https://raw.githubusercontent.com/apache/flink/master/flink-python/pyflink/examples/table/word_count.py
        -o word_count.py
    python3 word_count.py
    # You will see outputs as following:
    # Use --input to specify file input.
    # Printing result to stdout. Use --output to specify output path.
    # +I[To, 1]
    # +I[be,, 1]
    # +I[or, 1]
    # +I[not, 1]
    # +I[to, 1]
    # +I[be,--that, 1]
    # ...

If there are any problems, you could perform the following checks.

Check the logging messages in the log file to see if there are any problems:

.. code-block:: bash

    # Get the installation directory of PyFlink
    python3 -c "import pyflink;import os;print(os.path.dirname(os.path.abspath(pyflink.__file__)))"
    # It will output a path like the following:
    # /path/to/python/site-packages/pyflink

    # Check the logging under the log directory
    ls -lh /path/to/python/site-packages/pyflink/log
    # You will see the log file as following:
    #  -rw-r--r--  1 dianfu  staff    45K 10 18 20:54 flink-dianfu-python-B-7174MD6R-1908.local.log

Besides, you could also check if the files of the PyFlink package are consistent.
It may happen that you have installed an old version of PyFlink before and multiple PyFlink versions exist at the
same time for some reason.

.. code-block:: bash

    # List the jar packages under the lib directory
    ls -lh /path/to/python/site-packages/pyflink/lib


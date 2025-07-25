.. ################################################################################
     Licensed to the Apache Software Foundation (ASF) under one
     or more contributor license agreements.  See the NOTICE file
     distributed with this work for additional information
     regarding copyright ownership.  The ASF licenses this file
     to you under the Apache License, Version 2.0 (the
     "License"); you may not use this file except in compliance
     with the License.  You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
    limitations under the License.
   ################################################################################

Table Operations
================

Table operations provide the core functionality for transforming and processing data in the Table API.

.. toctree::
   :maxdepth: 2
   :caption: Table Operations

   operations
   row_based_operations

Overview
--------

Table operations enable you to transform and process data in a declarative way:

* **General Operations**: Standard table operations like select, filter, join, etc.
* **Row-based Operations**: Operations that work on individual rows
* **Aggregation Operations**: Group-by, window aggregations, and other aggregations
* **Set Operations**: Union, intersection, and other set-based operations

Key Concepts
------------

* **Declarative API**: Write operations using SQL-like syntax
* **Lazy Evaluation**: Operations are optimized and executed when needed
* **Type Safety**: Strong typing with Python type hints
* **Optimization**: Automatic query optimization by Flink

Getting Started
--------------

See :doc:`operations` for a comprehensive introduction to table operations.

Advanced Operations
------------------

* **Row-based Processing**: See :doc:`row_based_operations` for row-level transformations
* **User-defined Functions**: Extend operations with custom UDFs
* **Window Operations**: Time-based and count-based windowing 
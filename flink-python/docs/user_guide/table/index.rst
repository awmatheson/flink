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

Table API
=========

The Table API is a unified, relational API for stream and batch processing. It can be embedded in Java and Scala programs, or used in SQL clients.

.. toctree::
   :maxdepth: 2
   :caption: Table API Documentation

   intro_to_table_api
   table_environment
   catalogs
   python_types
   conversion_of_pandas
   conversion_of_data_stream
   connectors
   sql
   built_in_functions
   metrics
   operations/index
   udfs/index

Overview
--------

The Table API provides a unified way to work with both batch and streaming data. It offers:

* **Declarative API**: Write queries using SQL-like syntax
* **Type Safety**: Strong typing with Python type hints
* **Optimization**: Automatic query optimization
* **Integration**: Seamless integration with DataStream API
* **UDFs**: Support for Python user-defined functions

Key Concepts
------------

* **Table**: A structured dataset with a schema
* **TableEnvironment**: Entry point for Table API operations
* **Catalog**: Metadata management for tables and functions
* **UDF**: User-defined functions for custom transformations

Getting Started
--------------

See :doc:`intro_to_table_api` for a quick introduction to the Table API.

For detailed tutorials, see :doc:`table_api_tutorial`.

Operations
----------

The Table API provides various operations for data transformation:

* **Row-based Operations**: See :doc:`operations/row_based_operations`
* **General Operations**: See :doc:`operations/operations`

User-Defined Functions
---------------------

Extend the Table API with custom functions:

* **Overview**: See :doc:`udfs/overview`
* **Python UDFs**: See :doc:`udfs/python_udfs`
* **Vectorized UDFs**: See :doc:`udfs/vectorized_python_udfs`

Configuration
-------------

* **Table Environment**: See :doc:`table_environment`
* **Catalogs**: See :doc:`catalogs`
* **Connectors**: See :doc:`python_table_api_connectors`

Data Types and Conversions
-------------------------

* **Python Types**: See :doc:`python_types`
* **Pandas Integration**: See :doc:`conversion_of_pandas`
* **DataStream Conversion**: See :doc:`conversion_of_data_stream` 
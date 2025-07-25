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

User-Defined Functions (UDFs)
=============================

User-defined functions allow you to extend the Table API with custom logic and transformations.

.. toctree::
   :maxdepth: 2
   :caption: User-Defined Functions

   overview
   general_udfs
   vectorized_udfs

Overview
--------

UDFs enable you to implement custom business logic in Python:

* **Scalar Functions**: Functions that operate on individual values
* **Table Functions**: Functions that return multiple rows
* **Aggregate Functions**: Functions that aggregate multiple values
* **Vectorized Functions**: High-performance functions for batch processing

Key Concepts
------------

* **Type Safety**: UDFs support Python type hints for better performance
* **Serialization**: UDFs are serialized and distributed across the cluster
* **Performance**: Vectorized UDFs provide optimized batch processing
* **Integration**: Seamless integration with Table API operations

Getting Started
--------------

See :doc:`overview` for an introduction to UDFs and their types.

Function Types
--------------

* **General UDFs**: See :doc:`general_udfs` for scalar and table functions
* **Vectorized UDFs**: See :doc:`vectorized_udfs` for high-performance batch processing

Best Practices
--------------

* Use type hints for better performance
* Consider vectorized UDFs for batch operations
* Handle null values appropriately
* Test UDFs thoroughly before deployment 
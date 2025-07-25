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

DataStream Operators
====================

Operators are the building blocks of DataStream transformations. They allow you to process and transform data streams in various ways.

.. toctree::
   :maxdepth: 2
   :caption: DataStream Operators

   overview
   process_function
   windows

Overview
--------

DataStream operators provide the core functionality for stream processing:

* **Transformation Operators**: Map, filter, flatMap, and other data transformations
* **Aggregation Operators**: Reduce, fold, and other aggregation operations  
* **Window Operators**: Time and count-based windowing operations
* **Process Functions**: Low-level stream processing with fine-grained control

Key Concepts
------------

* **Operator Chaining**: Multiple operators can be chained together for efficiency
* **Parallelism**: Operators can be executed in parallel across multiple tasks
* **State Management**: Operators can maintain state for processing
* **Time Handling**: Support for event time and processing time semantics

Getting Started
--------------

See :doc:`overview` for a comprehensive introduction to DataStream operators.

Advanced Features
----------------

* **Process Functions**: See :doc:`process_function` for low-level stream processing
* **Windows**: See :doc:`windows` for time-based and count-based windowing 
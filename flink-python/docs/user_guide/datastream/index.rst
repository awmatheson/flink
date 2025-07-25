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

DataStream API
=============

The DataStream API is the core API for stream processing in PyFlink. It provides low-level control over stream processing operations and is ideal for complex streaming applications.

.. toctree::
   :maxdepth: 2
   :caption: DataStream API Documentation

   intro_to_datastream_api
   data_types
   state
   operators/index

Overview
--------

The DataStream API provides:

* **Stream Processing**: Real-time processing of data streams
* **Event Time**: Support for event time semantics and watermarks
* **State Management**: Rich state management for complex applications
* **Operators**: Comprehensive set of transformation and aggregation operators
* **Parallelism**: Fine-grained control over parallelism and partitioning

Key Concepts
------------

* **DataStream**: A stream of data elements with a schema
* **Operators**: Transformations applied to data streams
* **State**: Persistent state for maintaining information across events
* **Time**: Event time, processing time, and ingestion time semantics
* **Watermarks**: Progress indicators for event time processing

Getting Started
--------------

See :doc:`intro_to_datastream_api` for a comprehensive introduction to the DataStream API.

Core Components
---------------

* **Data Types**: See :doc:`data_types` for supported data types and serialization
* **State Management**: See :doc:`state` for stateful stream processing
* **Operators**: See :doc:`operators/index` for available transformation operators

Use Cases
---------

* **Real-time Analytics**: Process streaming data for real-time insights
* **Event Processing**: Complex event processing and pattern matching
* **Data Pipelines**: Build robust data processing pipelines
* **Machine Learning**: Stream processing for ML model serving

For tutorials and examples, see :doc:`../datastream_tutorial`.

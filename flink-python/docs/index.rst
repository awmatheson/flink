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

PyFlink
=================================

PyFlink is a Python API for Apache Flink that allows you to build scalable batch and streaming
workloads, such as real-time data processing pipelines, large-scale exploratory data analysis,
Machine Learning (ML) pipelines and ETL processes.

If you're already familiar with Python and libraries such as Pandas, then PyFlink makes it simpler
to leverage the full capabilities of the Flink ecosystem. Depending on the level of abstraction you
need, there are two different APIs that can be used in PyFlink:

* The **PyFlink Table API** allows you to write powerful relational queries in a way that is similar
    to using SQL or working with tabular data in Python.
* At the same time, the **PyFlink DataStream API** gives you lower-level control over the core building
    blocks of Flink, state and time, to build more complex stream processing use cases.

.. toctree::
    :maxdepth: 1
    :caption: Getting Started

    getting_started/installation
    getting_started/quickstart

.. toctree::
    :maxdepth: 1
    :caption: Deployment

    deployment/index

.. toctree::
    :maxdepth: 2
    :caption: User Guide

    user_guide/index

.. toctree::
    :maxdepth: 2
    :caption: API Reference

    reference/index

.. toctree::
    :maxdepth: 1
    :caption: Cookbook

    cookbook/index

.. toctree::
    :maxdepth: 1
    :caption: Examples

    examples/index

.. toctree::
    :maxdepth: 1
    :caption: Developer Guide

    developer_guide/index

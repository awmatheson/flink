.. raw:: html

   <!--
   Licensed to the Apache Software Foundation (ASF) under one
   or more contributor license agreements.  See the NOTICE file
   distributed with this work for additional information
   regarding copyright ownership.  The ASF licenses this file
   to you under the Apache License, Version 2.0 (the
   "License"); you may not use this file except in compliance
   with the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.
   -->

Python Execution Mode
=====================

PyFlink supports two execution modes for Python user-defined functions:
``PROCESS`` execution mode and ``THREAD`` execution mode.

- **PROCESS execution mode**: Python user-defined functions are executed
  in separate Python worker processes. This is the default execution
  mode.
- **THREAD execution mode**: Python user-defined functions are executed
  in the same process as Java operators. This mode is more efficient
  but has some limitations.

Configuration
-------------

You can configure the execution mode using the following configuration
options:

Python Table API
~~~~~~~~~~~~~~~~

.. code-block:: python

   from pyflink.table import EnvironmentSettings, TableEnvironment

   # Specify `PROCESS` mode
   env_settings = EnvironmentSettings.in_streaming_mode()
   env_settings = env_settings.with_configuration(
       {"python.execution-mode": "process"}
   )
   table_env = TableEnvironment.create(env_settings)

   # Specify `THREAD` mode
   env_settings = EnvironmentSettings.in_streaming_mode()
   env_settings = env_settings.with_configuration(
       {"python.execution-mode": "thread"}
   )
   table_env = TableEnvironment.create(env_settings)

Python DataStream API
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pyflink.datastream import StreamExecutionEnvironment
   from pyflink.common.configuration import Configuration

   config = Configuration()

   # Specify `PROCESS` mode
   config.set_string("python.execution-mode", "process")

   # Specify `THREAD` mode
   config.set_string("python.execution-mode", "thread")

   # Create the corresponding StreamExecutionEnvironment
   env = StreamExecutionEnvironment.get_execution_environment(config)

Supported Cases
---------------

Python Table API
~~~~~~~~~~~~~~~~

The following table shows where the ``THREAD`` execution mode is
supported in Python Table API.

======================== =========== ==========
UDFs                     ``PROCESS`` ``THREAD``
======================== =========== ==========
Python UDF               Yes         Yes
Python UDTF              Yes         Yes
Python UDAF              Yes         No
Pandas UDF & Pandas UDAF Yes         No
======================== =========== ==========

Python DataStream API
~~~~~~~~~~~~~~~~~~~~~

The following table shows where the ``PROCESS`` execution mode and the
``THREAD`` execution mode are supported in Python DataStream API.

================ =========== ==========
Operators        ``PROCESS`` ``THREAD``
================ =========== ==========
Map              Yes         Yes
FlatMap          Yes         Yes
Filter           Yes         Yes
Reduce           Yes         Yes
Union            Yes         Yes
Connect          Yes         Yes
CoMap            Yes         Yes
CoFlatMap        Yes         Yes
Process Function Yes         Yes
Window Apply     Yes         Yes
Window Aggregate Yes         Yes
Window Reduce    Yes         Yes
Window Process   Yes         Yes
Side Output      Yes         Yes
State            Yes         Yes
Iterate          No          No
Window CoGroup   No          No
Window Join      No          No
Interval Join    No          No
Async I/O        No          No
================ =========== ==========

.. note::
   Currently, it still doesn't support to execute Python
   UDFs in ``THREAD`` execution mode in all places. It will fall back to
   ``PROCESS`` execution mode in these cases. So it may happen that you
   configure a job to execute in ``THREAD`` execution mode, however, it's
   actually executed in ``PROCESS`` execution mode.

.. note::
   ``THREAD`` execution mode is only supported in Python 3.8+.

Execution Behavior
------------------

This section provides an overview of the execution behavior of
``THREAD`` execution mode and contrasts they with ``PROCESS`` execution
mode. For more details, please refer to the FLIP that introduced this
feature:
`FLIP-206 <https://cwiki.apache.org/confluence/display/FLINK/FLIP-206%3A+Support+PyFlink+Runtime+Execution+in+Thread+Mode>`__.

PROCESS Execution Mode
^^^^^^^^^^^^^^^^^^^^^^

In ``PROCESS`` execution mode, the Python user-defined functions will be
executed in separate Python Worker process. The Java operator process
communicates with the Python worker process using various Grpc services.

.. image:: /assets/fig/pyflink_process_execution_mode.png
   :alt: Process Execution Mode

THREAD Execution Mode
^^^^^^^^^^^^^^^^^^^^^

In ``THREAD`` execution mode, the Python user-defined functions will be
executed in the same process as Java operators. PyFlink takes use of
third part library `PEMJA <https://github.com/alibaba/pemja>`__ to embed
Python in Java Application.

.. image:: /assets/fig/pyflink_embedded_execution_mode.png
   :alt: Embedded Execution Mode

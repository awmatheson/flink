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

Deployment
==========

This section covers how to deploy PyFlink applications to various environments.

------------------

PyFlink applications can be deployed in several ways:

* **Local Mode**: For development and testing
* **Standalone Cluster**: For production deployments
* **YARN**: For Hadoop environments
* **Kubernetes**: For containerized deployments
* **Docker**: For containerized deployments

---------------------

For local development and testing:

.. code-block:: python

   from pyflink.datastream import StreamExecutionEnvironment
   from pyflink.table import StreamTableEnvironment, EnvironmentSettings

   # Create execution environment
   env = StreamExecutionEnvironment.get_execution_environment()

   # Set parallelism for local execution
   env.set_parallelism(1)

   # Create table environment
   settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
   table_env = StreamTableEnvironment.create(env, settings)

   # Your PyFlink application code here

   # Execute
   env.execute("local-job")

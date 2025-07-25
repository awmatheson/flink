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

Environment Variables
=====================

These environment variables will affect the behavior of PyFlink:

.. raw:: html

   <table class="table table-bordered">

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th class="text-left" style="width: 30%">

Environment Variable

.. raw:: html

   </th>

.. raw:: html

   <th class="text-center">

Description

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   </thead>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td>

FLINK_HOME

.. raw:: html

   </td>

.. raw:: html

   <td>

PyFlink job will be compiled before submitting and it requires Flink’s
distribution to compile the job. PyFlink’s installation package already
contains Flink’s distribution and it’s used by default. This environment
allows you to specify a custom Flink’s distribution.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

PYFLINK_CLIENT_EXECUTABLE

.. raw:: html

   </td>

.. raw:: html

   <td>

The path of the Python interpreter used to launch the Python process
when submitting the Python jobs via “flink run” or compiling the
Java/Scala jobs containing Python UDFs. Equivalent to the configuration
option ‘python.client.executable’. The priority is as following:

.. raw:: html

   <ol>

.. raw:: html

   <li>

The configuration ‘python.client.executable’ defined in the source code;

.. raw:: html

   </li>

.. raw:: html

   <li>

The environment variable PYFLINK_CLIENT_EXECUTABLE;

.. raw:: html

   </li>

.. raw:: html

   <li>

The configuration 'python.client.executable' defined in :doc:`Flink configuration file <../deployment/config#flink-configuration-file>`

.. raw:: html

   </li>

.. raw:: html

   </ol>

If none of above is set, the default Python interpreter ‘python’ will be
used.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

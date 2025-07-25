.. Licensed to the Apache Software Foundation (ASF) under one
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

TableEnvironment
================

This document is an introduction of PyFlink ``TableEnvironment``. It includes detailed descriptions of every public interface of the ``TableEnvironment`` class.

Create a TableEnvironment
-------------------------

The recommended way to create a ``TableEnvironment`` is to create from an ``EnvironmentSettings`` object:

.. code:: python

   from pyflink.common import Configuration
   from pyflink.table import EnvironmentSettings, TableEnvironment

   # create a streaming TableEnvironment
   config = Configuration()
   config.set_string('execution.buffer-timeout', '1 min')
   env_settings = EnvironmentSettings \
       .new_instance() \
       .in_streaming_mode() \
       .with_configuration(config) \
       .build()

   table_env = TableEnvironment.create(env_settings)

Alternatively, users can create a ``StreamTableEnvironment`` from an existing ``StreamExecutionEnvironment`` to interoperate with the DataStream API.

.. code:: python

   from pyflink.datastream import StreamExecutionEnvironment
   from pyflink.table import StreamTableEnvironment

   # create a streaming TableEnvironment from a StreamExecutionEnvironment
   env = StreamExecutionEnvironment.get_execution_environment()
   table_env = StreamTableEnvironment.create(env)

TableEnvironment API
--------------------

Table/SQL Operations
~~~~~~~~~~~~~~~~~~~~

These APIs are used to create/remove Table API/SQL Tables and write queries:

.. list-table:: Table/SQL Operations
   :widths: 25 50 25
   :header-rows: 1

   * - APIs
     - Description
     - Reference
   * - ``from_elements(elements, schema=None, verify_schema=True)``
     - Creates a table from a collection of elements.
     - :func:`~pyflink.table.TableEnvironment.from_elements`
   * - ``from_pandas(pdf, schema=None, split_num=1)``
     - Creates a table from a pandas DataFrame.
     - :func:`~pyflink.table.TableEnvironment.from_pandas`
   * - ``from_path(path)``
     - Creates a table from a registered table under the specified path, e.g. tables registered via create_temporary_view.
     - :func:`~pyflink.table.TableEnvironment.from_path`
   * - ``create_temporary_view(view_path, table)``
     - Registers a ``Table`` object as a temporary view similar to SQL temporary views.
     - :func:`~pyflink.table.TableEnvironment.create_temporary_view`
   * - ``create_view(view_path, table, ignore_if_exists=False)``
     - Registers a ``Table`` object as a view similar to SQL views.
     - :func:`~pyflink.table.TableEnvironment.create_view`
   * - ``drop_temporary_view(view_path)``
     - Drops a temporary view registered under the given path.
     - :func:`~pyflink.table.TableEnvironment.drop_temporary_view`
   * - ``drop_view(view_path, ignore_if_not_exists=True)``
     - Drops a view registered in the given path.
     - :func:`~pyflink.table.TableEnvironment.drop_view`
   * - ``create_temporary_table(path, table_descriptor, ignore_if_exists=False)``
     - Registers a ``Table`` object as a temporary catalog table similar to SQL temporary tables.
     - :func:`~pyflink.table.TableEnvironment.create_temporary_table`
   * - ``create_table(path, table_descriptor, ignore_if_exists=False)``
     - Registers a ``Table`` object as a catalog table similar to SQL tables.
     - :func:`~pyflink.table.TableEnvironment.create_table`
   * - ``drop_temporary_table(table_path)``
     - Drops a temporary table registered under the given path. You can use this interface to drop the temporary source table and temporary sink table.
     - :func:`~pyflink.table.TableEnvironment.drop_temporary_table`
   * - ``drop_table(table_path, ignore_if_not_exists=True)``
     - Drops a table registered under the given path.
     - :func:`~pyflink.table.TableEnvironment.drop_table`
   * - ``execute_sql(stmt)``
     - Executes the given single statement and returns the execution result. The statement can be DDL/DML/DQL/SHOW/DESCRIBE/EXPLAIN/USE. Note that for "INSERT INTO" statement this is an asynchronous operation, which is usually expected when submitting a job to a remote cluster. However, when executing a job in a mini cluster or IDE, you need to wait until the job execution finished. Please refer to the `SQL documentation <https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/sql/>`__ for more details about SQL statements.
     - :func:`~pyflink.table.TableEnvironment.execute_sql`
   * - ``sql_query(query)``
     - Evaluates a SQL query and retrieves the result as a ``Table`` object.
     - :func:`~pyflink.table.TableEnvironment.sql_query`

Deprecated APIs

.. list-table:: Deprecated APIs
   :widths: 25 50 25
   :header-rows: 1

   * - APIs
     - Description
     - Reference
   * - ``scan(*table_path)``
     - Scans a registered table from catalog and returns the resulting Table. It can be replaced by from_path.
     - :func:`~pyflink.table.TableEnvironment.scan`
   * - ``register_table(name, table)``
     - Registers a Table object under a unique name in the TableEnvironment’s catalog. Registered tables can be referenced in SQL queries. It can be replaced by create_temporary_view.
     - :func:`~pyflink.table.TableEnvironment.register_table`
   * - ``insert_into(target_path, table)``
     - Instructs to write the content of a Table object into a sink table. Note that this interface would not trigger the execution of jobs. You need to call the “execute” method to execute your job.
     - :func:`~pyflink.table.TableEnvironment.insert_into`
   * - ``sql_update(stmt)``
     - Evaluates a SQL statement such as INSERT, UPDATE or DELETE or a DDL statement. It can be replaced by execute_sql.
     - :func:`~pyflink.table.TableEnvironment.sql_update`

Execute/Explain Jobs
~~~~~~~~~~~~~~~~~~~~

These APIs are used to explain/execute jobs. Note that the API execute_sql can also be used to execute jobs.

.. list-table:: Execute/Explain Jobs
   :widths: 25 50 25
   :header-rows: 1
   
   * - APIs
     - Description
     - Reference
   * - ``explain_sql(stmt, *extra_details)``
     - Returns the AST and the execution plan of the specified statement.
     - :func:`~pyflink.table.TableEnvironment.explain_sql`
   * - ``create_statement_set()``
     - Creates a StatementSet instance which accepts DML statements or Tables. It can be used to execute a multi-sink job.
     - :func:`~pyflink.table.TableEnvironment.create_statement_set`

Deprecated APIs

.. list-table:: Deprecated APIs
   :widths: 25 50 25
   :header-rows: 1
   
   * - APIs
     - Description
     - Reference
   * - ``explain(table=None, extended=False)``
     - Returns the AST of the specified Table API and SQL queries and the execution plan to compute the result of the given Table object or multi-sinks plan. If you use the insert_into or sql_update method to emit data to multiple sinks, you can use this method to get the plan. It can be replaced by TableEnvironment.explain_sql, Table.explain or StatementSet.explain.
     - :func:`~pyflink.table.TableEnvironment.explain`
   * - ``execute(job_name)``
     - Triggers the program execution. The environment will execute all parts of the program. If you use the insert_into or sql_update method to emit data to sinks, you can use this method to execute your job.
     - :func:`~pyflink.table.TableEnvironment.execute`

Create/Drop User Defined Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These APIs are used to register UDFs or remove the registered UDFs. Note that the API ``execute_sql`` can also be used to register/remove UDFs. For more details about the different kinds of UDFs, please refer to [User Defined Functions]({{< ref “docs/dev/table/functions/overview” >}}).

.. list-table:: Create/Drop User Defined Functions
   :widths: 25 50 25
   :header-rows: 1
   
   * - APIs
     - Description
     - Reference
   * - ``create_temporary_function(path, function)``
     - Registers a Python user defined function class as a temporary catalog function.
     - :func:`~pyflink.table.TableEnvironment.create_temporary_function`
   * - ``create_temporary_system_function(name, function)``
     - Registers a Python user defined function class as a temporary system function. If the name of a temporary system function is the same as a temporary catalog function, the temporary system function takes precedence.
     - :func:`~pyflink.table.TableEnvironment.create_temporary_system_function`
   * - ``create_java_function(path, function_class_name, ignore_if_exists=None)``
     - Registers a Java user defined function class as a catalog function under the given path. If the catalog is persistent, the registered catalog function can be used across multiple Flink sessions and clusters.
     - :func:`~pyflink.table.TableEnvironment.create_java_function`
   * - ``create_java_temporary_function(path, function_class_name)``
     - Registers a Java user defined function class as a temporary catalog function.
     - :func:`~pyflink.table.TableEnvironment.create_java_temporary_function`
   * - ``create_java_temporary_system_function(name, function_class_name)``
     - Registers a Java user defined function class as a temporary system function.
     - :func:`~pyflink.table.TableEnvironment.create_java_temporary_system_function`
   * - ``drop_function(path)``
     - Drops a catalog function registered under the given path.
     - :func:`~pyflink.table.TableEnvironment.drop_function`
   * - ``drop_temporary_function(path)``
     - Drops a temporary system function registered under the given name.
     - :func:`~pyflink.table.TableEnvironment.drop_temporary_function`
   * - ``drop_temporary_system_function(name)``
     - Drops a temporary system function registered under the given name.
     - :func:`~pyflink.table.TableEnvironment.drop_temporary_system_function`

Dependency Management
~~~~~~~~~~~~~~~~~~~~~

These APIs are used to manage the Python dependencies which are required by the Python UDFs. Please refer to the `Dependency Management `__ documentation for more details.

.. list-table:: Dependency Management
   :widths: 25 50 25
   :header-rows: 1

   * - APIs
     - Description
     - Reference
   * - ``add_python_file(file_path)``
     - Adds a Python dependency which could be Python files, Python packages or local directories. They will be added to the PYTHONPATH of the Python UDF worker.
     - :func:`~pyflink.table.TableEnvironment.add_python_file`
   * - ``set_python_requirements(requirements_file_path, requirements_cache_dir=None)``
     - Specifies a requirements.txt file which defines the third-party dependencies. These dependencies will be installed to a temporary directory and added to the PYTHONPATH of the Python UDF worker.
     - :func:`~pyflink.table.TableEnvironment.set_python_requirements`
   * - ``add_python_archive(archive_path, target_dir=None)``
     - Adds a Python archive file. The file will be extracted to the working directory of Python UDF worker.
     - :func:`~pyflink.table.TableEnvironment.add_python_archive`

Configuration
~~~~~~~~~~~~~

These APIs are used to get the configuration of the TableEnvironment.

.. list-table:: Configuration
   :widths: 25 50 25
   :header-rows: 1

   * - APIs
     - Description
     - Reference
   * - ``get_config()``
     - Returns the table config to define the runtime behavior of the Table API. You can find all the available configuration options in `Configuration <https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/deployment/config/>`__ and `Python Configuration <../python_config.html>`__. The following code is an example showing how to set the configuration options through this API:

       .. code:: python

         # set the parallelism to 8
         table_env.get_config().set("parallelism.default", "8")
         # set the job name
         table_env.get_config().set("pipeline.name", "my_first_job")

     - :func:`~pyflink.table.TableEnvironment.get_config`

Catalog APIs
~~~~~~~~~~~~

These APIs are used to access catalogs and modules. You can find more detailed introduction in `Modules <https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/table/modules/>`__ and `Catalogs <https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/table/catalogs/>`__.

.. list-table:: Catalog APIs
   :widths: 25 50 25
   :header-rows: 1

   * - APIs
     - Description
     - Reference
   * - ``register_catalog(catalog_name, catalog)``
     - Registers a Catalog under a unique name.
     - :func:`~pyflink.table.TableEnvironment.register_catalog`
   * - ``get_catalog(catalog_name)``
     - Gets a registered Catalog by name.
     - :func:`~pyflink.table.TableEnvironment.get_catalog`
   * - ``use_catalog(catalog_name)``
     - Sets the current catalog to the given value. It also sets the default database to the catalog’s default one.
     - :func:`~pyflink.table.TableEnvironment.use_catalog`
   * - ``get_current_catalog()``
     - Gets the current default catalog name of the current session.
     - :func:`~pyflink.table.TableEnvironment.get_current_catalog`
   * - ``get_current_database()``
     - Gets the current default database name of the running session.
     - :func:`~pyflink.table.TableEnvironment.get_current_database`
   * - ``use_database(database_name)``
     - Sets the current default database. It has to exist in the current catalog. That path will be used as the default one when looking for unqualified object names.
     - :func:`~pyflink.table.TableEnvironment.use_database`
   * - ``load_module(module_name, module)``
     - Loads a Module under a unique name. Modules will be kept in the loaded order.
     - :func:`~pyflink.table.TableEnvironment.load_module`
   * - ``unload_module(module_name)``
     - Unloads a Module with given name.
     - :func:`~pyflink.table.TableEnvironment.unload_module`
   * - ``use_modules(*module_names)``
     - Enables and changes the resolution order of loaded modules.
     - :func:`~pyflink.table.TableEnvironment.use_modules`
   * - ``list_catalogs()``
     - Gets the names of all catalogs registered in this environment.
     - :func:`~pyflink.table.TableEnvironment.list_catalogs`
   * - ``list_modules()``
     - Gets the names of all enabled modules registered in this environment.
     - :func:`~pyflink.table.TableEnvironment.list_modules`
   * - ``list_full_modules()``
     - Gets the names of all loaded modules (including disabled modules) registered in this environment.
     - :func:`~pyflink.table.TableEnvironment.list_full_modules`
   * - ``list_databases()``
     - Gets the names of all tables and views in the current database of the current catalog. It returns both temporary and permanent tables and views.
     - :func:`~pyflink.table.TableEnvironment.list_tables`
   * - ``list_views()``
     - Gets the names of all views in the current database of the current catalog. It returns both temporary and permanent views.
     - :func:`~pyflink.table.TableEnvironment.list_views`
   * - ``list_user_defined_functions()``
     - Gets the names of all user defined functions registered in this environment.
     - :func:`~pyflink.table.TableEnvironment.list_user_defined_functions`
   * - ``list_functions()``
     - Gets the names of all functions in this environment.
     - :func:`~pyflink.table.TableEnvironment.list_functions`
   * - ``list_temporary_tables()``
     - Gets the names of all temporary tables and views available in the current namespace (the current database of the current catalog).
     - :func:`~pyflink.table.TableEnvironment.list_temporary_tables`
   * - ``list_temporary_views()``
     - Gets the names of all temporary views available in the current namespace (the current database of the current catalog).
     - :func:`~pyflink.table.TableEnvironment.list_temporary_views`

Statebackend, Checkpoint and Restart Strategy
---------------------------------------------

Before Flink 1.10 you can configure the statebackend, checkpointing and restart strategy via the ``StreamExecutionEnvironment``. And now you can configure them by setting key-value options in ``TableConfig``, see [Fault Tolerance]({{< ref “docs/deployment/config” >}}#fault-tolerance), [State Backends]({{< ref “docs/deployment/config” >}}#checkpoints-and-state-backends) and [Checkpointing]({{< ref “docs/deployment/config” >}}#checkpointing) for more details.

The following code is an example showing how to configure the statebackend, checkpoint and restart strategy through the Table API:

.. code:: python

   # set the restart strategy to "fixed-delay"
   table_env.get_config().set("restart-strategy.type", "fixed-delay")
   table_env.get_config().set("restart-strategy.fixed-delay.attempts", "3")
   table_env.get_config().set("restart-strategy.fixed-delay.delay", "30s")

   # set the checkpoint mode to EXACTLY_ONCE
   table_env.get_config().set("execution.checkpointing.mode", "EXACTLY_ONCE")
   table_env.get_config().set("execution.checkpointing.interval", "3min")

   # set the statebackend type to "rocksdb", other available options are "hashmap"
   # you can also set the full qualified Java class name of the StateBackendFactory to this option
   # e.g. org.apache.flink.state.rocksdb.EmbeddedRocksDBStateBackendFactory
   table_env.get_config().set("state.backend.type", "rocksdb")

   # set the checkpoint directory, which is required by the RocksDB statebackend
   table_env.get_config().set("execution.checkpointing.dir", "file:///tmp/checkpoints/")

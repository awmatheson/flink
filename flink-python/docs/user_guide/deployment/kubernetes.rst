..  Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

..    http://www.apache.org/licenses/LICENSE-2.0

..  Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

==========
Kubernetes
==========

Kubernetes is a popular container-orchestration system for automating computer application deployment,
    scaling, and management.
This page shows you how to set up Python environment and execute PyFlink jobs in a Kubernetes cluster.

.. note::
   This guide focuses on PyFlink-specific setup for Kubernetes. For comprehensive Flink deployment instructions
       on Kubernetes,
   including cluster setup, configuration, and management, please refer to the
   `Flink Kubernetes Deployment Guide <https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/resource-providers/native_kubernetes/>`_.


Build PyFlink Image
-------------------

It requires Python 3.8 or above with PyFlink pre-installed to be available in the docker container.
It's suggested to use Python virtual environments to set up the Python environment.
See :ref:`create-a-python-virtual-environment <deployment/prepare:create-a-python-virtual-environment>` for more details on how
to prepare Python virtual environments with PyFlink installed.

You need install Python environments in the docker image with PyFlink pre-installed in advance.

To build a custom image which has Python and PyFlink prepared, you can refer to the following Dockerfile:

.. code-block:: bash

    FROM flink:2.0

    # install python3: it has updated Python to 3.11 in Debian 12 and so install Python 3.8 from source
    # it currently supports Python 3.8, 3.9, 3.10 and 3.11 in PyFlink officially.

    RUN apt-get update -y && \
    apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libffi-dev && \
    wget https://www.python.org/ftp/python/3.8.18/Python-3.8.18.tgz && \
    tar -xvf Python-3.8.18.tgz && \
    cd Python-3.8.18 && \
    ./configure --without-tests --enable-shared && \
    make -j6 && \
    make install && \
    ldconfig /usr/local/lib && \
    cd .. && rm -f Python-3.8.18.tgz && rm -rf Python-3.8.18 && \
    ln -s /usr/local/bin/python3 /usr/local/bin/python && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    # install PyFlink
    RUN pip3 install apache-flink==2.0


Execute PyFlink jobs in application mode with Native Kubernetes
---------------------------------------------------------------

You could execute PyFlink jobs in `application mode <https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/resource-providers/native_kubernetes/#application-mode>`_ as following:

This is useful when there is already a Kubernetes cluster available and you want to execute each Flink job in a separate
Flink cluster. Flink is responsible for talking with Kubernetes and allocating and de-allocating TaskManagers depending
on the required resources.

.. code-block:: bash

    ./bin/flink run-application \
          --target kubernetes-application \
          --parallelism 8 \
          -Dkubernetes.cluster-id=<ClusterId> \
          -Dtaskmanager.memory.process.size=4096m \
          -Dkubernetes.taskmanager.cpu=2 \
          -Dtaskmanager.numberOfTaskSlots=4 \
          -Dkubernetes.container.image=<PyFlinkImageName> \
          --pyModule word_count \
          --pyFiles /opt/flink/examples/python/table/word_count.py


Execute PyFlink jobs in session mode with Native Kubernetes
-----------------------------------------------------------

You could also starting a Flink session cluster on Kubernetes and then submit PyFlink jobs to the session cluster.

The session cluster could be started as following:

.. code-block:: bash

    ./bin/kubernetes-session.sh -Dkubernetes.cluster-id=my-first-flink-cluster

Then you could submit PyFlink jobs to the session cluster as following:

.. code-block:: bash

    ./bin/flink run \
        --target kubernetes-session \
        -Dkubernetes.cluster-id=my-first-flink-cluster \
        -pyarch /path/to/venv.zip \
        -pyexec venv.zip/venv/bin/python3
        -py word_count.py

.. note::
    Option **-pyclientexec** could be used to specify a local Python executable as the job will be compiled at the
    client side. Otherwise, if it's not specified, it will use the Python environment of the current shell environment.

See `Session Mode <https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/resource-providers/native_kubernetes/#session-mode>`_
for more details about session mode of Kubernetes.


Execute PyFlink jobs with Flink Kubernetes Operator
---------------------------------------------------

See `PyFlink Example <https://github.com/apache/flink-kubernetes-operator/tree/main/examples/flink-python-example>`_ for
more details on how to execute PyFlink jobs with Flink Kubernetes Operator.

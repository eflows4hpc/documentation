Workflow Execution Service
==========================

The Workflow Execution Service is a RESTful web service that provides a way for end users to execute workflows.
This component is developed specifically for the eFlows4HPC project.

This service will interact with Alien4Cloud list and trigger applicative workflows and with Hashicorp Vault to manage users access credentials.

The source code can be found in project repository_.

Installation
------------

The easiest way to install this service is to use docker.
A docker image is automatically published with latest changes under the name ``ghcr.io/eflows4hpc/hpcwaas-api:main``.

At press time there is no released version of this service yet.
We will follow semantic versioning to tag our releases and containers.
All the containers will be available in the project docker registry_.


Running the service using docker
--------------------------------

Please refer to the help of the hpcwaas-api container to know how to run it.

.. code:: bash

    docker run ghcr.io/eflows4hpc/hpcwaas-api:main /hpcwaas-api server --help

.. _repository: https://github.com/eflows4hpc/hpcwaas-api
.. _registry: https://github.com/eflows4hpc/hpcwaas-api/pkgs/container/hpcwaas-api

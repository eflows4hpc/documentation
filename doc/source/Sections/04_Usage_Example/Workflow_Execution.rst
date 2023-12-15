.. _section_workflow_execution:

Credentials setup and Workflow Execution
========================================

As a end-user in eFlows4HPC, the process of executing workflows involves defining inputs and triggering the workflow execution via the
HPCWaaS API. This section provides guidance for end-users to perform these tasks effectively.

Download required tools
-----------------------

Visit the `HPCWaaS API release page on GitHub <https://github.com/eflows4hpc/hpcwaas-api/releases>`_ to download a binary version of
the ``waas`` Command Line Interface (CLI) that is compatible with your computer.

Alternatively, a Docker image (ghcr.io/eflows4hpc/hpcwaas-api:main-cli) containing the CLI can also be obtained.
To utilize the Docker image, the following command can be executed in the terminal:

.. code-block:: bash

    docker run -ti --rm ghcr.io/eflows4hpc/hpcwaas-api:main-cli help

This is equivalent to executing:

.. code-block:: bash

    ./waas help

SSO authentication
------------------

The `waas` CLI uses Unity for authentication. For each request, the user needs to provide a valid access token. This token can be retrieved by logging in (in a browser) to the `/auth/login` endpoint of your HPCWaaS server.
You can then use this token to launch `waas` commands. For example:

.. code-block:: bash

    ./waas -t=<access_token> workfows list

It is also possible to pass this token by setting a `HW_ACCESS_TOKEN` environment variable or by adding `access_token: <access_token>` to your `waas` config file.  
  
For more information on how to generate and use access tokens, please refer to the HPCWaaS documentation.

Setup your credentials
----------------------

To enable secure data transfer and execution of workflows, it is necessary to generate a pair of private and public SSH keys using the CLI.
The system generates the key pair and securely stores it in a Vault, with the private key being kept confidential and not accessible.

The public key and key ID are returned upon successful key pair generation and should be carefully recorded as they cannot be retrieved later

.. code-block:: bash

    $ ./waas --api_url <api_url> -t=<access_token> ssh_keys key-gen
    INFO: Below is your newly generated SSH public key.
    INFO: Take note of it as you will not see it again.
    INFO: You are responsible for adding it to the authorized_keys file on the systems you want to run your workflows.

    INFO: SSH key ID: 31...3f
    INFO: SSH Public key: ssh-rsa AAA...mH

To grant access to the designated HPC clusters, the SSH Public Key generated during the key pair generation process must be copied to
the ``authorized_keys`` file located in the ``.ssh`` directory of the user's home directory (``${HOME}/.ssh/authorized_keys``).

List available workflows
------------------------

.. code-block:: bash

    ./waas --api_url <api_url> -t=<access_token> workflows list


The above command lists the workflows accessible to you. Take note of the workflow ID of the desired workflow for the next step.


Trigger a workflow execution
----------------------------

To initiate the execution of a workflow, you must first determine the inputs required for the workflow from the Workflow developer.
Then, execute the following command to trigger the workflow execution:

.. code-block:: bash

    ./waas --api_url <api_url> -t=<access_token> workflows trigger -f \
        -i input1Name=input1Value -i input2Name=input2Value \
        <workflow_id>


Monitor a workflow execution
----------------------------

In order to monitor a workflow execution, one can use the ``-f`` flag on the ``trigger`` command. This flag enables the continuous
retrieval of the execution status from the HPCWaaS API.

Alternatively, the execution status can be obtained using the ``execution status`` command along with the Execution ID, which is
returned by the ``trigger`` command. The syntax for this command is as follows:

.. code-block:: bash

    ./waas --api_url <api_url> -t=<access_token> executions status <Execution_ID>


It is to be noted that the ``execution status`` command also has its own ``-f`` flag, which can be used for continuously
monitoring the execution status.

Cancel a workflow execution
---------------------------

You may cancel a workflow execution that is currently in progress by utilizing the ``executions cancel`` command.

.. code-block:: bash

    ./waas --api_url <api_url> -t=<access_token> executions cancel <Execution_ID>

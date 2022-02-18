Software Invocation Description
===============================

The idea behind the 'Software' invocation description is to define a common way in which multiple software components can be integrated in single workflow. The definition is composed of a decorator and a configuration file with the necessary parameters.

Software decorator
------------------
@software decorator is used to indicate that a certain python function represents the invocation of and external HPC or DA programs in a single workflow. This decorator must be combined with the 'task' decorator to indicate de directionality of the parameters and allow the runtime to detect the dependencies with the rest of workflow tasks.
When a `task` with the `@software` decorator is called, an external program is executed respecting the configuration defined in its configuration file. The goal of this decorator is to describe the execution of whatever external programs included in a workflow from simple binary executable to complex MPI applications.


Configuration File
------------------
A configuration file must have two mandatory keys; `type` and `properties`. 'Type' is needed to specify exactly what type of program the user wants to execute (e.g: "mpi",
"binary"). And the `properties` will contain the customizable properties of a type of execution such as binary path, number of processes, etc.


Examples
--------

As an example, the following code snippets show how an MPI application execution can be defined using the @software decorator. Users only have to add the software
decorator on top of the task function, and provide a 'config_file' parameter where the configuration details are defined:

.. code-block:: python

    from pycompss.api.software import software
    from pycompss.api.task import task

    @software(config_file="mpi_config.json")
    @task()
    def task_python_mpi():
         pass

And inside the configuration file the type of program, and its properties are explicitly set. For example, if the user wants to run an MPI job with two processes using
'mpirun' command, the configuration file (**"mpi_config.json"** in this example) should look like as follows:

.. code-block:: JSON

  {
    "type":"mpi",
    "properties":{
        "runner": "mpirun",
        "binary": "app_mpi.bin",
        "processes": 2
    }
  }

Finally, call to the task function from the main program:

.. code-block:: python

    task_python_mpi()


It is also possible to refer to task parameters from the configuration file. Properties such as `working_dir` and `params` ('params' strings are command
line arguments to be passed to the 'binary') can contain this kind of references. In this case, the task parameters should be surrounded by curly braces. For example, in the
following example, 'work_dir' and 'param_d' parameters of the python task are used in the 'working_dir' and 'params' strings, respectively . Moreover, the number of computing
units is added as a constraint, to indicate that every MPI process will have this requirement (run with 2 threads):

Task definition:

.. code-block:: python

    from pycompss.api.software import software
    from pycompss.api.task import task

    @software(config_file="mpi_w_params.json")
    @task()
    def task_mpi_w_params(work_dir, param_d):
         pass


Configuration file ("mpi_w_params.json"):

.. code-block:: JSON

  {
    "type":"mpi",
    "properties":{
        "runner": "mpirun",
        "binary": "parse_params.bin",
        "working_dir": "/tmp/{{work_dir}}",
        "params": "-d {{param_d}}"
    },
    "constraints":{
        "computing_units": 2
    }
  }

Call to the task function:

.. code-block:: python

    task_mpi_w_params('my_folder', 'hello_world')


Another example can be when the external program is expected to run within a container. For that, the user can add the `container` configuration to the JSON file
by specifying its 'engine' and the 'image'. At the time of execution, the Runtime will execute the given program within the container. For example, in order to run a
simple 'grep' command that searches for a pattern (e.g. an 'error' ) in the input file within a Docker container, the task definition and the configuration file should
be similar to the examples below:

Task definition:

.. code-block:: python

    from pycompss.api.parameter import FILE_IN
    from pycompss.api.software import software
    from pycompss.api.task import task

    @software(config_file="container_config.json")
    @task(in_file=FILE_IN)
    def task_container(in_file, expression):
         pass


Configuration file ("container_config.json"):

.. code-block:: JSON

  {
    "type":"binary",
    "properties":{
        "binary": "grep",
        "params": "{{expression}} {{in_file}}"
    },
    "container":{
		"engine": "DOCKER",
		"image": "compss/compss"
	}
  }

Call to the task function:

.. code-block:: python

   task_container('some_file.txt', 'error')




.. warning::

   Limitation: Currently it is not possible to run MPI jobs within containers.


For more detailed information about the @software decorator of PyCOMPSs please see the `documentation`_.


.. _documentation: https://compss.readthedocs.io/en/latest/Sections/02_App_Development/02_Python/01_Task_definition/Sections/06_Other_task_types.html#software-decorator

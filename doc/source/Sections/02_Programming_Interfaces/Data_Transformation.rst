Data Transformation
~~~~~~~~~~~~~~~~~~~

The *@data_transformation* (or just *@dt*) decorator is used for the execution of a data transformation function that should be applied on a given
```PyCOMPSs task``` parameter. It means, by specifying the parameter name and a python function, users can assure that the parameter will go through
transformation process by the given function. Then the result of the data transformation function will be used in the task instead of the initial
value of the parameter.


Data transformation decorator has a simple order for the definition. The first argument of the decorator is a string name of the parameter we want to
transform. The second argument is the data transformation function (NOT as a string, but actual reference) that expects at least one input which will
the transformation will be applied to. If the transformation function needs more parameters, they can be added to the *@dt* definition as ```kwargs```.

.. code-block:: python
    :name: dt_sytax
    :caption: Arguments list of the data transformation decorator.

    @dt("<parameter_name>", "<dt_function>", "<kwargs_of_dt_function>")
    @task()
    def task_func(...):
        ...


.. IMPORTANT::

    Please note that data transformation definitions should be on top of the *@task* (or *@software*) decorator.


Adding data transformation on top of the ```@task``` decorator allows the PyCOMPSs Runtime generate an intermediate task. This task method applies the given DT
to the given input and the output is sent to the *original* task as the input. Following code snippet is an example of basic usage of the *@dt* decorator:


.. code-block:: python
    :name: dt_bsic
    :caption: An example of data transformation decorator.

    from pycompss.api.data_transformation import dt
    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on

    def append_dt(A):
        A.append("from_dt")
        return A

    @dt("A", append_dt)
    @task()
    def task_func(A):
        A.append("from_task_itself")
        return A

    def main():
        A = ["initial_value"]
        A = compss_wait_on(task_func(A))
        print(A)


When the ```main``` function called, a new list called ```A``` will be initialized with one element and will be sent to a PyCOMPSs task called ```task_func```.
Then, a call to "task_func" method results in generation of 2 tasks by the PyCOMPSs Runtime. The first task accepts the initial list and adds "from_dt"
element to it. Then the modified list is passed to the "task_func" defined by the user and "from_task_itself" is added to the list. As a result, the output of
code above is a list with 3 elements including those were added by the data transformation and the "task_func" tasks.

If the user wants to use a workflow as a data transformation function and thus avoid the intermediate task creation, PyCOMPSs provides the ```is_workflow```
argument to do so (by default *False*). This gives the flexibility of importing workflow from different libraries.

It is also possible to define multiple data transformation functions for the same parameter, as well as for the multiple parameters from the same task. In both
cases each data transformation with "is_workflow=False" will take place in a different task:



.. code-block:: python
    :name: dt_multiple
    :caption: Example: multiple data transformations for a single task method.

    from pycompss.api.data_transformation import dt
    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on

    @task()
    def bb(A):
        A.append("from_bb")
        return A

    @task()
    def aa(A):
        A.append("from_aa")
        return A

    # calls 2 @task functions for a given input
    def workflow_dt(A):
        return aa(bb(A))

    # regular python task that appends a given value to the input list
    def appender_w_param(a_list, item):
        a_list.append(item)
        return a_list


    @dt("A", appender_w_param, item="dt_no_workflow")
    @dt("A", workflow_dt, is_workflow=True)
    @dt("B", appender_w_param, item="dt_no_workflow")
    @dt("B", workflow_dt, is_workflow=True)
    @task()
    def task_func(A, B):
        A.append("task itself")
        B.append("task itself")
        return A, B


In the example above, input parameter A is meant to be modified 2 times sequentially: first, "appender_w_param" function is called within a separate task and
its output is sent to the next data transformation which is a *workflow*. The "workflow_dt" function consists of 2 PyCOMPSs tasks executed one after another.
Only applying all these transformations to the initial value of *A*, it's passed to the "task_func" as the input. The same scenario applies for the parameter
B.

Moreover, PyCOMPSs supports inter-types data transformations which allows the conversion of the input data to another object type. For example, if the user wants to use
a object's serialized file as an input for a task, but the task function expects the object itself, then ```@dt``` can take care of it. So far PyCOMPSs supports this kind
of data transformations only for the ```FILE```, ```OBJECT``` and ```COLLECTION``` types.

For the cases where type conversions happen, there are some mandatory parameters:

    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                             |
    +========================+=========================================================================================================================================+
    | **target**             | (Mandatory) Name of the input parameter that DT will be applied to.                                                                     |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **function**           | (Mandatory) The data transformation function.                                                                                           |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **type**               | (Mandatory) Type of the DT (e.g. FILE_TO_OBJECT)                                                                                        |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **destination**        | If the output of the DT is a file, then output file name can be specified as "destination".                                             |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **size**               | (Mandatory only if the output of the DT is a COLLECTION) Size of the output COLLECTION.                                                 |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

Following code snippet shows how the **@dt** decorator can be used for "file to object" conversion:


.. code-block:: python
    :name: dt_fto
    :caption: Data Transformation with type conversion.

    from pycompss.api.data_transformation import *
    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on

    def fto(some_file):
        ret = None
        # deserialize the file
        ...

        return ret

    @dt(target="data", function=fto, type=FILE_TO_OBJECT)
    @task()
    def file_to_object(data):
        # 'data' is deserialized object from its initial file
        ...

    def main(self):
        in_file = "src/infile.pickle"
        result = file_to_object(in_file)
        result = compss_wait_on(result)


PyCOMPSs API also provides Data Transformation Object class which gives the flexibility of the data transformation definitions. Any task function can be
decorated with an empty **@dt** and simply by passing *DTO*\(s) as a task parameter the user can achieve the same behaviour. Same as the decorator itself, DTO
accepts the arguments in the same order (*"<parameter_name>", "<dt_function>", "<kwargs_of_dt_function>"*). A list of DTO objects is also accepted for the same or
various parameters:


.. code-block:: python
    :name: dt_dto
    :caption: Data Transformation Object example.

    from pycompss.api.data_transformation import dto
    from pycompss.api.data_transformation import dt
    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on


    @dt()
    @task()
    def dto_basic(A, B):
        A.append("from_task")
        B.append("from_task")
        return A

    def appender(a_list):
        a_list.append("from_dt")
        return a_list

    def dto_example(self):
        A = ["initial"]
        B = ["initial_B"]

        # create Data Transformation Objects
        dt_1 = dto("A", appender)
        dt_2 = dto("B", appender, is_workflow=False)

        # send DT Objects to the task function as input
        A = cwo(dto_basic(A, B, dt=[dt_1, dt_2]))

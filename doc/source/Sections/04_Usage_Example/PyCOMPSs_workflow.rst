PyCOMPSs Workflow
=================
PyCOMPSs is a task-based programming model which allow to define parallel workflows as simple sequential python scripts. To implement a PyCOMPSs application, developers has to identify what parts of an application are the candidates to be a task. They are usually python methods with a certain computation granularity (larger than hundred milisecons) that can potentially run concurrently with other parts of the application.
Those methods have to be annotated with the `@task` decorator to indicate the directionality of they parameters.

:numref:`wordcount` shows how to program a PyCOMPSs workflow for counting the words in a folder. The code is similar to what a developer will write in a sequential python code.
Two methods are defined in the application: the `wordcount` to count the words of a file; and the `merge_dicts` to merge the results of the separate `wordcount` tasks.
On top of these methods, we have added the `@task` decorator to convert it to a PyCOMPSs task, indicating the directionality of the parameters and returns.
Based on these annotations, the COMPSs runtime will detect that all `wordcount` invocations are independent and the `merge_dicts` ones will depend to the `wordcount` task
of the same iteration and the `merge_dicts` of the previous one.


.. code-block:: python
    :name: wordcount
    :caption: PyCOMPSs wordcount example

    @task(file_path=FILE_IN, returns=dict)
    def wordCount(file_path):
        """ Construct a frequency word dictorionary from a list of words.
        :file_path: file to count words
        :return: a dictionary where key=word and value=#appearances
        """
        partialResult = {}
        with open(file_path, 'r') as f:
            for line in f:
                data = line.split()
                for entry in data:
                    if entry in partialResult:
                        partialResult[entry] += 1
                    else:
                        partialResult[entry] = 1
        return partialResult


    @task(returns=dict, priority=True)
    def merge_dicts(dic1, dic2):
        """ Update a dictionary with another dictionary.
        :param dic1: first dictionary
        :param dic2: second dictionary
        :return: dic1+=dic2
        """
        for k in dic2:
            if k in dic1:
                dic1[k] += dic2[k]
            else:
                dic1[k] = dic2[k]
        return dic1


    if __name__ == "__main__":
        from pycompss.api.api import compss_wait_on

        # Get the dataset path
        pathDataset = sys.argv[1]

        # Read file's content execute a wordcount on each of them
        partialResult = []
        for fileName in os.listdir(pathDataset):
            path = os.path.join(pathDataset, fileName))
            partialResult.append(wordCount(path))

        # Accumulate the partial results to get the final result.
        result = {}
        for partial in partialResult:
            result = merge_dicts(result, partial)

        # Synchronize remote result
        result = compss_wait_on(result)

        # Print the results and elapsed time
        print("Word appearances:")
        from pprint import pprint
        pprint(result)


A part from python methods, developers can integrate executions of other software in PyCOMPSs workflows by means of the `@software` decorator described in the `Software invocation description <../02_Programming_Interfaces/Software_Description.rst>`_ section.

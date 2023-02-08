dislib
======

The `Distributed Computing Library`_ (dislib) is a library that provides various distributed machine-learning algorithms.
It has been implemented on top of `PyCOMPSs`_, with the goal of facilitating the execution of big data
analytics algorithms in distributed platforms, such as clusters, clouds, and supercomputers.

Dislib comes with two primary programming interfaces: an API to manage data in a distributed way and an estimator-based interface to work with different
machine learning models.

Dislib main data structure is the distributed array (ds-array) that enables to distribute the data sets in multiple nodes of a computing infrastructure. The
typical workflow in dislib consists of the following steps:

* Reading input data into a ds-array.

* Creating an estimator object.

* Fitting the estimator with the input data.

* Getting information from the model’s estimator or applying the model to new data.


Some useful links for more detailed information:

1. `Source code`_.
2. `Installation`_.
3. `Tutorial`_.


.. _Distributed Computing Library: https://dislib.bsc.es/
.. _PyCOMPSs: https://www.bsc.es/research-and-development/software-and-apps/software-list/comp-superscalar/
.. _Source code: https://github.com/eflows4hpc/dislib
.. _Installation: https://dislib.readthedocs.io/en/stable/quickstart.html#quickstart-guide
.. _Tutorial: https://compss.readthedocs.io/en/stable/Sections/10_Tutorial/07_Dislib.html

ParSoDA
=======
ParSoDA (Parallel Social Data Analytics) is a high-level library for developing parallel data mining applications based on the extraction of useful knowledge from large data set gathered from social media. The library aims at reducing the programming skills needed for implementing scalable social data analysis applications.

The main idea behind ParSoDA is to simplify the creation of data analysis applications, making some aspects of development transparent to the programmer. The main effort for developing ParSoDA was to create a set of interfaces, abstract classes and concrete classes that could be reused several times and in a modular way for composing scalable and distributed data analysis workflows. The first prototype of ParSoDA was built on Apache Hadoop. Another version of ParSoDA based on Spark has been implemented. The Spark version has proven to offer several performance benefits compared to the Hadoop-based version. During the last months we have implemented a new version based on PyCOMPSs which is described later in this document.

Source code of ParSoDA
----------------------
The source code of ParSoDA is available `here`_.

.. _here: https://github.com/SCAlabUnical/ParSoDA

The current version of the library (v. 1.3.0 dated October 25, 2018) contains more than forty predefined functions organized in seven packages, corresponding to the seven ParSoDA steps.

Installation and use of ParSoDA
-------------------------------
The software requirements of ParSoDA are:

- Java JDK 1.8 or higher

- Maven as dependency manager and build automation tool. We used Maven for our convenience, but it doesn't mean that other valid solutions, such as Gradle, can't be used.

- GIT as versioning tool

The current version of ParSoDA has been tested with Hadoop 2.7.4, but we are working on addressing some minor issues to make it work with Hadoop version 3.

On the ParSoDA project available on GitHub, you can find a dedicated branch containing a docker-compose file that can be used to quickly deploy a Hadoop cluster with only 1 node, which can be used to test ParSoDA applications.

1) Clone the master branch of the `ParSoDA’s project from GitHub`_::

    git clone --branch master https://github.com/SCAlabUnical/ParSoDA.git

.. _ParsoDA’s project from GitHub: https://github.com/SCAlabUnical/ParSoDA

2) After cloning the project, you have to launch the following command to download and install all the project dependencies::

    mvn install

3) If required, add to the Maven project any external libraries you need. For example, the sample applications presented today required two external JAR libraries. In particular, we used **SPMF**, which is an open-source data mining library written in Java, specialized in pattern mining. We also used a Hadoop implementation of the well-known PrefixSpan algorithm, called **MGFSM**, to extract frequent sequential patterns. To import these libraries, you can run the following commands::

    mvn install:install-file -Dfile=./libs/spmf.jar -DgroupId=ca.pfv.spmf -DartifactId=spmf -Dversion=1.0.0 -Dpackaging=jar

    mvn install:install-file -Dfile=./libs/mgfsm-hadoop.jar  -DgroupId=de.mpii.fsm -DartifactId=mgfsm-hadoop -Dversion=1.0.0 -Dpackaging=jar


4) Finally, to build an executable JAR you can use the following command::

    mvn package.

The library code has been organized into packages, which follow the 7 main steps that compose the execution flow of ParSoDA: acquisition, filtering, mapping, reduction, partitioning, analysis, and visualization.
It is organized in packages among which we find the followings:

- The package “*app*” contains some runnable example of data analysis applications based on ParSoDA;

- The package “*common*” contains the core classes of ParSoDA, including data models, intefaces, abstract classes, and so on;

- The package “*acquisition*” contains the classes of some data crawlers that can be used for collecting data from social media platforms. Currently, it contains 2 crawlers for social media platforms (i.e., Twitter and Flickr), plus a dummy crawler (called *FileReaderCrawler*) that allow to load data from local filesystem or HDFS filesystem;

- All other packages contains some pre-built functions for each corresponding block of a ParSoDA application.

Parsoda-Py
==========
ParSoDA has been redesigned in Python to support the use of the Python libraries ecosystem. ParSoDA-Py has been extended to support multiple execution runtimes. Specifically, according to the bridge design pattern, we defined the ParsodaDriver interface (i.e., the implementor of the bridge pattern) that allows a developer to implement adapters for different execution systems. A valid instance of ParsodaDriver must invoke some function that exploits some parallel pattern, such as Map, Filter, ReduceByKey and SortByKey. The SocialDataApp class is the abstraction of the bridge pattern and is designed to use these parallel patterns efficiently for running ParSoDA applications. It is worth noting that the execution flow of an application remains unchanged even by changing the execution runtime, which makes the porting of a ParSoDA application to new execution runtimes.

In particular, we included four execution drivers into ParSoDA-Python:

- ParsodaSingleCoreDriver, a driver that implements parallel patterns as simple sequential algorithms to be run on a single core, on the local machine. It is useful for verifying the correctness of a new ParSoDA Driver during its construction.

- ParsodaMultiCoreDriver, which runs the application in parallel on multiple cores, on the local machine, using Python multiprocessing package.

- ParsodaPySparkDriver, which runs the application on a Spark cluster. It is based on the PySpark library and requires the initialization of a SparkConf object.

- ParsodaPyCompssDriver, which runs the application on a COMPSs cluster. It relies on the PyCOMPSs binding to gain access to the COMPSs runtime.

Source code of ParSoDA-Py
-------------------------
The code of ParSoDA-Py library is available in this `repository`_.

.. _repository: https://github.com/eflows4hpc/ParSoDA-Py

Installation and use of ParSoDA-Py
----------------------------------
The ParSoDA library requires Python 3.8 or above.

To install the current version of ParSoDA on a Python environment 
you just need to put the ParSoDA package into some directory,
then it can be used in a new application that can be run on the 
local environment. 

To use ParSoDA on top of PyCOMPSs or PySpark, 
you need to install and correctly configure one or both these two 
environments. At that point the application can be run through the 
ParsodaPyCompssDriver or the ParsodaPySparkDriver classes.
The current experimental version of ParSoDA comes with two example
applications, Trajectory Mining and Sentiment Analysis, which
requires the following python packages to be installed::

    emoji==1.7.0
    fastkml==0.12
    geopy==2.2.0
    shapely==1.8.1

The ParSoDA package contains a file “requirements.txt” which can be used with pip to install the application requirements, executing the following command in the root directory of ParSoDA::

    python3 -m pip install -r requirements.txt

Installing ParSoDA-Py through pip
---------------------------------
ParSoDA can be installed by pip through the setup.py script. You just need to change current directory to the root of this repository

    cd <ParSoDA repo root directory>

and run

    pip3 install .

Docker containers
-----------------
For testing or developing ParSoDA-Py library and applications, a Docker container can be created from the Dockerfile included into the repository.
In order to build the Docker image, run the following command in the root of the ParSoDA-Py repository:

    docker build . -t "<your image name>"

Then, you can create the development container by setting up the following docker stack::

    version: '3'
    services:
        parsoda:
            image: <your image name>
            restart: unless-stopped

ParSoDA-Py on top of PyCOMPSs
-----------------------------

The following example shows the Trajectory Mining application written with ParSoDA-Py, running on the PyCOMPSs environment::

    driver = ParsodaPyCompssDriver()

    app = SocialDataApp("Trajectory Mining", driver, num_partitions=args.partitions, chunk_size=args.chunk_size)

    app.set_crawlers([
        LocalFileCrawler('/root/dataset/FlickrRome2017.json', FlickrParser())
        LocalFileCrawler('/root/dataset/TwitterRome2017.json', TwitterParser())
    ])
    app.set_filters([
        IsInRoI("./resources/input/RomeRoIs.kml")
    ])
    app.set_mapper(FindPoI("./resources/input/RomeRoIs.kml"))
    app.set_secondary_sort_key(lambda x: x[0])
    app.set_reducer(ReduceByTrajectories(3))
    app.set_analyzer(GapBIDE(1, 0, 10))
    app.set_visualizer(
        SortGapBIDE(
            "./resources/output/trajectory_mining.txt",
            'support',
            mode='descending',
            min_length=3
        )
    )

    app.execute()


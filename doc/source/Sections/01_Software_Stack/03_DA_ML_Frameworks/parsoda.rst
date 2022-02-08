ParSoDA
=======
ParSoDA (Parallel Social Data Analytics) is a high-level library for developing parallel data mining applications based on the extraction of useful knowledge from large data set gathered from social media. The library aims at reducing the programming skills needed for implementing scalable social data analysis applications.

The main idea behind ParSoDA is to simplify the creation of data analysis applications, making some aspects of development transparent to the programmer. The main effort for developing ParSoDA was to create a set of interfaces, abstract classes and concrete classes that could be reused several times and in a modular way for composing scalable and distributed data analysis workflows. The first prototype of ParSoDA was built on Apache Hadoop. Another version of ParSoDA based on Spark has been implemented. The Spark version has proven to offer several performance benefits compared to the Hadoop-based version. We are now working on a new version based on PyCOMPSs.


Source code
-----------
The source code of ParSoDA is available here: https://github.com/SCAlabUnical/ParSoDA

The current version of the library (v. 1.3.0 dated October 25, 2018) contains more than forty predefined functions organized in seven packages, corresponding to the seven ParSoDA steps.

Installation and use guide
--------------------------
The software requirements of ParSoDA are: 

- Java JDK 1.8 or higher

- Maven as dependency manager and build automation tool. We used Maven for our convenience, but it doesn't mean that other valid solutions, such as Gradle, can't be used.

- GIT as versioning tool

The current version of ParSoDA has been tested with Hadoop 2.7.4, but we are working on addressing some minor issues to make it work with Hadoop version 3.

On the ParSoDA project available on GitHub, you can find a dedicated branch containing a docker-compose file that can be used to quickly deploy a Hadoop cluster with only 1 node, which can be used to test ParSoDA applications.

1) Clone the master branch of the `ParsoDA’s project from GitHub`_::

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

There is also a package named “*app*” that contains some runnable example of data analysis applications based on ParSoDA. In addition, the package “*common*” contains the core classes of ParSoDA, including data models, intefaces, abstract classes, and so on. The first package “*acquisition*” contains the classes of some data crawlers that can be used for collecting data from social media platforms. Currently, it contains 2 crawlers for social media platforms (i.e., Twitter and Flickr), plus a dummy crawler (called *FileReaderCrawler*) that allow to load data from local filesystem or HDFS filesystem.

As a general setting, all the ParSoDA library is organized according to the following approach: INTERFACE --> ABSTRACT CLASS --> CONCRETE CLASS. Thus, ParSoDA provides some ready-to-use concrete classes, but at the same time it enables developers to create their own functions. This means, for example, that a specific data crawler could be developed to acquire data from a different file system or data storage, such as Amazon AWS S3, NoSQL Databases, and so on.


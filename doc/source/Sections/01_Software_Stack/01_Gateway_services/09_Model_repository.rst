Model Repository
======================

The service provides a means for scientific users to store serialized models along with the metadata 
describing their machine learning/AI experiments. The model repository service is a new addition to 
the eFlows4HPC software stack in the 2nd year of the project. The model repository is based on 
the open source MLflow_ software, which is widely used in the AI/ML community. 

We envision the following scenarios for the model repository. In case of 
interactive access (e.g. via Jupyter notebook), where model training parameters, 
evaluation metrics and other metadata can be uploaded directly into the repository. Alternatively,
 if model training is done offline, locally collected metadata is uploaded to the model repository 
 during the stage-out phase using the Data Logistics Service (examples can be found in examples_). 
Finally, users in the project and  beyond can browse the model repository, compare the metadata, 
and download the models for reuse. 

 The current pilot version of the Model Repository supports these three use cases and will be evaluated 
 by users in the coming months to address additional requirements. In addition, we have prepared 
 examples_ for all use cases and integrated the model repository into the eFlows4HPC software stack 
 by implementing the required DLS pipeline and TOSCA component. 


The service is based on MLflow_ open source software. The project specific extensions can be found 
in the project repository_.

There is an instance of the model repository service hosted in Julich HDF could which can be accessed_.



.. _MLflow: https://mlflow.org
.. _repository: https://github.com/eflows4hpc/model-repository
.. _dagrepo: https://github.com/eflows4hpc/dls-dags
.. _examples: https://github.com/eflows4hpc/model-repository/tree/main/notebooks
.. _documentation: https://mlflow.org/docs/latest/index.html
.. _accessed: https://modelrepository.eflows4hpc.eu
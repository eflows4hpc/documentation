The following code snippet

@Software(config=mpi_description.json)
@task(input_file= FILE_IN, output_file=FILE_OUT)
def hpc_simulation (input_file, output_file):
   pass

@data_transformation(action=load_and_rechunk, data=train_data_set, action_arguments=partitions)
@Software(config=_python_ml_framework.json)
@task(train_data_set=COLLECTION_IN, returns=1)
def ml_train(train_data_set, partitions):
   ...
   # Python code for doing the ml training

def main():
  ...
  output_data = []
  for input, output in simulations:
       hpc_simulation(input, output)
       output_data.append(ouput)
  model = ml_train(output_data, 20)

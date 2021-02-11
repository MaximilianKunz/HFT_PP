import pandas as pd
import numpy as np
from import_datasets_class import ReadSedResults

# Import of the Active Layer File
active_layer = ReadSedResults(file_name = "Datasets_AL.dat")
active_layer.get_data(file_name = "Datasets_AL.dat")

# Reading the Timesteps from the Active Layer File
active_layer.get_timesteps(file_name = "Datasets_AL.dat")
print("Number of time steps: {0}".format(active_layer.timesteps))
active_layer.create_list_timesteps(file_name="Datasets_AL.dat")
print("List of timesteps")
print(active_layer.list_timesteps)

# Transform the Data of the Active Layer File
active_layer.transform_data()
print(active_layer.data_transformed)
print(active_layer.data_transformed.dtypes)
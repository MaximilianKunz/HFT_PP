from import_datasets_class import *
from import_2dm_class import *

# Read no. of nodes and no. of fractions from 2dm files
sim_data = read2DM()
# sim_data.get_num_nodes() does not work yet
# sim_data.get_num_fractions() does not work yet

# Import of the Active Layer File
active_layer = ReadSedResults(file_name="Datasets_AL.dat")
active_layer.get_data(file_name="Datasets_AL.dat")

# Import number of nodes and fractions from 2dm file
# active_layer.nodes = sim_data.num_nodes does not work yet
active_layer.nodes = 61803
print("Number of nodes: {0}".format(active_layer.nodes))
# active_layer.fractions = sim_data.num_fractions does not work yet
active_layer.fractions = 8
print("Number of fractions: {0}".format(active_layer.fractions))

# Calculate no. of datasets
active_layer.get_datasets()
print("Number of datasets: {0}".format(active_layer.datasets))

# Reading the Timesteps from the Active Layer File
active_layer.get_timesteps(file_name="Datasets_AL.dat")
print("Number of time steps: {0}".format(active_layer.timesteps))

# Creating a list of timesteps
active_layer.create_list_timesteps(file_name="Datasets_AL.dat")
# print("List of timesteps:")
# print(active_layer.list_timesteps)

# Creating a list of timesteps for the columns
active_layer.create_list_timesteps_columns()

# Creating a list of simulation time for the columns
active_layer.create_list_time_columns()

# Transform the Data of the Active Layer File
active_layer.transform_data()
print(active_layer.data_transformed)
print(active_layer.data_transformed.dtypes)

# Export Dataframe as CSV-file
active_layer.data_transformed.to_csv('Data_transformed.csv', index=False)
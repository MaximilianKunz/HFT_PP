from import_datasets_class import ReadSedResults

# Import of the Active Layer File
active_layer = ReadSedResults(file_name = "Datasets_AL.dat")
active_layer.get_data(file_name = "Datasets_AL.dat")

# Reading the Timesteps from the Active Layer File
active_layer.get_timesteps(file_name = "Datasets_AL.dat")
print("Number of time steps: {0}".format(active_layer.timesteps))

# Creating a list of timesteps
active_layer.create_list_timesteps(file_name="Datasets_AL.dat")
print("List of timesteps:")
print(active_layer.list_timesteps)

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
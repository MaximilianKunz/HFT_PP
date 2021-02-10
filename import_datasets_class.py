import pandas as pd
import numpy as np

class ReadSedResults:
    def __init__(self, file_name="Datasets_Al.dat"):
        self.nodes = 61803  # should be read from .2dm file
        self.fractions = 8  # should be read from .2dm file
        self.datasets = self.fractions +2
        self.data_imported = pd.DataFrame
        self.get_data(file_name)
        self.data_transformed = pd.DataFrame
        self.transform_data()
        self.timesteps = int()
        self.list_timesteps = []
        self.get_timesteps(file_name)

    def get_data(self, file_name):
        df_import = pd.read_table(file_name, skiprows=1)
        self.data_imported = df_import.rename(columns={'OBJTYPE "mesh2d"': 'Datasets'})

    def get_timesteps(self, file_name):
        file = open(file_name)
        timestep = 0
        for line in iter(file):
            if line.startswith('TS'):
                timestep += 1
        self.timesteps = int(round(timestep / self.datasets))

    def create_list_timesteps(self, file_name):
        file = open(file_name)
        tstep = []
        for line in iter(file):
            if line.startswith('TS'):
                tstep.append(line.split())
        tstep = np.asanyarray(tstep)
        tstep2 = np.delete(tstep, 0, 1)
        tstep3 = np.asanyarray(tstep2).astype(float)
        self.list_timesteps = tstep3[0:self.timesteps:1, 1]

    def transform_data(self):
        # read total number of lines from the dataframe
        lines = self.data_imported.shape[0]
        # calculate the length of one dataset (no. of lines)
        length_datasets = int(round(lines / self.datasets))
        # transform dataframe to array
        array_unsorted = self.data_imported.to_numpy()
        # transform array to array with one line for each dataset
        array_sorted = array_unsorted.reshape(self.datasets, length_datasets)
        # transpose array to array with one column for each dataset
        array_sorted_transposed = np.transpose(array_sorted)
        # create list of column names
        columns = ["Fraction{0}".format(str(i)) for i in np.arange(1, self.fractions + 1, 1)]
        columns.append("Mean diameter")
        columns.append("Layer thickness")
        # turn array back to dataframe
        self.data_transformed = pd.DataFrame(array_sorted_transposed, columns=columns)

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
import pandas as pd
import numpy as np

class ReadSedResults:
    def __init__(self, file_name="Datasets_Al.dat"):
        """
        This class reads the result files of a Hydro-FT simulation and transforms them into an array (Pandas Dataframe).
        The class was written by Max with assistance of Maria for the get_timesteps and create_list_timesteps functions.
        :param file_name: File name of either the Dataset of the Active Layer or Under Layer to import
        """
        self.nodes = int()  # should be read from .2dm file
        self.fractions = int()  # should be read from .2dm file
        self.datasets = int ()
        self.get_datasets()
        self.data_imported = pd.DataFrame
        self.get_data(file_name)
        self.timesteps = int()
        self.get_timesteps(file_name)
        self.list_timesteps = []
        self.create_list_timesteps(file_name)
        self.list_timesteps_columns = []
        self.create_list_timesteps_columns()
        self.list_time_columns = []
        self.create_list_time_columns()
        self.data_transformed = pd.DataFrame
        self.transform_data()

    def get_datasets(self):
        self.datasets = self.fractions + 2

    def get_data(self, file_name):
        """
        Imports the result file and turns it into a Pandas Dataframe
        :param file_name: File name of the Layer Dataset to import
        :return: Pandas Dataframe of the imported Dataset
        """
        df_import = pd.read_table(file_name, skiprows=1)
        self.data_imported = df_import.rename(columns={'OBJTYPE "mesh2d"': 'Datasets'})

    def get_timesteps(self, file_name):
        """
        Reads the number of timesteps from the imported Dataset
        :param file_name: File name of the Layer Dataset to import
        :return: Number of timesteps (integer)
        """
        file = open(file_name)
        timestep = 0
        for line in iter(file):
            if line.startswith('TS'):
                timestep += 1
        self.timesteps = int(round(timestep / self.datasets))

    def create_list_timesteps(self, file_name):
        """
        Creates a list of the timesteps by reading them from the imported Datset
        :param file_name: File name of the Layer Dataset to import
        :return: List of timesteps in seconds
        """
        file = open(file_name)
        tstep = []
        for line in iter(file):
            if line.startswith('TS'):
                tstep.append(line.split())
        tstep = np.asanyarray(tstep)
        tstep2 = np.delete(tstep, 0, 1)
        tstep3 = np.asanyarray(tstep2).astype(float)
        tstep4 = tstep3[0:self.timesteps:1, 1]
        self.list_timesteps = np.ndarray.tolist(tstep4)

    def create_list_timesteps_columns(self):
        """
        Creates a list of timestep numbers to be used as a column in the final dataframe
        :return: List of timestep numbers for dataframe
        """
        list = []
        count_ts = 1
        while True:
            list1 = [count_ts] * self.nodes
            list.extend(list1)
            count_ts += 1  # Replaces count = count + 1
            if count_ts > self.timesteps:
                break
        self.list_timesteps_columns = list

    def create_list_time_columns(self):
        """
        Creates a list of simulation time (in seconds) to be used as a column in the final dataframe
        :return: List of simulation time (in seconds) for dataframe
        """
        list2 = []
        count_ts1 = 0
        while True:
            list3 = [self.list_timesteps[count_ts1]] * self.nodes
            list2.extend(list3)
            count_ts1 += 1  # Replaces count = count + 1
            if count_ts1 > (self.timesteps - 1):
                break
        self.list_time_columns = list2

    def transform_data(self):
        """
        Transforms the imported data into a dataframe with one column for each dataset (fractions, mean diameter, layer thickness)
        and additional columns for the timestep number and the simulation time
        :return: Dataframe of imported data
        """
        # read total number of lines from the imported dataframe
        lines = self.data_imported.shape[0]
        # calculate the length of one dataset (no. of lines)
        length_datasets = int(round(lines / self.datasets))
        # transform the dataframe to a numpy array
        array_unsorted = self.data_imported.to_numpy()
        # transform the array to an array with one line for each dataset
        array_sorted = array_unsorted.reshape(self.datasets, length_datasets)
        # transpose the array to an array with one column for each dataset
        array_sorted_transposed = np.transpose(array_sorted)
        # create a list of column names
        columns = ["Fraction{0}".format(str(i)) for i in np.arange(1, self.fractions + 1, 1)]
        columns.append("Mean diameter")
        columns.append("Layer thickness")
        # turn the array back to a dataframe with the column names taken from the list created above
        data_in_columns = pd.DataFrame(array_sorted_transposed, columns=columns)
        # turn datatype from object to float, all non-floats will be NaNs
        data_as_float = data_in_columns.apply(pd.to_numeric, errors='coerce')
        # delete rows that have NaN values
        df_data = data_as_float.dropna(axis=0, how='all').reset_index(drop=True)
        # create dataframes for timestep and time in seconds
        df_timesteps = pd.DataFrame(self.list_timesteps_columns, columns=["Timestep"])
        df_time = pd.DataFrame(self.list_time_columns, columns=["Time (seconds)"])
        # merge dataframes to one dataframe
        df_transformed = pd.concat([df_timesteps.reset_index(drop=True), df_time.reset_index(drop=True),
                                    df_data.reset_index(drop=True)], axis=1)
        # transformed dataframe
        self.data_transformed = df_transformed


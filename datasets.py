from config import *


class ReadSedResults:
    def __init__(self, file_name):
        """
        This class provides all the functions to read result files of a Hydro-FT simulation
        and transform them into an array (pandas dataframe).
        The class was written by Max with assistance of Maria for the get_timesteps, create_list_timesteps functions and the function
        to get the files with just the timestep.
        :param file_name: File name of either the dataset of the active layer or under layer to import
        """
        self.nodes = int()
        self.fractions = int()
        self.datasets = int()
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
        self.list_nodes_columns = []
        self.create_list_nodes_columns()
        self.data_transformed = pd.DataFrame
        self.transform_data()
        self.file_justTime(file_name)

    def get_datasets(self):
        """
        Reads the number of datasets in the file (each fraction represents one dataset,
        additionally the mean diameter and layer thickness are written to the result file).
        :return: Number of datasets in the file
        """
        self.datasets = self.fractions + 2

    def get_data(self, file_name):
        """
        Imports the result file and turns it into a pandas dataframe
        :param file_name: File name of either the dataset of the active layer or under layer to import
        :return: Pandas dataframe of the imported dataset
        """
        df_import = pd.read_table(file_name, skiprows=1)
        self.data_imported = df_import.rename(columns={'OBJTYPE "mesh2d"': 'Datasets'})

    def get_timesteps(self, file_name):
        """
        Reads the number of time steps from the imported dataset
        :param file_name: File name of either the dataset of the active layer or under layer to import
        :return: Number of time steps
        """
        file = open(file_name)
        timestep = 0
        for line in iter(file):
            if line.startswith('TS'):
                timestep += 1
        self.timesteps = int(round(timestep / self.datasets))

    def create_list_timesteps(self, file_name):
        """
        Creates a list of the time steps by reading them from the imported dataset
        :param file_name: File name of either the dataset of the active layer or under layer to import
        :return: List of time steps in seconds
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
        Creates a list of time step numbers to be used as a column in the final dataframe
        :return: List of time step numbers for dataframe
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

    def create_list_nodes_columns(self):
        """
        Creates a list of node IDs to be used as a column in the final dataframe
        :return: List of node IDs for dataframe
        """
        list_nodes = list(range(1, self.nodes + 1, 1)) * self.timesteps
        self.list_nodes_columns = list_nodes

    def transform_data(self):
        """
        Transforms the imported data into a dataframe with one column for each dataset (fractions, mean diameter, layer thickness)
        and additional columns for the node ID, timestep number and the simulation time
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
        # create dataframes for node ID, time step and time in seconds
        df_nodeid = pd.DataFrame(self.list_nodes_columns, columns=["Node ID"])
        df_timesteps = pd.DataFrame(self.list_timesteps_columns, columns=["Timestep"])
        df_time = pd.DataFrame(self.list_time_columns, columns=["Time (seconds)"])
        # merge dataframes to one dataframe
        df_transformed = pd.concat([df_timesteps.reset_index(drop=True), df_time.reset_index(drop=True),
                                    df_nodeid.reset_index(drop=True), df_data.reset_index(drop=True)], axis=1)
        # transformed dataframe
        self.data_transformed = df_transformed

    def file_justTime(self, file_name):
        """
        Reads line by line the mesh file and returns the mesh file without the results. The output file gives
        you a quick view of the time step and the simulated time.
        """
        count = 0
        subdat = open("output.txt", "a")
        file = open(file_name, 'r')
        for line in iter(file):
            count += 1
            if line[:1].isalpha():
                subdat.write(line)
        file.close()
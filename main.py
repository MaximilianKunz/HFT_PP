from mesh import *
from calculate_gsd import *
from plotfig import *
from time import perf_counter

# Import number of nodes and fractions from 2dm file
mesh = Read2DM(file2dm)
mesh.get_num_nodes(file2dm)
mesh.get_num_fractions(file2dm)
nodes = mesh.num_nodes
fractions = mesh.num_fractions
dm_fractions = mesh.get_dm_fractions(file2dm)

def create_array(name, file_name):
    """
    This function reads result files of a Hydro-FT simulation and transforms them into an array (Pandas Dataframe).
    :param name: name of the layer to be transformed (e.g. AL for active layer or UL for under layer)
    :param file_name: corresponding file name of the layer
    :return: csv-file including all information written by Hydro-FT in columns (fractions, mean diameter,
    layer thickness) for every node and every time step calculated
    """
    # Import the layer file
    layer = ReadSedResults(file_name)
    layer.get_data(file_name)
    # Use the no. of nodes and fractions previously read from the 2dm-file
    layer.nodes = nodes
    layer.fractions = fractions
    # Calculate the no. of datasets
    layer.get_datasets()
    # Read the time steps from the layer file
    layer.get_timesteps(file_name)
    # Create a list of time steps
    layer.create_list_timesteps(file_name)
    # Create a list of time steps for the columns in the array
    layer.create_list_timesteps_columns()
    # Create a list of simulation time for the columns in the array
    layer.create_list_time_columns()
    # Create a list of node IDs for the columns in the array
    layer.create_list_nodes_columns()
    # Transform the data of the layer file into an array (pandas dataframe)
    layer.transform_data()
    # Export the dataframe as a csv-file
    layer.data_transformed.to_csv('Data_transformed_{}.csv'.format(name), index=False)
    df = layer.data_transformed
    #A = layer.data_transformed.iloc[12, 3:11]
    #B= layer.data_transformed["Node ID"] == 1
    #print(B)
    # Print information
    print("The array of the {0} has been successfully exported as Data_transformed_{0}.csv".format(name))
    print("Number of nodes: {0}".format(layer.nodes))
    print("Number of fractions: {0}".format(layer.fractions))
    print("Number of datasets: {0}".format(layer.datasets))
    print("Number of time steps: {0}".format(layer.timesteps))
    return df

def append_gsd(name, csv_file):
    """
    This function calculates the grain size distribution from the fraction and appends it to the previously built array.
    :param name: name of the layer for which the grain size distribution shall be calculated
    (e.g. AL for active layer or UL for under layer)
    :param csv_file: corresponding previously built csv-file of the layer
    :return: csv-file including the grain size distributions for every node at every time step calculated
    """
    layer = CalculateGSD(csv_file)
    layer.read_csv(csv_file)
    layer.fractions = fractions
    layer.calculate_gsd()
    df1 = layer.data_gsd
    layer.data_gsd.to_csv('Data_GSD_{}.csv'.format(name), index=False)
    print("The grain size distributions of the {0} have been successfully added to the file Data_GSD_{0}.csv".format(name))
    return df1

def slice_array_d50(df,idNode):
    array = df[df["Node ID"] == idNode]
    subarray = array.iloc[:, [1, 11]]
    return subarray

def slice_array_graindist(df1,idNode,timestep):
    array = df1[df1["Node ID"] == idNode]
    subarray = array.iloc[timestep, 13:21]
    return subarray


def log_actions(fun):
    def wrapper(*args, **kwargs):
        start_logging()
        fun(*args, **kwargs)
        logging.shutdown()
    return wrapper


def start_logging():
    logging.basicConfig(filename="logfile.log", format="[%(asctime)s] %(message)s",
                        filemode="w", level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())


@log_actions
def main():
    """
    Create csv-files of the resorted existing result files and additionally calculate grain size distributions for each node
    at every time step
    :return: csv-files files of result data with and without grain size distributions
    """
    # create array for active layer
    df = create_array(name='AL', file_name='Datasets_AL.dat')
    #A=df.iloc[12, 2:10]
    # append grain size distributions to array of active layer
    df1= append_gsd(name='AL', csv_file="Data_transformed_AL.csv")
    # create array for under layer
    create_array(name='UL', file_name='Datasets_UL.dat')
    # append grain size distributions to array of under layer
    append_gsd(name='UL', csv_file="Data_transformed_UL.csv")

    # Export mean diameter at idNode (?)
    C = slice_array_d50(df=df, idNode=1)
    n = plot_d50(C)

    # Export grain distribution at idNode (?) and timestep (?)
    A = slice_array_graindist(df1=df1, idNode=1,timestep=1)
    m = plot_grain (A, dm_fractions)

if __name__ == '__main__':
    # run code and evaluate performance
    t0 = perf_counter()
    main()
    t1 = perf_counter()
    print("Time elapsed: " + str(t1 - t0))

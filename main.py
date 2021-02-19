from import_datasets_class import *
from import_2dm_class import *

# Read no. of nodes and no. of fractions from 2dm files
# sim_data = read2DM()
# sim_data.get_num_nodes() does not work yet
# sim_data.get_num_fractions() does not work yet


def create_array(name, file_name):
    # Import of the Active Layer File
    layer = ReadSedResults(file_name)
    layer.get_data(file_name)

    # Import number of nodes and fractions from 2dm file
    layer.nodes = read2DM.get_num_nodes(file2dm)
    # layer.nodes = 61803
    # layer.fractions = read2DM.num_fractions(file2dm)
    layer.fractions = 8

    # Calculate no. of datasets
    layer.get_datasets()

    # Reading the Timesteps from the Layer File
    layer.get_timesteps(file_name)

    # Creating a list of timesteps
    layer.create_list_timesteps(file_name="Datasets_AL.dat")

    # Creating a list of timesteps for the columns
    layer.create_list_timesteps_columns()

    # Creating a list of simulation time for the columns
    layer.create_list_time_columns()

    # Transform the Data of the Layer File
    layer.transform_data()

    # Export Dataframe as CSV-file
    layer.data_transformed.to_csv('Data_transformed_{}.csv'.format(name), index=False)

    # Print information
    print("The array of the {0} has been successfully exported as Data_transformed_{0}.csv".format(name))
    print("Number of nodes: {0}".format(layer.nodes))
    print("Number of fractions: {0}".format(layer.fractions))
    print("Number of datasets: {0}".format(layer.datasets))
    print("Number of time steps: {0}".format(layer.timesteps))
    # print("This is the exported array:")
    # print(layer.data_transformed)
    # print(layer.data_transformed.dtypes)


def main():
    # create array for active layer
    create_array(name='AL', file_name='Datasets_AL.dat')
    # create array for under layer
    create_array(name='UL', file_name='Datasets_UL.dat')

    # Export grain distribution at node ? and t ?
    # plot_transform = data_transformed[0,3:11]
    # D_char= plot_grain(plot_transform)


if __name__ == '__main__':
    # launch main function
    main()
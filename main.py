from import_datasets_class import *
from mesh import *
from calculate_gsd_class import *
from plotfig import *

def create_array(name, file_name, file2dm):
    # Import of the Active Layer File
    layer = ReadSedResults(file_name)
    layer.get_data(file_name)
    # Import number of nodes and fractions from 2dm file
    layer.nodes = read2DM.get_num_nodes(file2dm)
    # layer.fractions = read2DM.num_fractions(file2dm)
    layer.fractions = 8
    # Calculate no. of datasets
    layer.get_datasets()
    # Reading the Timesteps from the Layer File
    layer.get_timesteps(file_name)
    # Creating a list of timesteps
    layer.create_list_timesteps(file_name)
    # Creating a list of timesteps for the columns
    layer.create_list_timesteps_columns()
    # Creating a list of simulation time for the columns
    layer.create_list_time_columns()
    # Transform the Data of the Layer File
    layer.transform_data()
    # Export Dataframe as CSV-file
    layer.data_transformed.to_csv('Data_transformed_{}.csv'.format(name), index=False)
    # Print information
    print("The array of the {0} has been successfully exported as Data_GSD_{0}.csv".format(name))
    print("Number of nodes: {0}".format(layer.nodes))
    print("Number of fractions: {0}".format(layer.fractions))
    print("Number of datasets: {0}".format(layer.datasets))
    print("Number of time steps: {0}".format(layer.timesteps))


def append_gsd(name, csv_file):
    layer = CalculateGSD(csv_file)
    layer.read_csv(csv_file)
    layer.fractions = 8
    layer.calculate_gsd()
    layer.data_gsd.to_csv('Data_GSD_{}.csv'.format(name), index=False)
    print("The grain size distributions of the {0} have been successfully added to the file Data_GSD_{0}.csv".format(name))


def main():
    # create array for active layer
    create_array(name='AL', file_name='Datasets_AL.dat', file2dm=glob.glob('*.2dm'))
    # append grain size distributions to array of active layer
    append_gsd(name='AL', csv_file="Data_transformed_AL.csv")
    # create array for under layer
    create_array(name='UL', file_name='Datasets_UL.dat', file2dm=glob.glob('*.2dm'))
    # append grain size distributions to array of under layer
    append_gsd(name='UL', csv_file="Data_transformed_UL.csv")

    # Export grain distribution at node ? and t ?
    # plot_transform = data_transformed[0,3:11]
    # D_char= plot_grain(plot_transform)

    # Export grain distribution at node ? and t ?
    #print (data_transformed[0, 1])
    # D_char= plot_grain(plot_transform)
    A = [0.1, 0.2, 0.3, 0.4]
    B = [10, 200, 600, 400]
    m = plot_grain (A, B)

if __name__ == '__main__':
    # launch main function
    main()

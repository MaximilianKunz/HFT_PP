import pandas as pd
import numpy as np

# import the datasets as a pandas dataframe (1 column containing all the datasets)
df_import = pd.read_table("Datasets_Al.dat", skiprows = 1)

# rename the dataframe
df_import = df_import.rename(columns={'OBJTYPE "mesh2d"': 'Datasets_AL'})

# read total number of rows from the dataframe
rows = df_import.shape[0]

# get number of nodes and fractions from Maria's code (read from .2dm file)
nodes = 61803
fractions = 8

# calculate the total number of datasets contained in the dataframe
# there are fractions + 2 datasets, because in addition to all fractions,
# the mean diameter and layer thickness are also given
no_datasets = fractions + 2

# calculate the length of one dataset (no. of lines)
length_datasets = int(round(rows / no_datasets))

# print(df_import.head)

# transform dataframe to array
array_unsorted = df_import.to_numpy()
# print("Unsorted Array:")
# print(array_unsorted)

# transform array to array with one line for each dataset
array_sorted = array_unsorted.reshape(no_datasets, length_datasets)
print("Sorted Array:")
print(array_sorted)

# transpose array to array with one column for each dataset
array_sorted_transposed = np.transpose(array_sorted)
print("Sorted and transposed Array:")
print(array_sorted_transposed)

# create list of column names
columns = ["Fraction{0}".format(str(i)) for i in np.arange(1, fractions + 1, 1)]
columns.append("Mean diameter")
columns.append("Layer thickness")
print("List of column names:")
print(columns)

# turn array back to dataframe
datasets = pd.DataFrame(array_sorted_transposed, columns = columns)
print("Dataframe:")
print(datasets)
print(datasets.dtypes)


# Splitting of dataframe
#count = 1
#while True:
#    df_AL +str(count) = df_AL_1 = df_import.iloc[(count-1)*length_datasets: count*length_datasets]
#	count += 1 # Replaces count = count + 1
#	if count > no_datasets:
#		break

# df_AL_1 = df_import.iloc[:length_datasets]
# df_AL_2 = df_import.iloc[length_datasets : 2*length_datasets]

#print("Shape of new dataframes - {} , {}".format(df_AL_1.shape, df_AL_2.shape))
#print(df_AL_1.head)
#print(df_AL_2.head)
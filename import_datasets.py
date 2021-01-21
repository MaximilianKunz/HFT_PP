import pandas as pd

df_import = pd.read_table("Datasets_Al.dat", skiprows = 1)
df_rename = df_import.rename(columns={'OBJTYPE "mesh2d"': 'Datasets_AL'})
rows = df_rename.shape[0]
nodes = 61803 #should be read from file line 4
fractions = 8 #should be an input
fractions_add = fractions + 2 #because of dm and h layer
length_datasets = rows / fractions_add
#print (length_datasets)
#print (rows)
#print(df_rename.head)

#Splitting of
df_AL_1 = df_rename.iloc[:1977734]
df_AL_2 = df_rename[1977735: 395468]
print("Shape of new dataframes - {} , {}".format(df_AL_1.shape, df_AL_2.shape))
#from config import *
#from import_datasets_class import *

#class subdataset(ReadSedResults)
#    def __ init__(self, data_tran):
#        ReadSedResults.__init__(self)
#        self.slice = pd.DataFrame
#        self.data_transformed = data_transformed
from itertools import islice

def slice (file_name):

    count = 0
    subdat = open("output.txt", "a")
    file = open(file_name, 'r')
    for line in iter(file):
        count += 1
        #if line[:1].isalpha():
            #subdat.write(line)
        if line.startswith('TS'):
            m = file ()
            subdat.write(m)
    file.close()

slice(file_name='Datasets_AL.dat')

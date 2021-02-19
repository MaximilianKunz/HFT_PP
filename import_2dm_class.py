import glob
import numpy as np

file2dm = glob.glob('*.2dm')
file = open(file2dm[0], 'r')
# print(file2dm)

#path = str(path)
#if filehdft.endswith('*AL.dat'):
#    path = extractall (outpatch)
#else:
#    raise ValueError('Unsupported archive provided. Method supports only .zip/.gz files.')
#file2 = open('Datasets_AL.dat')

class read2DM:
    def __init__(self):
        self.get_num_nodes()
#        self.num_nodes = int()
#        self.list_nodes = []
#        self.create_list_nodes()
#        self.num_fractions = int()
        self.num_fractions()

    def get_num_nodes(self):
        nodes = 0
        elements = 0
        nodestrings = 0
        for line in iter(file):
            if line.startswith('ND'):
                nodes += 1
            elif line.startswith('NS'):
                nodestrings += 1
            elif line.startswith('E'):
                elements += 1
        return nodes
#        self.num_nodes = nodes

    def create_list_nodes(self):
        list2 = []
        for line in iter(file):
            if line.startswith('ND'):
                list2.append(line.split())
        list2 = np.asanyarray(list2)
        list3 = np.delete(list2, 0, 1)
        list4 = np.asanyarray(list3).astype(float)
        idnode = list4[:, 0]
        x = list4[:, 1]
        y = list4[:, 2]
        z = list4[:, 3]
        print(list4)

    def num_fractions(self):
        fractions = []
        for line in iter(file):
            if line.startswith('GP_VAL 2 28'):
                fractions.append(line.split())
        fractions = np.asanyarray(fractions)
        print(fractions)
        fractions2 = fractions[0, 3]
        print(fractions2)
        num_fractions = int(fractions2[0])
        return num_fractions

m = read2DM.num_fractions(file2dm)
print(m)


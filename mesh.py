from config import *

class read2DM:
    def __init__(self, file2dm):
        """
        This class reads the mesh files with the extension .2dm and get the most important information necessary to transform the data.
        The class was written by Maria.
        :param file2dm
        """
#       self.readmesh()
        self.get_num_nodes()
#        self.num_nodes = int()
#        self.list_nodes = []
#        self.create_list_nodes()
#        self.num_fractions = int()
        self.num_fractions()
#    def readmesh(self, file2dm):
#        try:
#            file = open(file2dm[0], 'r')
#        except ImportError:
#            print("ERROR: Cannot find 2dm file in the folder")
#        return file

    def get_num_nodes(file2dm):
        nodes = 0
        elements = 0
        nodestrings = 0
        file = open(file2dm[0], 'r')
        for line in iter(file):
            if line.startswith('ND'):
                nodes += 1
            elif line.startswith('NS'):
                nodestrings += 1
            elif line.startswith('E'):
                elements += 1
        return nodes

    def create_list_nodes(file2dm):
        list2 = []
        file = open(file2dm[0], 'r')
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

    def num_fractions(file2dm):
        fractions = []
        file = open(file2dm[0], 'r')
        for line in iter(file):
            if line.startswith('GP_VAL 2 28'):
                fractions.append(line.split())
        print (fractions)
        #list2 = np.asanyarray(fractions)
        #print (list2)
        num_fractions= [i[3] for i in fractions]
        print (num_fractions)
        return int(num_fractions)

m = read2DM.num_fractions(glob.glob('*.2dm'))
print (m)

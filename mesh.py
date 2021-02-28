from config import *


class Read2DM:
    def __init__(self, file2dm):
        """
        This class reads the mesh files with the extension .2dm and get the most important information necessary
        to transform the data.
        The class was written by Maria.
        :param file2dm
        """
        self.num_nodes = int()
        self.get_num_nodes(file2dm)
        self.list_nodes = []
        self.create_list_nodes(file2dm)
        self.num_fractions = int()
        self.get_num_fractions(file2dm)
        self.get_dm_fractions(file2dm)

    def get_num_nodes(self, file2dm):
        nodes = 0
        elements = 0
        nodestrings = 0
        mesh_file = open(file2dm[0], 'r')
        for line in iter(mesh_file):
            if line.startswith('ND'):
                nodes += 1
            elif line.startswith('NS'):
                nodestrings += 1
            elif line.startswith('E'):
                elements += 1
        self.num_nodes = nodes

    def create_list_nodes(self, file2dm):
        list2 = []
        mesh_file = open(file2dm[0], 'r')
        for line in iter(mesh_file):
            if line.startswith('ND'):
                list2.append(line.split())
        list2 = np.asanyarray(list2)
        list3 = np.delete(list2, 0, 1)
        list4 = np.asanyarray(list3).astype(float)
        idnode = list4[:, 0]
        x = list4[:, 1]
        y = list4[:, 2]
        z = list4[:, 3]
        self.list_nodes = list4

    def get_num_fractions(self, file2dm):
        fractions = []
        mesh_file = open(file2dm[0], 'r')
        for line in iter(mesh_file):
            if line.startswith('GP_VAL 2 28'):
                fractions.append(line.split())
        fractions2 = pd.DataFrame(fractions)
        num_fractions = int(fractions2.iloc[0,3])
        self.num_fractions = num_fractions

    def get_dm_fractions(self, file2dm):
        dmfractions = []
        mesh_file = open(file2dm[0], 'r')
        for line in iter(mesh_file):
            if line.startswith('GP_VAL 2 2'):
                dmfractions.append(line.split())
            elif line.startswith('GP_VAL 2 3'):
                dmfractions.append(line.split())
        dm_fractions2 = pd.DataFrame(dmfractions)
        dm_fractions = dm_fractions2.iloc[1:9,3]
        #dm_fractions = dm_fractions2[dm_fractions2[2] > 28]
        #self.dm_fractions = dm_fractions
        #print (dm_fractions)
        return dm_fractions

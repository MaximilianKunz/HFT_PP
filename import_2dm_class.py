import glob
import pandas as pd
import numpy as np
from typing import Dict

# from Project.HFT_PP.import_datasets import nodes

file2dm = glob.glob('*.2dm')
file = open(file2dm[0], 'r')
print(file2dm)

filehdft = glob.glob('*.dat')
print(filehdft)
#path = str(path)
#if filehdft.endswith('*AL.dat'):
#    path = extractall (outpatch)
#else:
#    raise ValueError('Unsupported archive provided. Method supports only .zip/.gz files.')
file2 = open('Datasets_AL.dat')


class read2DM:
    def __init__(self):
        self.num_nodes = int()
        self.get_num_nodes()
#        self.list_nodes = []
#        self.create_list_nodes()
#       self.num_fractions = int()
#        self.get_num_fractions()

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
        self.num_nodes = nodes

#  def create_list_nodes(self):
#        list2 = []
#        for line in iter(file):
#            if line.startswith('ND'):
#                list2.append(line.split())
#        list2 = np.asanyarray(list2)
#        list3 = np.delete(list2, 0, 1)
#        list4 = np.asanyarray(list3).astype(float)
#        idnode = list4[:, 0]
#        x = list4[:, 1]
#        y = list4[:, 2]
#        z = list4[:, 3]
#        print(list4)

#    def get_num_fractions(self):
#        fractions = []
#        for line in iter(file):
#            if line.startswith('GP_VAL 2 28'):
#                fractions.append(line.split())
#        fractions = np.asanyarray(fractions)
#        fractions2 = np.delete (fractions, 0, 1)
#        fractions3 = np.asanyarray(fractions2).astype(float)
#        self.num_fractions = fractions3 [:, 2]
#       print(self.num_fractions)



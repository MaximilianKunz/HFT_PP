import glob
import numpy as np
from typing import Dict

file2dm = glob.glob('*.2dm')
file = open(file2dm[0], 'r')
print(file2dm)

class read2DM:

    def __init__(self):
        self._num_nodes: Dict[str, int] = {}
        self._list_nodes

    def num_nodes(self) -> None:
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
        print(nodes)

    def list_nodes(self):
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

m = read2DM.list_nodes(file2dm)

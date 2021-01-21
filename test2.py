import glob
from typing import Callable, Dict, IO, Iterator, List, Optional

file2dm = glob.glob('*.2dm')
print(file2dm)


def __init__(self) -> None:
        self._open: Optional[IO[str]] = None
		self._stats: Dict[str, int] = {}
        self._nodes: List[Node]

def open(self) -> IO[str]:
    self._file = open(file2dm[0],'r')

def num_nodes(self) -> int:
    if not self._stats:
        self._count()
    return self._stats['num_nodes']


def _count(self) -> None:
   	self._file()
	assert self._file is not None
	self._file.seek(0)
	self._stats = {'num_materials_per_element': -1}
	nodes = 0
	elements = 0
	nodestrings = 0
	for line in iter(self._file):
            if line.startswith('ND'):
               nodes += 1
            elif line.startswith('NS'):
                nodestrings += 1
            elif line.startswith('E'):
                elements += 1
			elif line.startswith('NUM_MATERIALS_PER_ELEM'):
							self._stats['num_materials_per_element'] = int(line.split()[1])
					self._stats.update({'num_nodes': nodes,
										'num_elements': elements,
										'num_nodestrings': nodestrings})

def _filter_lines(self, filter_: Callable[[str], bool]) -> Iterator[str]:
	self._file.seek(0)
    while True:
        line = next_line(self._file)
        if not line:
            break
        if filter_(line):
            yield line

def iter_nodes(self) -> Iterator[Node]:
    last_id = 0
    for line in self._filter_lines(lambda s: s.startswith('ND')):
        node = Node.parse_line(line.split())
        if node.id != last_id + 1:
            if last_id == 0 and node.id == 0:
                warnings.warn(
                    'Node indices are starting at 0 instead of 1')
            else:
                raise FormatError('Node list is not ordered')
        last_id = node.id
        yield node

def nodes(self) -> List[Node]:
    try:
        self._nodes = list(self.iter_nodes())
        return self._nodes
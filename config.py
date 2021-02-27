try:
    import glob
    import logging
except ImportError:
    print("ERROR: Cannot import basic Python libraries.")

try:
    import numpy as np
    import pandas as pd
except ImportError:
    print("ERROR: Cannot import SciPy libraries.")

try:
    file2dm = glob.glob('hydro_as-2d.2dm')
except ImportError:
    print("ERROR: Cannot find 2dm file in the folder")

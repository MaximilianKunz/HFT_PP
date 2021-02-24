try:
    import glob
except ImportError:
    print("ERROR: Cannot import basic Python libraries.")

try:
    import numpy as np
    import pandas as pd
except ImportError:
    print("ERROR: Cannot import SciPy libraries.")
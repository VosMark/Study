"""
A module can be deduced as a library
Each Python file ".py" is treated as a module

import <<filename>> # Import everything from a file
    import os
    import math
import <<filename>> as <<alias>> # Renaming a module
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

from <<filename>> import <<Class, function>> # Import specific items
    from collections import Counter
"""

from functions import my_name
my_name("Marko", 200)
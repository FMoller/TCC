"""
Logical expressions tools module
"""

__version__ = "1.0"
__author__ = "Frederico Moeller"
__copyright__ = "Copyright 2021, Frederico Moeller"
__license__ = "MIT"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyeda.inter import *

def and_splitter(expression):
    splitted = expression.split(sep='*')
    if len(splitted)==1:
        return splitted[0]
    else:
        pivot = And(splitted[0],splitted[1])
        for i in range(2,len(splitted)):
            pivot = And(pivot,splitted[i])
        return pivot

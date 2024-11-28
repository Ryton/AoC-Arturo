# AoC_helper
import os, sys
import numpy as np
import math
#import pandas as pd
import numpy.matlib
import matplotlib.pyplot as plt
import copy
import csv #for load from file
import pandas as pd

class text_functions:

    def __init__(self):
        pass

    def load_to_pandas(self,filename=None,url=None,delimeter=","):
        if filename is not None:
            df = pd.read_csv(filename,header=None) # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
        return df

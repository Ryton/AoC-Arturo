
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

    def load_to_pandas(filename=None,url=None,delimeter=","):
        if filename is not None:
            df = pd.read_csv(filename,header=None) # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
        return df



df =text_functions.load_to_pandas(filename='aoc1.txt', delimeter="")


#list=df.diff()
#print(np.sum(list>0)) #1a

list=df.values

#sum_curr = np.array(int)
sum_curr=np.array([])
for index in range(len(df.values)-2):
    sum_curr = np.append(sum_curr,df.values[index]+df.values[index+1]+df.values[index+2])

list=np.diff(sum_curr)
print(np.sum(list>0)) #1b
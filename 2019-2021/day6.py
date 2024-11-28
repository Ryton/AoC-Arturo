import AoC_helper
import os, sys
import numpy as np
import math
#import pandas as pd
import numpy.matlib
import matplotlib.pyplot as plt
import copy
import csv #for load from file
import pandas as pd

helper =  AoC_helper.text_functions()
df =helper.load_to_pandas(filename='input6.txt', delimeter="")

valuelist = df.values[0] #full

valuelist = [3,4,3,1,2] # demo

fishtypes_days = np.zeros([8,81])
for el in valuelist:
    fishtypes_days[el,0] +=1

print(fishtypes_days[:][0])


def age(fishtypes_days,curr_day):
    currgen=fishtypes_days[:,curr_day]

    for agegroup in range(len(currgen)):

        if agegroup == 0:
            nextgen[6] = currgen[0]
            nextgen[8] = currgen[0]

        elif agegroup ==1:
            nextgen[agegroup-1] = currgen[agegroup]

    return currgen

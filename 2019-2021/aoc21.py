
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


def aoc_day1():
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

    if 1: #b
        horiz = 0
        depth = 0 #down increases.

        print(horiz*depth)
        return

def aoc_day2():
    data = pd.read_csv('input_2.txt', header=None)
    list = data.values
    print('head', list[1:5], '\n tail:', list[-5:-1])
    forward, updown, X = [], [], []
    for i in list:
        if i[0][0] == 'u':
            updown.append(-1)
            forward.append(0)
        elif i[0][0] == 'd':
            updown.append(1)
            forward.append(0)
        elif i[0][0] == 'f':
            updown.append(0)
            forward.append(1)
        X.append(int(i[0][-1]))
    print(len(X), len(forward), len(updown))
    depth, hor, aim = 0, 0, 0
    for index in range(len(forward)):
        if forward[index] == 0:  # up or down.
            # depth += updown[index]*X[index]
            aim += updown[index] * X[index]
        else:  # forward
            hor += abs(X[index])
            depth += aim * abs(X[index])
    print(hor * depth)


    #list=df.diff()
    #print(np.sum(list>0)) #1a

    list=df.values
    #sum_curr = np.array(int)
    sum_curr=np.array([])
    for index in range(len(df.values)-2):
        sum_curr = np.append(sum_curr,df.values[index]+df.values[index+1]+df.values[index+2])

    list=np.diff(sum_curr)
    print(np.sum(list>0)) #1b

    def aoc_day2():
        horiz = 0
        depth = 0 #down increases.

        print(horiz*depth)
        return

def aoc_day3():
    df = text_functions.load_to_pandas(filename='input.txt', delimeter="")
    list = df.values

    list_12bits =

    count = 0
    gamma, epsilon = '',''
    count_tot = 1000

    for pos in range(11,-1,-1):
        running_sum = 0
        for item in range(len(list)):
            numstring = str(list[item][0])
            if pos < len(numstring):
                running_sum +=int(numstring[pos])

        if running_sum>500:
            gamma +='1'
            epsilon +='0'
        else:
            gamma += '0'
            epsilon += '1'

        epsilon = epsilon[::-1]
        gamma = gamma[::-1]
    print(int(gamma,2)* int(epsilon,2))
#3991104

aoc_day3()
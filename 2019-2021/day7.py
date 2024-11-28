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

import input_scrub
input_scrub.parse_from_URL()
helper =  AoC_helper.text_functions()
sys.run('input_parser.py --day 5 >5.txt')

df =helper.load_to_pandas(filename='5.txt', delimeter="")

valuelist = df.values[0] #full
print(valuelist)
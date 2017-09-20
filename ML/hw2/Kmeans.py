import pandas as pd
import math
from collections import defaultdict
data = []
file_name = "clusters.txt"
mode = "r"
input_file = open(file_name,mode)
for line in input_file.readlines():
    data.append(tuple(map(float,line.strip().split(","))))

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:39:46 2018

@author: pengu
"""
import pandas as pd
import numpy as np
import math

def confidence(ld):
    x=0
    r=0
    while r<0.995:
        r += (math.exp(-ld))*(ld**x)/(math.factorial(x))
        x += 1
    return x

#read lambda values from file
filename= r'D:\Cornell\Baseline_lambda_threshold.xlsx'
df = pd.read_excel(filename)
lambda_values = df.values

conf = np.copy(lambda_values)

for i in range(30):
    for k in range(30):
        if lambda_values[i][k] == 0:
            pass
        else:
            conf[i][k] = confidence(lambda_values[i][k])
        
df = pd.DataFrame(conf)
df.to_csv("D:/Cornell/confidence.csv")

df = pd.read_csv("D:/Cornell/confidence.csv", index_col = 0)
df1 = df.values
print(df1)
sum = 0
for i in range(30):
    for k in range(30):
        sum += df1[i][k]
print(sum)
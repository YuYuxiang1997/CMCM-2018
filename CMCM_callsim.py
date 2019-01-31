# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 13:24:27 2018

@author: pengu
"""
import random
import math
import time
import numpy as np
import pandas as pd

filename= r'D:\Cornell\Baseline_lambda_calls.xlsx'
df = pd.read_excel(filename)
lambda_values = df.values
for i in range(30):
    for j in range(30):
        lambda_values[i][j] = lambda_values[i][j]/(24)

random.seed(time.time())

def poisson(x):
    k = (math.exp(-x))*x*10000000
    r = random.randint(1,10000000)
    if r < k:
        return True
    else:
        return False
    
callsim=np.zeros((30,30))

for day in range(365):
    print(day)
    for i in range(24):
        for j in range(30):
            for k in range(30):
                if poisson(lambda_values[j][k]):
                    callsim[j][k] +=1
                
print(callsim)
sum = 0
for i in range(30):
    for j in range(30):
        sum += callsim[i][j]
print(sum)

df = pd.DataFrame(callsim)
df.to_csv("D:/Cornell/callsim_Weekend.csv")
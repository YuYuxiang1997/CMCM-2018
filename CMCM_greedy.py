from CMCM_readamb import amb_array
import pandas as pd
import numpy as np

#threshold of greedy algo
threshold = 1350
amb_list = []

#read lambda values from file
df = pd.read_csv("D:/Cornell/confidence.csv", index_col = 0)
lambda_values = df.values

#sums lambda values
def sum_lambda(x):
    sum = 0
    for i in range(30):
        for j in range(30):
            sum += x[i][j]
    return sum

#safetly mechanism to prevent infinite loop
safety = sum_lambda(lambda_values)

'''
costfunc
'''
cf = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1}
'''
penalise for repeating
'''
repeats = np.zeros((30,30))


while sum_lambda(lambda_values) > threshold:
    results = []
    
    #iterate across all ambulances
    for amb in range(len(amb_array)):
        temp = np.copy(lambda_values)
        redux = 0
        for i in range(30):
            for j in range(30):
                if temp[i][j] > 0 and amb_array[amb].targets[i][j] > 0:
                    if repeats[i][j] == 0:
                        redux += cf[int(temp[i][j])]
                    else:
                        pass
                        #redux += 0.01
                        #redux += (cf[int(temp[i][j])]/((repeats[i][j]+1)**3))
        results.append(redux)
        
    
    #best placement is ambulance that minimizes resulting sum
    winner = results.index(max(results))
    amb_list.append(amb_array[winner])
    for i in range(30):
        for j in range(30):
            if (lambda_values[i][j] > 0):
                lambda_values[i][j] -= amb_array[winner].targets[i][j]
            if (amb_array[winner].targets[i][j] > 0):
                repeats[i][j] +=1
    if sum_lambda(lambda_values) == safety:
        break
    safety = sum_lambda(lambda_values)
residue = lambda_values
for i in range(len(amb_list)):
    print(amb_list[i].ID)
print(len(amb_list))
#print(sum_lambda(lambda_values))
#print(amb_list[4].home)
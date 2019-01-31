import random
import math
import time
import numpy as np
import pandas as pd
import CMCM_dijkstra

#import ambulance arrays
from CMCM_greedy import amb_list

#read lambda values from file
filename= r'D:\Cornell\Weekend_lambda_calls.xlsx'
df = pd.read_excel(filename)
lambda_values = df.values

#Set random seed based on os.time
random.seed(time.time())


class ambu:
    def __init__(self,ID,home):
        self.ID = ID
        self.home = home


#get additional time for moving across small squares
add_dict = [[0,20,20,0,0,0],
            [15,15,40,40,40,40],
            [15,15,40,40,40,40],
            [15,15,40,40,40,40],
            [15,20,25,25,25,25],
            [15,15,0,0,0,0]]
def add_time(x,y):
    if x[0]-y[0] > 0:
        diffx = x[0]-y[0]
    else:
        diffx = y[0]-x[0]
    if x[1]-y[1] > 0:
        diffy = x[1]-y[1]
    else:
        diffy = y[1]-x[1]
    if (diffx,diffy) == (1,1) or (diffx,diffy) == (1,0) or (diffx,diffy) == (0,1):
        diff = 1
    else:
        diff = 2
    return add_dict[(y[0])//5][(y[1])//5]*diff

def get_ambu_from_ID(ambu_l,ID):
    for i in range(len(ambu_l)):
        if ambu_l[i].ID == ID:
            return ambu_l[i]
#Poisson function: Input lambda value
#returns true if RNG rolls 1, false if RNG rolls 0
def poisson(x):
    k = (math.exp(-x))*x*10000000
    r = random.randint(1,10000000)
    if r < k:
        return True
    else:
        return False

array = np.zeros((30,30,40))
ambu_l = []
for amb in range(len(amb_list)):
    ambu_l.append(ambu(amb+1,amb_list[amb].home))
    for i in range(30):
        for j in range(30):
            if amb_list[amb].targets[i][j] != 0:
                k = 0 
                while array[i][j][k] != 0:
                    k += 1
                array[i][j][k]=amb+1

total = 0

ambulance = np.zeros(60)
'''
Simulation
'''
failure_grid = np.zeros((30,30))
sum_failures = 0
time_array = []

for i in range(500*4):
    temp = np.zeros((30,30))
    for amb in range(len(amb_list)):
        if ambulance[amb] < i:
            ambulance[amb] = i
    for j in range(array.shape[0]):
        for k in range(array.shape[1]):
            if poisson(lambda_values[j][k]/(24)):
                response = False
                node = CMCM_dijkstra.get_node((j+5)//5,(k+5)//5)
                
                for amb in range(array.shape[2]):
                    res_amb = int(array[j][k][amb])
                    if res_amb != 0:
                        if (ambulance[res_amb-1] == i):
                            response = True
                            ambulance[res_amb-1] += 1
                            res_amb_obj = get_ambu_from_ID(ambu_l,res_amb)
                            amb_home_node = CMCM_dijkstra.get_node(res_amb_obj.home[0],res_amb_obj.home[1])
                            time = CMCM_dijkstra.dijsktra(CMCM_dijkstra.graph, node, amb_home_node)
                            time = time+add_time((j,k),amb_home_node.coord)
                            time = min(240,time)
                            time_array.append(time)
                            #print("Session:" +str(i//4) + " days " + str(i%4) + " hrs")
                            #print("Call at location(" + str(j) + "," + str(k) + "), Ambulance " + str(res_amb) + " sent in time:" + str(time))
                            break
                
                if response == False:
                    #print("Session:" +str(i//4) + " days " + str(i%4) + " hrs")
                    #print("Call at location(" + str(j) + "," + str(k) + "), Ambulance busy") 
                    dist_from_amb = {}
                    failure_grid[j][k] +=1
                    for amb in range(len(ambulance)):
                        if ambulance[amb] == i:
                            amb_obj = get_ambu_from_ID(ambu_l,amb+1)
                            amb_home_node = CMCM_dijkstra.get_node(amb_obj.home[0],amb_obj.home[1])
                            time = CMCM_dijkstra.dijsktra(CMCM_dijkstra.graph, node, amb_home_node)
                            time = time+add_time((j,k),amb_home_node.coord)
                            dist_from_amb.update({amb+1:time})
                    a_min = min(dist_from_amb.values())
                    time_array.append(a_min)
                    amb_min = 0
                    for ambs in dist_from_amb:
                        if dist_from_amb[ambs] == a_min:
                            amb_min = ambs
                            break
                    ambulance[amb_min-1]+=1
                    a_min = max(280,a_min)
                    #print("Ambulace " + str(amb_min) + " sent in time: " + str(a_min))
                    sum_failures +=1

sum_time=0
for i in range(len(time_array)):
    sum_time += time_array[i]
print("Average time: " + str(sum_time/len(time_array)))
print(sum_failures)

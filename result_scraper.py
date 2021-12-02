# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:29:33 2021

@author: aaron
"""


# Python program to read stored job results and plot the output probabilities
import numpy as np
import json
import matplotlib.pyplot as plt

 
nbits = 5 #state the number of qubits in the simulation
# Opening JSON file
f = open(r'put json file path here')
 

data = json.load(f)
x= data['results'][0]['data']['counts']
N = data['results'][0]['shots']
keys = data['results'][0]['data']['counts'].keys()

print(x)
f.close()


problist = np.array([x[p]/N for p in x]) #this is a list of probabillites of measuring a certain state
states = [bin(int(hexs, 16))[2:].zfill(nbits) for hexs in keys] #extracting states from hex form given in the results
plt.bar(states, problist, color='g')   #bar chart of the results
plt.show()
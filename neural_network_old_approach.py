import json
import sys
import operator
import numpy as np
import time

start_time = time.time()
file = 'BCR_strings_length_8_occ50000_patient_cluster_percents'
data = json.load(open(file + '.json'))

original_data = json.load(open('bcr_project_data.json'))
sys.stderr.write(str(time.time()-start_time)+'seconds to load data \n')

output_matrix = []
cancer_map = {}
cancer_map['SKCM'] = 0
cancer_map['LUSC'] = 0.0833333
cancer_map['READ'] = 0.1666666
cancer_map['STAD'] = 0.25
cancer_map['BRCA'] = 0.3333333
cancer_map['BLCA'] = 0.4166666
cancer_map['KIRC'] = 0.5
cancer_map['HNSC'] = 0.5833333
cancer_map['PRAD'] = 0.6666666
cancer_map['LUAD'] = 0.75
cancer_map['COAD'] = 0.8333333
cancer_map['THCA'] = 0.9166666
cancer_map['OV'] = 1
for patient_BCR_record in original_data:
    output_matrix.append(cancer_map[patient_BCR_record['cancer']])


output_matrix = output_matrix[0:100]
input_matrix = []

for obj in data["data"]:
    cluster10 = obj["cluster3"]
    input_array = np.zeros(3,)
    for cluster_label in cluster10:
        if(cluster_label!=-1):
            input_array[int(cluster_label)] = obj["cluster3"][cluster_label]
    input_matrix.append(input_array)

input_matrix = input_matrix[0:100]

start_time2 = time.time()
# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input dataset
X = np.array(input_matrix)
    
# output dataset            
y = np.array([output_matrix]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1

for iter in range(15000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)


labels = [0, 
          0.0833333, 
          0.1666666, 
          0.25,
          0.3333333, 
          0.4166666,
          0.5, 
          0.5833333, 
          0.6666666, 
          0.75, 
          0.8333333, 
          0.9166666, 
          1]


predictions = []
for targetVal in l1:
    diff = 100
    cand = 0
    for label in labels:
        if abs(label - targetVal) < diff:
            diff = abs(label - targetVal)
            cand = label    
    predictions.append(cand)

correctly_picked = 0
for x in range(len(predictions)):
    if predictions[x] == output_matrix[x]:
        correctly_picked = correctly_picked + 1


print ("Output After Training:")
print (predictions)
print(correctly_picked)

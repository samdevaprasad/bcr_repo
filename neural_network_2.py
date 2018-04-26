import json
import sys
import operator
import numpy as np
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

import matplotlib.pyplot as plt

start_time = time.time()
file = 'BCR_strings_length_5_occ5000_patient_cluster_percents'
data = json.load(open(file + '.json'))

original_data = json.load(open('bcr_project_data.json'))
sys.stderr.write(str(time.time()-start_time)+'seconds to load data \n')

output_matrix = []
cancer_map = {}
cancer_map['SKCM'] = 0
cancer_map['LUSC'] = 1
cancer_map['READ'] = 2
cancer_map['STAD'] = 3
cancer_map['BRCA'] = 4
cancer_map['BLCA'] = 5
cancer_map['KIRC'] = 6
cancer_map['HNSC'] = 7
cancer_map['PRAD'] = 8
cancer_map['LUAD'] = 9
cancer_map['COAD'] = 10
cancer_map['THCA'] = 11
cancer_map['OV'] = 12
for patient_BCR_record in original_data:
    output_array = np.zeros(13,)
    output_array[cancer_map[patient_BCR_record['cancer']]] =1
    output_matrix.append(output_array)


output_matrix = output_matrix

input_matrix = []

cluster_size = 50
cluster_string = "ward_clustering_" + str(cluster_size)
i=0
for obj in data["data"]:
    cluster_results = obj[cluster_string]
    if(len(obj[cluster_string])>0):
        if i == 0:
            print(obj[cluster_string])
            print(len(obj[cluster_string]))
        input_array = np.zeros(cluster_size,)
        for cluster_label in cluster_results:
            if(cluster_label != '-1' and cluster_label!=-1):
                input_array[int(cluster_label)] = obj[cluster_string][cluster_label]
        input_matrix.append(input_array)
        i = 1
if len(input_matrix) > 0:
    input_matrix = input_matrix
    print(input_matrix[0:2])

    X_train, X_test, y_train, y_test = train_test_split(input_matrix, output_matrix, test_size=0.2, random_state=23)


    X_train = np.array(X_train)
    y_train = np.array(y_train)

    model = Sequential()
    model.add(Dense(100, input_dim=cluster_size, activation="relu"))
    model.add(Dense(13, activation="softmax"))
    print("Dense add 1")
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    print("Compile finished")

    history = model.fit(X_train, y_train, epochs=200, batch_size=32)
    print("model fit")
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig('loss1.png')

    X_test = np.array(X_test)
    y_test = np.array(y_test)
    scores = model.evaluate(X_test, y_test)

    print("\nAccuracy: %.2f%%" % (scores[1]*100))
elif len(input_matrix) == 0:
    print("No data for cluster approach")

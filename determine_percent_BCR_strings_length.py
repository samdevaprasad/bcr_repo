import json
import sys
import operator
import numpy as np
import sklearn.cluster 
import distance
import time
from pprint import pprint
import pandas as pd

start_time = time.time()

file = 'BCR_strings_length_5_occ5000'
length_of_string = 5
string_data_list = json.load(open( file + '.json'))
cluster_data = json.load(open(file + '_clusters.json'))

string_data_dict = { "cluster3" : {}, 
			     	 "cluster10" : {}, 
					 "cluster50" : {}, 
					 "cluster100" : {}, 
					 "clusters1000" : {},
					 "spectralclustering" : {},
					 "ward_clustering" : {},
					 "birch_clustering" : {},
					 "spectralclustering_10" : {},
					 "ward_clustering_10" : {},
					 "birch_clustering_10" : {},
					 "spectralclustering_50" : {},
					 "ward_clustering_50" : {},
					 "birch_clustering_50" : {}, 
                    }

for i in xrange(0, len(string_data_list)):
	cluster_types = string_data_dict.keys()
	for cluster_type in cluster_types:
		if cluster_type in cluster_data:
			string_data_dict[cluster_type][string_data_list[i]] = cluster_data[cluster_type][i]

#load the BCR raw data
data = json.load(open('bcr_project_data.json'))
sys.stderr.write(str(time.time()-start_time)+'seconds to do json load \n');


i=0
patients_cluster_data = []

start_time2 = time.time();
for patient_record in data:
	i += 1
	sys.stderr.write(str(i) + '\n')
	patient_BCR_list = patient_record['BCR']
	string_total_count = 0
	patient_cluster_info = { "cluster3" : {}, 
							 "cluster10" : {}, 
							 "cluster50" : {}, 
							 "cluster100" : {}, 
							 "clusters1000" : {},
							 "spectralclustering" : {},
							 "ward_clustering" : {},
							 "birch_clustering" : {},
							 "spectralclustering_10" : {},
							 "ward_clustering_10" : {},
							 "birch_clustering_10" : {},
							 "spectralclustering_50" : {},
							 "ward_clustering_50" : {},
							 "birch_clustering_50" : {}, 
                        }
	for x in xrange(0, len(patient_BCR_list)):
		#sub string of length six analysis
		single_BCR_data_pt = patient_BCR_list[x][0]
	
		if not pd.isnull(single_BCR_data_pt) and len(single_BCR_data_pt) >= length_of_string:
			for x in xrange(0,len(single_BCR_data_pt)-length_of_string + 1):
				sub_string = single_BCR_data_pt[x:x+length_of_string]
				string_total_count += 1
				cluster_types = string_data_dict.keys()
				for cluster_type in cluster_types:
					if cluster_type in cluster_data:
						if sub_string not in string_data_dict[cluster_type]:
							if -1 not in patient_cluster_info[cluster_type]:
								patient_cluster_info[cluster_type][-1] = 1
							else:
								patient_cluster_info[cluster_type][-1] += 1
						elif sub_string in string_data_dict[cluster_type]:
							cluster_label = string_data_dict[cluster_type][sub_string]
							if cluster_label not in patient_cluster_info[cluster_type]:
								patient_cluster_info[cluster_type][cluster_label] = 1
							else:
								patient_cluster_info[cluster_type][cluster_label] += 1
	for cluster_type in cluster_types:
		if cluster_type in cluster_data:
			patient_cluster_info[cluster_type].update((x, y*100/float(string_total_count)) for x, y in patient_cluster_info[cluster_type].items())
	patients_cluster_data.append(patient_cluster_info)


		 		
sys.stderr.write(str(time.time()-start_time2)+'seconds to loop \n')


start_time3 = time.time()
orig_stdout = sys.stdout
f = open(file + '_patient_cluster_percents.json', 'w')
sys.stdout = f
print json.dumps({ "data" : patients_cluster_data})
sys.stdout = orig_stdout
f.close()

sys.stderr.write(str(time.time()-start_time3)+'seconds to json dump \n')

# pprint(len(string_data))
# pprint(len(cluster_data["cluster3"]))
# pprint(len(cluster_data["cluster10"]))
# pprint(len(cluster_data["spectralclustering"]))
# pprint(len(cluster_data["ward_clustering"]))
# pprint(len(cluster_data["birch_clustering"]))
# pprint(len(cluster_data["spectralclustering_10"]))
# pprint(len(cluster_data["ward_clustering_10"]))
# pprint(len(cluster_data["birch_clustering_10"]))
# pprint(len(cluster_data["spectralclustering_50"]))
# pprint(len(cluster_data["ward_clustering_50"]))
# pprint(len(cluster_data["birch_clustering_50"]))
# sys.stderr.write(str(time.time()-start_time)+'seconds to load data \n')



sys.stderr.write(str(time.time()-start_time)+'seconds to complete \n')
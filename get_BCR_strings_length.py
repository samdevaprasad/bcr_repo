import json
import sys
import operator
import numpy as np
import pandas as pd
import time
from pprint import pprint

#load the BCR raw data
start_time = time.time();
data = json.load(open('bcr_project_data.json'))
sys.stderr.write(str(time.time()-start_time)+'seconds to do json load \n');


#create a list of all unique strings of length 6
# patient_BCR_dict = {};
# i=0

# start_time2 = time.time();
# for patient_BCR_record in data:
# 	i += 1
# 	sys.stderr.write(str(i) + '\n')
# 	patient_BCR_list = patient_BCR_record['BCR']
# 	for x in xrange(0, len(patient_BCR_list)):
# 		#sub string of length six analysis
# 		single_BCR_data_pt = patient_BCR_list[x][0]
	
# 		if not pd.isnull(single_BCR_data_pt) and len(single_BCR_data_pt) >= 8:
# 			for x in xrange(0,len(single_BCR_data_pt)-7):
# 				sub_string = single_BCR_data_pt[x:x+8]
# 				if sub_string not in patient_BCR_dict:
# 		 			patient_BCR_dict[sub_string] = 1
# 		 		elif sub_string in patient_BCR_dict:
# 	 				patient_BCR_dict[sub_string] += 1

# sys.stderr.write(str(time.time()-start_time2)+'seconds to loop \n')

# #write the data to a json file
# start_time3 = time.time()
# i=0
# patient_BCR_final_100 = {};
# patient_BCR_final_500 = {};
# patient_BCR_final_1000 = {};
# patient_BCR_final_5000 = {};
# patient_BCR_final_10000 = {};
# patient_BCR_final_50000 = {};
# for key, value in patient_BCR_dict.items():
# 	if value > 100:
# 		patient_BCR_final_100[key] = key
# 	if value > 500:
# 		patient_BCR_final_500[key] = key
# 	if value > 1000:
# 		patient_BCR_final_1000[key] = key
# 	if value > 5000:
# 		patient_BCR_final_5000[key] = key
# 	if value > 10000:
# 		patient_BCR_final_10000[key] = key
# 	if value > 50000:
# 		patient_BCR_final_50000[key] = key

# orig_stdout = sys.stdout
# f = open('BCR_strings_length_8_occ100.json', 'w')
# sys.stdout = f
# print json.dumps(patient_BCR_final_100.keys())
# sys.stdout = orig_stdout
# f.close()

# orig_stdout = sys.stdout
# f = open('BCR_strings_length_8_occ500.json', 'w')
# sys.stdout = f
# print json.dumps(patient_BCR_final_500.keys())
# sys.stdout = orig_stdout
# f.close()

# orig_stdout = sys.stdout
# f = open('BCR_strings_length_8_occ1000.json', 'w')
# sys.stdout = f
# print json.dumps(patient_BCR_final_1000.keys())
# sys.stdout = orig_stdout
# f.close()

# orig_stdout = sys.stdout
# f = open('BCR_strings_length_8_occ5000.json', 'w')
# sys.stdout = f
# print json.dumps(patient_BCR_final_5000.keys())
# sys.stdout = orig_stdout
# f.close()

# orig_stdout = sys.stdout
# f = open('BCR_strings_length_8_occ10000.json', 'w')
# sys.stdout = f
# print json.dumps(patient_BCR_final_10000.keys())
# sys.stdout = orig_stdout
# f.close()

# orig_stdout = sys.stdout
# f = open('BCR_strings_length_8_occ50000.json', 'w')
# sys.stdout = f
# print json.dumps(patient_BCR_final_50000.keys())
# sys.stdout = orig_stdout
# f.close()

# sys.stderr.write(str(time.time()-start_time3)+'seconds to json dump \n');

# sys.stderr.write(str(time.time()-start_time)+'seconds to complete \n');
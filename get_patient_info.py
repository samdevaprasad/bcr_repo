import json
import sys
import operator
import numpy as np
import time

start_time = time.time()
data = json.load(open('bcr_project_data.json'))
sys.stderr.write(str(time.time()-start_time)+'seconds to load data \n')

patient_info_list = []

for patient_BCR_record in data:
	patient_info = {"living" : "",
				"cancer_type": "",
				"days_survived": -1,
				"age": -1}
	patient_info["living"] = patient_BCR_record["EVENT"]
	patient_info["cancer_type"] = patient_BCR_record["cancer"]
	patient_info["days_survived"] = patient_BCR_record["OS"]
	patient_info["age"] = patient_BCR_record["age"]
	patient_info_list.append(patient_info)

start_time3 = time.time()
orig_stdout = sys.stdout
f = open('patient_info.json', 'w')
sys.stdout = f
print json.dumps({ "data" : patient_info_list })
sys.stdout = orig_stdout
f.close()

sys.stderr.write(str(time.time()-start_time3)+'seconds to json dump \n')
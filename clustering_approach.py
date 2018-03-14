import json
from pprint import pprint
data = json.load(open('bcr_project_data.json'))


patient_BCR_dict = {};
patient_BCR_list = data[0]['BCR'];

for x in xrange(0, len(patient_BCR_list)):
	single_BCR_data_pt = patient_BCR_list[x][0];
	if single_BCR_data_pt not in patient_BCR_dict:
		patient_BCR_dict[single_BCR_data_pt] = 1;
	elif single_BCR_data_pt in patient_BCR_dict:
		patient_BCR_dict[single_BCR_data_pt] += 1;

pprint(len(patient_BCR_dict))
#pprint(data[0]['BCR'][4][0])
#4240 entries
#73 BCR rows for data[0]
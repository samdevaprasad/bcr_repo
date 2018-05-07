import json
import sys
import operator
import numpy as np
import time
import matplotlib.pyplot as plt

start_time = time.time()
data = json.load(open('patient_info.json'))
sys.stderr.write(str(time.time()-start_time)+'seconds to load data \n')

alive_patients = 0
alive_patients_with_age = 0
dead_patients = 0

data = data["data"]
dead_patients_age_list = []
dead_pateints_survival_days_list = []
alive_patients_age_list = []
alive_patients_survival_days_list = []

cancer_type_skcm_patients = 0
cancer_type_lusc_patients = 0
cancer_type_read_patients = 0
cancer_type_stad_patients = 0
cancer_type_brca_patients = 0
cancer_type_blca_patients = 0
cancer_type_kirc_patients = 0
cancer_type_hnsc_patients = 0
cancer_type_prad_patients = 0
cancer_type_luad_patients = 0
cancer_type_coad_patients = 0
cancer_type_thca_patients = 0
cancer_type_ov_patients = 0

cancer_type_skcm_list = []
cancer_type_lusc_list = []
cancer_type_read_list = []
cancer_type_stad_list = []
cancer_type_brca_list = []
cancer_type_blca_list = []
cancer_type_kirc_list = []
cancer_type_hnsc_list = []
cancer_type_prad_list = []
cancer_type_luad_list = []
cancer_type_coad_list = []
cancer_type_thca_list = []
cancer_type_ov_list = []

cancer_type_skcm_dead_patients = 0
cancer_type_lusc_dead_patients = 0
cancer_type_read_dead_patients = 0
cancer_type_stad_dead_patients = 0
cancer_type_brca_dead_patients = 0
cancer_type_blca_dead_patients = 0
cancer_type_kirc_dead_patients = 0
cancer_type_hnsc_dead_patients = 0
cancer_type_prad_dead_patients = 0
cancer_type_luad_dead_patients = 0
cancer_type_coad_dead_patients = 0
cancer_type_thca_dead_patients = 0
cancer_type_ov_dead_patients = 0

cancer_type_skcm_dead_list = []
cancer_type_lusc_dead_list = []
cancer_type_read_dead_list = []
cancer_type_stad_dead_list = []
cancer_type_brca_dead_list = []
cancer_type_blca_dead_list = []
cancer_type_kirc_dead_list = []
cancer_type_hnsc_dead_list = []
cancer_type_prad_dead_list = []
cancer_type_luad_dead_list = []
cancer_type_coad_dead_list = []
cancer_type_thca_dead_list = []
cancer_type_ov_dead_list = []

cancer_type_skcm_alive_patients = 0
cancer_type_lusc_alive_patients = 0
cancer_type_read_alive_patients = 0
cancer_type_stad_alive_patients = 0
cancer_type_brca_alive_patients = 0
cancer_type_blca_alive_patients = 0
cancer_type_kirc_alive_patients = 0
cancer_type_hnsc_alive_patients = 0
cancer_type_prad_alive_patients = 0
cancer_type_luad_alive_patients = 0
cancer_type_coad_alive_patients = 0
cancer_type_thca_alive_patients = 0
cancer_type_ov_alive_patients = 0

cancer_type_skcm_alive_list = []
cancer_type_lusc_alive_list = []
cancer_type_read_alive_list = []
cancer_type_stad_alive_list = []
cancer_type_brca_alive_list = []
cancer_type_blca_alive_list = []
cancer_type_kirc_alive_list = []
cancer_type_hnsc_alive_list = []
cancer_type_prad_alive_list = []
cancer_type_luad_alive_list = []
cancer_type_coad_alive_list = []
cancer_type_thca_alive_list = []
cancer_type_ov_alive_list = []

patient_data_info = []
for patient_data in data:
	if not np.isnan(patient_data["age"]) and not np.isnan(patient_data["days_survived"]):
		patient_data_info.append(patient_data)

for patient_data in patient_data_info:
	if patient_data["living"] == "living":
		alive_patients = alive_patients + 1
		alive_patients_age_list.append(patient_data["age"])
		alive_patients_survival_days_list.append(patient_data["days_survived"])
		if patient_data["cancer_type"] == "SKCM":
			cancer_type_skcm_alive_list.append(patient_data["age"])
			cancer_type_skcm_alive_patients = cancer_type_skcm_alive_patients + 1
		elif patient_data["cancer_type"] == "LUSC":
			cancer_type_lusc_alive_list.append(patient_data["age"])
			cancer_type_lusc_alive_patients = cancer_type_lusc_alive_patients + 1
		elif patient_data["cancer_type"] == "READ":
			cancer_type_read_alive_list.append(patient_data["age"])
			cancer_type_read_alive_patients = cancer_type_read_alive_patients + 1
		elif patient_data["cancer_type"] == "STAD":
			cancer_type_stad_alive_list.append(patient_data["age"])
			cancer_type_stad_alive_patients = cancer_type_stad_alive_patients + 1
		elif patient_data["cancer_type"] == "BRCA":
			cancer_type_brca_alive_list.append(patient_data["age"])
			cancer_type_brca_alive_patients = cancer_type_brca_alive_patients + 1
		elif patient_data["cancer_type"] == "BLCA":
			cancer_type_blca_alive_list.append(patient_data["age"])
			cancer_type_blca_alive_patients = cancer_type_blca_alive_patients + 1
		elif patient_data["cancer_type"] == "KIRC":
			cancer_type_kirc_alive_list.append(patient_data["age"])
			cancer_type_kirc_alive_patients = cancer_type_kirc_alive_patients + 1
		elif patient_data["cancer_type"] == "HNSC":
			cancer_type_hnsc_alive_list.append(patient_data["age"])
			cancer_type_hnsc_alive_patients = cancer_type_hnsc_alive_patients + 1
		elif patient_data["cancer_type"] == "PRAD":
			cancer_type_prad_alive_list.append(patient_data["age"])
			cancer_type_prad_alive_patients = cancer_type_prad_alive_patients + 1
		elif patient_data["cancer_type"] == "LUAD":
			cancer_type_luad_alive_list.append(patient_data["age"])
			cancer_type_luad_alive_patients = cancer_type_luad_alive_patients + 1
		elif patient_data["cancer_type"] == "COAD":
			cancer_type_coad_alive_list.append(patient_data["age"])
			cancer_type_coad_alive_patients = cancer_type_coad_alive_patients + 1
		elif patient_data["cancer_type"] == "THCA":
			cancer_type_thca_alive_list.append(patient_data["age"])
			cancer_type_thca_alive_patients = cancer_type_thca_alive_patients + 1
		elif patient_data["cancer_type"] == "OV":
			cancer_type_ov_alive_list.append(patient_data["age"])
			cancer_type_ov_alive_patients = cancer_type_ov_alive_patients + 1
	elif patient_data["living"] == "death":
		dead_patients = dead_patients + 1
		dead_patients_age_list.append(patient_data["age"])
		dead_pateints_survival_days_list.append(patient_data["days_survived"])
		if patient_data["cancer_type"] == "SKCM":
			cancer_type_skcm_dead_list.append(patient_data["age"])
			cancer_type_skcm_dead_patients = cancer_type_skcm_dead_patients + 1
		elif patient_data["cancer_type"] == "LUSC":
			cancer_type_lusc_dead_list.append(patient_data["age"])
			cancer_type_lusc_dead_patients = cancer_type_lusc_dead_patients + 1
		elif patient_data["cancer_type"] == "READ":
			cancer_type_read_dead_list.append(patient_data["age"])
			cancer_type_read_dead_patients = cancer_type_read_dead_patients + 1
		elif patient_data["cancer_type"] == "STAD":
			cancer_type_stad_dead_list.append(patient_data["age"])
			cancer_type_stad_dead_patients = cancer_type_stad_dead_patients + 1
		elif patient_data["cancer_type"] == "BRCA":
			cancer_type_brca_dead_list.append(patient_data["age"])
			cancer_type_brca_dead_patients = cancer_type_brca_dead_patients + 1
		elif patient_data["cancer_type"] == "BLCA":
			cancer_type_blca_dead_list.append(patient_data["age"])
			cancer_type_blca_dead_patients = cancer_type_blca_dead_patients + 1
		elif patient_data["cancer_type"] == "KIRC":
			cancer_type_kirc_dead_list.append(patient_data["age"])
			cancer_type_kirc_dead_patients = cancer_type_kirc_dead_patients + 1
		elif patient_data["cancer_type"] == "HNSC":
			cancer_type_hnsc_dead_list.append(patient_data["age"])
			cancer_type_hnsc_dead_patients = cancer_type_hnsc_dead_patients + 1
		elif patient_data["cancer_type"] == "PRAD":
			cancer_type_prad_dead_list.append(patient_data["age"])
			cancer_type_prad_dead_patients = cancer_type_prad_dead_patients + 1
		elif patient_data["cancer_type"] == "LUAD":
			cancer_type_luad_dead_list.append(patient_data["age"])
			cancer_type_luad_dead_patients = cancer_type_luad_dead_patients + 1
		elif patient_data["cancer_type"] == "COAD":
			cancer_type_coad_dead_list.append(patient_data["age"])
			cancer_type_coad_dead_patients = cancer_type_coad_dead_patients + 1
		elif patient_data["cancer_type"] == "THCA":
			cancer_type_thca_dead_list.append(patient_data["age"])
			cancer_type_thca_dead_patients = cancer_type_thca_dead_patients + 1
		elif patient_data["cancer_type"] == "OV":
			cancer_type_ov_dead_list.append(patient_data["age"])
			cancer_type_ov_dead_patients = cancer_type_ov_dead_patients + 1
	if patient_data["cancer_type"] == "SKCM":
		cancer_type_skcm_list.append(patient_data["age"])
		cancer_type_skcm_patients = cancer_type_skcm_patients + 1
	elif patient_data["cancer_type"] == "LUSC":
		cancer_type_lusc_list.append(patient_data["age"])
		cancer_type_lusc_patients = cancer_type_lusc_patients + 1
	elif patient_data["cancer_type"] == "READ":
		cancer_type_read_list.append(patient_data["age"])
		cancer_type_read_patients = cancer_type_read_patients + 1
	elif patient_data["cancer_type"] == "STAD":
		cancer_type_stad_list.append(patient_data["age"])
		cancer_type_stad_patients = cancer_type_stad_patients + 1
	elif patient_data["cancer_type"] == "BRCA":
		cancer_type_brca_list.append(patient_data["age"])
		cancer_type_brca_patients = cancer_type_brca_patients + 1
	elif patient_data["cancer_type"] == "BLCA":
		cancer_type_blca_list.append(patient_data["age"])
		cancer_type_blca_patients = cancer_type_blca_patients + 1
	elif patient_data["cancer_type"] == "KIRC":
		cancer_type_kirc_list.append(patient_data["age"])
		cancer_type_kirc_patients = cancer_type_kirc_patients + 1
	elif patient_data["cancer_type"] == "HNSC":
		cancer_type_hnsc_list.append(patient_data["age"])
		cancer_type_hnsc_patients = cancer_type_hnsc_patients + 1
	elif patient_data["cancer_type"] == "PRAD":
		cancer_type_prad_list.append(patient_data["age"])
		cancer_type_prad_patients = cancer_type_prad_patients + 1
	elif patient_data["cancer_type"] == "LUAD":
		cancer_type_luad_list.append(patient_data["age"])
		cancer_type_luad_patients = cancer_type_luad_patients + 1
	elif patient_data["cancer_type"] == "COAD":
		cancer_type_coad_list.append(patient_data["age"])
		cancer_type_coad_patients = cancer_type_coad_patients + 1
	elif patient_data["cancer_type"] == "THCA":
		cancer_type_thca_list.append(patient_data["age"])
		cancer_type_thca_patients = cancer_type_thca_patients + 1
	elif patient_data["cancer_type"] == "OV":
		cancer_type_ov_list.append(patient_data["age"])
		cancer_type_ov_patients = cancer_type_ov_patients + 1
	else:
		print("error cancer type")	

dead_patients_avg_age = sum(dead_patients_age_list) / len(dead_patients_age_list)
alive_patients_avg_age = sum(alive_patients_age_list) / len(alive_patients_age_list)

cancer_type_skcm_avg_age = sum(cancer_type_skcm_list) / len(cancer_type_skcm_list)
cancer_type_lusc_avg_age = sum(cancer_type_lusc_list) / len(cancer_type_lusc_list)
cancer_type_read_avg_age = sum(cancer_type_read_list) / len(cancer_type_read_list)
cancer_type_stad_avg_age = sum(cancer_type_stad_list) / len(cancer_type_stad_list)
cancer_type_brca_avg_age = sum(cancer_type_brca_list) / len(cancer_type_brca_list)
cancer_type_blca_avg_age = sum(cancer_type_blca_list) / len(cancer_type_blca_list)
cancer_type_kirc_avg_age = sum(cancer_type_kirc_list) / len(cancer_type_kirc_list)
cancer_type_hnsc_avg_age = sum(cancer_type_hnsc_list) / len(cancer_type_hnsc_list)
cancer_type_prad_avg_age = sum(cancer_type_prad_list) / len(cancer_type_prad_list)
cancer_type_luad_avg_age = sum(cancer_type_luad_list) / len(cancer_type_luad_list)
cancer_type_coad_avg_age = sum(cancer_type_coad_list) / len(cancer_type_coad_list)
cancer_type_thca_avg_age = sum(cancer_type_thca_list) / len(cancer_type_thca_list)
cancer_type_ov_avg_age = sum(cancer_type_ov_list) / len(cancer_type_ov_list)

cancer_type_skcm_dead_avg_age = sum(cancer_type_skcm_dead_list) / len(cancer_type_skcm_dead_list)
cancer_type_lusc_dead_avg_age = sum(cancer_type_lusc_dead_list) / len(cancer_type_lusc_dead_list)
cancer_type_read_dead_avg_age = sum(cancer_type_read_dead_list) / len(cancer_type_read_dead_list)
cancer_type_stad_dead_avg_age = sum(cancer_type_stad_dead_list) / len(cancer_type_stad_dead_list)
cancer_type_brca_dead_avg_age = sum(cancer_type_brca_dead_list) / len(cancer_type_brca_dead_list)
cancer_type_blca_dead_avg_age = sum(cancer_type_blca_dead_list) / len(cancer_type_blca_dead_list)
cancer_type_kirc_dead_avg_age = sum(cancer_type_kirc_dead_list) / len(cancer_type_kirc_dead_list)
cancer_type_hnsc_dead_avg_age = sum(cancer_type_hnsc_dead_list) / len(cancer_type_hnsc_dead_list)
cancer_type_prad_dead_avg_age = sum(cancer_type_prad_dead_list) / len(cancer_type_prad_dead_list)
cancer_type_luad_dead_avg_age = sum(cancer_type_luad_dead_list) / len(cancer_type_luad_dead_list)
cancer_type_coad_dead_avg_age = sum(cancer_type_coad_dead_list) / len(cancer_type_coad_dead_list)
cancer_type_thca_dead_avg_age = sum(cancer_type_thca_dead_list) / len(cancer_type_thca_dead_list)
cancer_type_ov_dead_avg_age = sum(cancer_type_ov_dead_list) / len(cancer_type_ov_dead_list)

cancer_type_skcm_alive_avg_age = sum(cancer_type_skcm_alive_list) / len(cancer_type_skcm_alive_list)
cancer_type_lusc_alive_avg_age = sum(cancer_type_lusc_alive_list) / len(cancer_type_lusc_alive_list)
cancer_type_read_alive_avg_age = sum(cancer_type_read_alive_list) / len(cancer_type_read_alive_list)
cancer_type_stad_alive_avg_age = sum(cancer_type_stad_alive_list) / len(cancer_type_stad_alive_list)
cancer_type_brca_alive_avg_age = sum(cancer_type_brca_alive_list) / len(cancer_type_brca_alive_list)
cancer_type_blca_alive_avg_age = sum(cancer_type_blca_alive_list) / len(cancer_type_blca_alive_list)
cancer_type_kirc_alive_avg_age = sum(cancer_type_kirc_alive_list) / len(cancer_type_kirc_alive_list)
cancer_type_hnsc_alive_avg_age = sum(cancer_type_hnsc_alive_list) / len(cancer_type_hnsc_alive_list)
cancer_type_prad_alive_avg_age = sum(cancer_type_prad_alive_list) / len(cancer_type_prad_alive_list)
cancer_type_luad_alive_avg_age = sum(cancer_type_luad_alive_list) / len(cancer_type_luad_alive_list)
cancer_type_coad_alive_avg_age = sum(cancer_type_coad_alive_list) / len(cancer_type_coad_alive_list)
cancer_type_thca_alive_avg_age = sum(cancer_type_thca_alive_list) / len(cancer_type_thca_alive_list)
cancer_type_ov_alive_avg_age = sum(cancer_type_ov_alive_list) / len(cancer_type_ov_alive_list)

print("Stats:")
print("Number of Alive Patients: " + str(alive_patients))
print("Alive Patients Avg Age: " + str(alive_patients_avg_age))
print("Number of Dead Patients: " + str(dead_patients))
print("Dead Patients Avg Age: " + str(dead_patients_avg_age))

print("Number of SKCM Patients: " + str(cancer_type_skcm_patients))
print("Average Age of Cancer Type SKCM: " + str(cancer_type_skcm_avg_age))
print("Percentage SKCM Dead Patients: " + str(cancer_type_skcm_dead_patients / float(cancer_type_skcm_patients)))
print("Average Age of Cancer Type SKCM Dead: " + str(cancer_type_skcm_dead_avg_age))
print("Average Age of Cancer Type SKCM Alive: " + str(cancer_type_skcm_alive_avg_age))

print("Number of LUSC Patients: " + str(cancer_type_lusc_patients))
print("Average Age of Cancer Type LUSC: " + str(cancer_type_lusc_avg_age))
print("Percentage LUSC Dead Patients: " + str(cancer_type_lusc_dead_patients / float(cancer_type_lusc_patients)))
print("Average Age of Cancer Type LUSC Dead: " + str(cancer_type_lusc_dead_avg_age))
print("Average Age of Cancer Type LUSC Alive: " + str(cancer_type_lusc_alive_avg_age))

print("Number of READ Patients: " + str(cancer_type_read_patients))
print("Average Age of Cancer Type READ: " + str(cancer_type_read_avg_age))
print("Percentage READ Dead Patients: " + str(cancer_type_read_dead_patients / float(cancer_type_read_patients)))
print("Average Age of Cancer Type READ Dead: " + str(cancer_type_read_dead_avg_age))
print("Average Age of Cancer Type READ Alive: " + str(cancer_type_read_alive_avg_age))

print("Number of STAD Patients: " + str(cancer_type_stad_patients))
print("Average Age of Cancer Type STAD: " + str(cancer_type_stad_avg_age))
print("Percentage STAD Dead Patients: " + str(cancer_type_stad_dead_patients / float(cancer_type_stad_patients)))
print("Average Age of Cancer Type STAD Dead: " + str(cancer_type_stad_dead_avg_age))
print("Average Age of Cancer Type STAD Alive: " + str(cancer_type_stad_alive_avg_age))

print("Number of BRCA Patients: " + str(cancer_type_brca_patients))
print("Average Age of Cancer Type BRCA: " + str(cancer_type_brca_avg_age))
print("Percentage BRCA Dead Patients: " + str(cancer_type_brca_dead_patients / float(cancer_type_brca_patients)))
print("Average Age of Cancer Type BRCA Dead: " + str(cancer_type_brca_dead_avg_age))
print("Average Age of Cancer Type BRCA Alive: " + str(cancer_type_brca_alive_avg_age))

print("Number of BLCA Patients: " + str(cancer_type_blca_patients))
print("Average Age of Cancer Type BLCA: " + str(cancer_type_blca_avg_age))
print("Percentage BLCA Dead Patients: " + str(cancer_type_blca_dead_patients / float(cancer_type_blca_patients)))
print("Average Age of Cancer Type BLCA Dead: " + str(cancer_type_blca_dead_avg_age))
print("Average Age of Cancer Type BLCA Alive: " + str(cancer_type_blca_alive_avg_age))

print("Number of KIRC Patients: " + str(cancer_type_kirc_patients))
print("Average Age of Cancer Type KIRC: " + str(cancer_type_kirc_avg_age))
print("Percentage KIRC Dead Patients: " + str(cancer_type_kirc_dead_patients / float(cancer_type_kirc_patients)))
print("Average Age of Cancer Type KIRC Dead: " + str(cancer_type_kirc_dead_avg_age))
print("Average Age of Cancer Type KIRC Alive: " + str(cancer_type_kirc_alive_avg_age))

print("Number of HNSC Patients: " + str(cancer_type_hnsc_patients))
print("Average Age of Cancer Type HNSC: " + str(cancer_type_hnsc_avg_age))
print("Percentage HNSC Dead Patients: " + str(cancer_type_hnsc_dead_patients / float(cancer_type_hnsc_patients)))
print("Average Age of Cancer Type HNSC Dead: " + str(cancer_type_hnsc_dead_avg_age))
print("Average Age of Cancer Type HNSC Alive: " + str(cancer_type_hnsc_alive_avg_age))

print("Number of PRAD Patients: " + str(cancer_type_prad_patients))
print("Average Age of Cancer Type PRAD: " + str(cancer_type_prad_avg_age))
print("Percentage PRAD Dead Patients: " + str(cancer_type_prad_dead_patients / float(cancer_type_prad_patients)))
print("Average Age of Cancer Type PRAD Dead: " + str(cancer_type_prad_dead_avg_age))
print("Average Age of Cancer Type PRAD Alive: " + str(cancer_type_prad_alive_avg_age))

print("Number of LUAD Patients: " + str(cancer_type_luad_patients))
print("Average Age of Cancer Type LUAD: " + str(cancer_type_luad_avg_age))
print("Percentage LUAD Dead Patients: " + str(cancer_type_luad_dead_patients / float(cancer_type_luad_patients)))
print("Average Age of Cancer Type LUAD Dead: " + str(cancer_type_luad_dead_avg_age))
print("Average Age of Cancer Type LUAD Alive: " + str(cancer_type_luad_alive_avg_age))

print("Number of COAD Patients: " + str(cancer_type_coad_patients))
print("Average Age of Cancer Type COAD: " + str(cancer_type_coad_avg_age))
print("Percentage COAD Dead Patients: " + str(cancer_type_coad_dead_patients / float(cancer_type_coad_patients)))
print("Average Age of Cancer Type COAD Dead: " + str(cancer_type_coad_dead_avg_age))
print("Average Age of Cancer Type COAD Alive: " + str(cancer_type_coad_alive_avg_age))

print("Number of THCA Patients: " + str(cancer_type_thca_patients))
print("Average Age of Cancer Type THCA: " + str(cancer_type_thca_avg_age))
print("Percentage THCA Dead Patients: " + str(cancer_type_thca_dead_patients / float(cancer_type_thca_patients)))
print("Average Age of Cancer Type THCA Dead: " + str(cancer_type_thca_dead_avg_age))
print("Average Age of Cancer Type THCA Alive: " + str(cancer_type_thca_alive_avg_age))

print("Number of OV Patients: " + str(cancer_type_ov_patients))
print("Average Age of Cancer Type OV: " + str(cancer_type_ov_avg_age))
print("Percentage OV Dead Patients: " + str(cancer_type_ov_dead_patients / float(cancer_type_ov_patients)))
print("Average Age of Cancer Type OV Dead: " + str(cancer_type_ov_dead_avg_age))
print("Average Age of Cancer Type OV Alive: " + str(cancer_type_ov_alive_avg_age))


# #plot dead patients
# plt.plot(dead_patients_age_list, dead_pateints_survival_days_list, 'ro', markersize=2)
# plt.title('Dead Patients Age vs Survival In Days')
# plt.axis([0, 100, 0, 5000])
# plt.show()

# #plot alive patients
# plt.plot(dead_patients_age_list, dead_pateints_survival_days_list, 'go', markersize=2)
# plt.title('Alive Patients Age vs Survival In Days')
# plt.axis([0, 100, 0, 5000])
# plt.show()
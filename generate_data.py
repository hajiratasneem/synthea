import requests
import json
from fhir.resources.bundle import Bundle
import subprocess
import os.path
import os, shutil
from os import path

odoo_fhirurl = 'https://emr.nucural.com/fhir/'
# odoo_fhirurl = 'http://localhost:8080/'
synthea_path = '/home/dell/Downloads/synthea'
subprocess.call('./run_synthea -p 500', shell=True, cwd=synthea_path)
synthea_output_path = synthea_path + '/output/fhir/'
if path.exists(synthea_output_path):
    hospital_info_files = []
    patient_files = []
    prac_info_files = []
    for i in os.listdir(synthea_output_path):
        if os.path.isfile(os.path.join(synthea_output_path, i)):
            if i.startswith('hospitalInformation'):
                hospital_info_files.append(i)
            elif i.startswith('practitionerInformation'):
                prac_info_files.append(i)
            else:
                patient_files.append(i)
    final_files = []
    final_files.extend(hospital_info_files)
    final_files.extend(prac_info_files)
    final_files.extend(patient_files)
    for h in final_files:
        f = open(synthea_output_path + h, )
        data_bundle = json.load(f)
        response = requests.post(url=odoo_fhirurl, json=data_bundle)
        print("response--------------", h, response.text)
        print("++++++++++++++++++")
        print("")


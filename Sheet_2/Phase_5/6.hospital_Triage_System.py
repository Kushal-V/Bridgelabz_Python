# patient = [{'patient1': {'severity': 3, 'arrival_time': '2022-01-01 12:00:00'}}]
# sort patient based on severity first and then arrival time

import json

patient_data = json.loads(input("Enter Patient Data: "))

sorted_patients = [
    patient['name']
    for patient in sorted(
        patient_data,
        key=lambda patient: (-patient['severity'], patient['arrival_time'])
    )
]

print(sorted_patients)
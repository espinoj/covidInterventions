import json

fin = open("us_location_interventions.json", "r")
fout = open("us_location_interventions.csv", "w")

us_location_interventions = json.loads(fin.read())

intervention_keys = ["date_reported", "date_lower", "date_upper", "date_ended",
                     "covid_intervention_measure_name"]
fout.write('"state_local_id",')
for i in range(len(intervention_keys)):
    fout.write('"' + intervention_keys[i] + '"')
    if i < len(intervention_keys) - 1:
        fout.write(",")
    else:
        fout.write("\n")

for state_local_id in us_location_interventions:
    # print(state_local_id)
    for interventions in us_location_interventions[state_local_id]:
        fout.write('"' + state_local_id + '",')
        for i in range(len(intervention_keys)):
            fout.write('"' + interventions[intervention_keys[i]] + '"')
            if i < len(intervention_keys) - 1:
                fout.write(",")
            else:
                fout.write("\n")

fin.close()
fout.close()



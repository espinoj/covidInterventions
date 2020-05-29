import json
from datetime import date

date = date.today().strftime("%Y%m%d")

fin = open("us_location_interventions-" + date + ".json", "r")
fout = open("us_location_interventions-" + date + ".csv", "w")

us_location_interventions = json.loads(fin.read())



intervention_keys = ["date_reported",
                     "covid_intervention_id",
                     "location_id",
                     "covid_intervention_id",
                     "date_mean",
                     "date_lower",
                     "date_upper",
                     "date_ended",
                     "covid_intervention_measure_id",
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
    for intervention_idx in range(len(us_location_interventions[state_local_id]['values'])):
        fout.write('"' + state_local_id + '",')
        for i in range(len(intervention_keys)):
            fout.write('"' + str(us_location_interventions[state_local_id]['values'][intervention_idx][i]) + '"')
            if i < len(intervention_keys) - 1:
                fout.write(",")
            else:
                fout.write("\n")

fin.close()
fout.close()



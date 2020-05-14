import json
import requests

us_location_interventions = {}

locations_url = "https://covid19.healthdata.org/api/metadata/location?v=7"
locations_response = requests.get(locations_url)

#print(locations_response.text)

locations_json = json.loads(locations_response.text)

us_locations = None
for loc in locations_json:
    #print(loc)
    if (loc['local_id'] == 'USA'):
        us_locations = loc['children']

for loc in us_locations:
    #print(loc)
    #print(loc['location_id'], loc['location_name'], loc['local_id'])

    interventions_url = "https://covid19.healthdata.org/api/data/intervention?location={0}".format(loc['location_id'])
    intervention_response = requests.get(interventions_url)
    intervention_json = json.loads(intervention_response.text)

    us_location_interventions[loc['local_id']] = intervention_json

f = open("us_location_interventions.json","w")
f.write(json.dumps(us_location_interventions))
f.close()









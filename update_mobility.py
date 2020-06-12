

import json
import requests
from datetime import date


us_location_mobility = {}

locations_url = "https://covid19.healthdata.org/api/metadata/location?v=7"
locations_response = requests.get(locations_url)

date = date.today().strftime("%Y%m%d")

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

    mobility_url = "https://covid19.healthdata.org/api/data/hospitalization?location={0}&measure=composite_mobility".format(loc['location_id'])
    mobility_response = requests.get(mobility_url)
    mobility_json = json.loads(mobility_response.text)

    us_location_mobility[loc['local_id']] = mobility_json

f = open("us_location_mobility-" + date + ".json","w")
f.write(json.dumps(us_location_mobility))
f.close()










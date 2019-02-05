import json
import pandas as pd
import glob

files = glob.glob("upper-niger-water*.geojson")

for f in files:
    content = open(f).read()
    data = json.loads(content)
    hybas_id = data['features'][0]['properties']['HYBAS_ID']

    print(f)
    with open('./by_id/water-area-' + str(int(hybas_id)) + '.geojson', 'w') as out:
        out.write(content)


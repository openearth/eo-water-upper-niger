import json
import pandas as pd

data = json.load(open('water-area.geojson'))

def get_row(data):
    for f in data['features']:
        p = f['properties']

        hybas_id = p['HYBAS_ID']

        times = p['times']
        areaBIO = p['areaBIO']
        areaMNDWI = p['areaMNDWI']

        df = pd.DataFrame({ 
            'hybas_id': hybas_id, 
            'time': times, 
            'areaBIO': areaBIO, 
            'areaMNDWI': areaMNDWI
        })

        df['datetime'] = pd.to_datetime(df['time'], unit='ms')
        df['date'] = df['datetime'].apply(lambda x: x.strftime('%Y-%m-%d'))

        yield df


data_all = list(get_row(data))

data_all = pd.concat([d for d in data_all])

data_all.to_csv('water-area.csv')
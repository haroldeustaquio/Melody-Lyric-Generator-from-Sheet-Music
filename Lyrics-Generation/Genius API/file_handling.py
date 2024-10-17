import json
import pandas as pd
def read_json(name):
    with open(f'data/{name}.json', 'r') as file:
        data = json.load(file)
    return data

def save_json(name,data):
    with open(f'data/{name}.json', 'w') as file:
        json.dump(data, file, indent=4)


def save_as_csv(data):
    history = pd.read_csv('data/filter_data.csv')
    
    lyrics, feelings = [], []
    
    for i in range(len(data)):
        lyrics.append(data[i]['lyrics'])
        feelings.append(', '.join(data[i]['feelings']))

    data = {
        'lyrics':lyrics,
        'feelings': feelings
    }
    
    df = pd.DataFrame(data)
    history = pd.concat([history,df],axis=0)
    history.to_csv('data/filter_data.csv',index=False)
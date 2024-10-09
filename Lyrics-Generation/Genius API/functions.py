import lyricsgenius
import pandas as pd
import time
import json
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json 

nltk.download('stopwords')
nltk.download('punkt_tab')

lexicon = pd.read_csv('espaniol_NRC.csv', index_col='Spanish Word')

def upload_song_data(artista_name, max_retries=5):
    
    data = read_json()
    retries = 0  # Contador de reintentos
    while retries < 5:  # Límite de reintentos
        genius = lyricsgenius.Genius(obtain_access_token())
        try:
            artista = genius.search_artist(artista_name,max_songs=1) # ,max_songs=10
            nuevas_filas = []
            for cancion in artista.songs:
                new_text = clean_text(cancion.lyrics)
                fila = {
                    'artista': artista_name,
                    'titulo': cancion.title,
                    'letra': new_text,
                    'feelings': feelings_in_text(new_text)
                } 
                nuevas_filas.append(fila)
                # print(fila)
            data.extend(nuevas_filas)
            print(f'Hay {len(nuevas_filas)} canciones nuevas')
            save_json(data)
            break  # Salir del bucle si la operación fue exitosa

        except FileNotFoundError as e:
            print("Archivo no encontrado. Verifica que 'keys.json' y 'data.json' existan.")
            break
        except json.JSONDecodeError as e:
            print("Error al decodificar JSON. Verifica la sintaxis del archivo.")
            break
        except Exception as e:
            print(f"Error: {e}. Intento {retries}/{max_retries}. Esperando 5 segundos antes de reintentar...")
            time.sleep(5)  # Espera 5 segundos antes de volver a intentar

def obtain_access_token():
    with open('keys.json', 'r') as file:
        data = json.load(file)
    return data['access_token']

def read_json():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

def save_json(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def clean_text(lyrics):
    lyrics = re.sub(r'\[.*?\]', '', lyrics)
    lyrics = re.sub(f'[{re.escape(string.punctuation)}]', ' ', lyrics).replace('\n', ' ').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').lower()
    lyrics = re.sub(r'(\d+|embed)$', '', lyrics)
    lyrics = re.sub(r'(\d+)$', '', lyrics)
    lyrics = re.sub(r'^.*?lyrics\s*', '', lyrics)
    lyrics = re.sub(r'\s+', ' ', lyrics)
    lyrics = re.sub(r'\d+', '', lyrics)
    
    tokens = word_tokenize(lyrics)
    stop_words = set(stopwords.words('spanish'))
    tokens_filtrados = [word for word in tokens if word.lower() not in stop_words]
    lyrics = " ".join(tokens_filtrados)
    
    return lyrics

def feelings_in_text(text):
    feelings_count = {col: 0 for col in lexicon.columns}
    words = text.split()

    for word in words:
        if word in lexicon.index:
            feeling_values = lexicon.loc[word].values
            for i,value in enumerate(feeling_values):
                feelings_count[lexicon.columns[i]] += value
    
    sorted_items = sorted(feelings_count.items(), key=lambda item: item[1], reverse=True)[:3]
    feelings = [item[0] for item in sorted_items]
    return feelings

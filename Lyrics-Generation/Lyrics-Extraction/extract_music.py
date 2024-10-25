import importlib
import file_handling, feelings_analysis, text_processing
importlib.reload(file_handling)
importlib.reload(text_processing)
importlib.reload(feelings_analysis)

import lyricsgenius
import time
import json 

def upload_song_data(artist_name, max_retries=5):
    
    complete_data = file_handling.read_json('complete_data')
    filter_data = file_handling.read_json('filter_data')
    retries = 0  # Contador de reintentos
    while retries < 5:  # Límite de reintentos
        genius = lyricsgenius.Genius(obtain_access_token())
        try:
            artista = genius.search_artist(artist_name) # ,max_songs=10
            complete_rows = []
            filter_rows = []
            for cancion in artista.songs:
                new_text = text_processing.clean_text(cancion.lyrics)
                feelings = feelings_analysis.feelings_in_text(new_text)
                complete_row = {
                    'artist': artist_name,
                    'title': cancion.title,
                    'lyrics': new_text,
                    'feelings': feelings
                }
                
                filter_row = {
                    'lyrics': new_text,
                    'feelings': feelings
                }
                
                complete_rows.append(complete_row)
                filter_rows.append(filter_row)
            complete_data.extend(complete_rows)
            filter_data.extend(filter_rows)
            file_handling.save_as_csv(filter_rows)
            print(f'Hay {len(complete_rows)} canciones nuevas')
            
            file_handling.save_json('complete_data',complete_data)
            file_handling.save_json('filter_data',filter_data)
            break
        
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
    with open('data/keys.json', 'r') as file:
        data = json.load(file)
    return data['access_token']


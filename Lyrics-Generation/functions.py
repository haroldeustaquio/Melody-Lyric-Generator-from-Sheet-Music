import lyricsgenius
import pandas as pd
import time
import json

def upload_song_data(artista_name, max_retries=5):
    
    data = read_data_json()
    retries = 0  # Contador de reintentos
    while retries < 5:  # Límite de reintentos
        genius = lyricsgenius.Genius(obtain_access_token())
        try:
            artista = genius.search_artist(artista_name,max_songs=10)
            nuevas_filas = []
            for cancion in artista.songs:
                fila = {
                    'artista': artista_name,
                    'titulo': cancion.title,
                    'letra': cancion.lyrics
                }               
                nuevas_filas.append(fila)
                # print(fila)
            data.extend(nuevas_filas)
            print(f'Hay {len(nuevas_filas)} canciones nuevas')
            save_data_json(data)
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
    with open('keys.json', 'r') as archivo:
        datos = json.load(archivo)
    return datos['access_token']

def read_data_json():
    with open('data.json', 'r') as archivo:
        data = json.load(archivo)
    return data

def save_data_json(data):
    with open('data.json', 'w') as archivo:
        json.dump(data, archivo, indent=4)



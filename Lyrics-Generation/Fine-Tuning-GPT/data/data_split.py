import json

with open("complete_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def format_and_write(data_slice, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for song in data_slice:
            artist = song.get("artist", "Desconocido")
            title = song.get("title", "Sin Título")
            lyrics = song.get("lyrics", "").replace("\n", " ")
            feelings = ", ".join(song.get("feelings", []))

            output_file.write(f"Título: {title}\n")
            output_file.write(f"Artista: {artist}\n")
            if feelings:
                output_file.write(f"Sentimientos: {feelings}\n")
            output_file.write(f"{lyrics}\n")
            output_file.write("<|endoftext|>\n\n")

slices_and_files = [
    (data[:1354], "data_1.txt"),
    (data[1354:2708], "data_2.txt"),
    (data[2708:4062], "data_3.txt"),
    (data[4062:], "data_4.txt"),
]

for data_slice, output_file_path in slices_and_files:
    format_and_write(data_slice, output_file_path)

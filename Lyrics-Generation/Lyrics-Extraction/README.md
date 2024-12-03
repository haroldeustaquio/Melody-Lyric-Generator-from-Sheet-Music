# Lyrics Extraction

## Overview

**Lyrics Extraction** is part of **Melody-Lyric-Generator**, which is designed to extract, process, and analyze emotional content from song lyrics. The project uses the **LyricsGenius API** to retrieve lyrics, processes the text to clean it, and then performs sentiment analysis using a predefined lexicon. The results are stored in JSON and CSV formats for further exploration and visualization.

**Content:**
- [Architecture](#architecture)
- [Functions](#functions)
    - [text_preprocessing.py](#text_preprocessingpy)
    - [feelings_analysis.py](#extract_musicpy)
    - [file_handling.py](#file_handlingpy)
    - [extract_music.py](#extract_musicpy)
    - [main.py](#mainpy)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
---

## Architecture

<p align="center">
  <img src="https://github.com/user-attachments/assets/f5565510-b8ad-48c9-80c1-8f62b8a65215" alt="Architecture">
</p>

<p align="center">
  <em>Figure 1: Architecture of Lyrics Generation</em>
</p>


---

## Functions

### ``text_preprocessing.py``
- Cleans song lyrics by removing unnecessary elements such as metadata, punctuation, numbers, and stopwords.
- Normalizes text by converting to lowercase and replacing accented characters.
- Prepares lyrics for further processing, such as tokenization and emotional analysis.

**Key Function:**
- ``clean_text(lyrics)``: Cleans and preprocesses the input lyrics, returning a normalized string without stopwords or extraneous content.

### `feelings_analysis.py`
- Reads a lexicon from a CSV file (`espaniol_NRC.csv`).
- Analyzes the emotional content of a given text by matching words with the lexicon.

**Key Functions:**
- `feelings_in_text(text)`: Takes a string as input, calculates the top three emotions present in the text based on the lexicon, and returns them.

### `file_handling.py`
- Handles reading and writing JSON files.
- Saves processed data as a CSV for persistent storage.

**Key Functions:**
- `read_json(name)`: Reads a JSON file from the `data` directory.
- `save_json(name, data)`: Writes data to a JSON file in the `data` directory.
- `save_as_csv(data)`: Appends new data to an existing CSV file (`filter_data.csv`) or creates it if it doesn’t exist.

### `extract_music.py`
- Retrieves song lyrics using the LyricsGenius API.
- Cleans the lyrics text using `text_processing` (assumed to be implemented elsewhere).
- Analyzes the emotional content of the lyrics using `feelings_analysis.py`.
- Saves the processed data in JSON and CSV formats using `file_handling.py`.

**Key Functions:**
- `upload_song_data(artist_name, max_retries=5)`: Main function to fetch and process song data for a given artist. Handles retries in case of API or connection issues.
- `obtain_access_token()`: Reads the API access token from a JSON file.


### `main.py`
This is the entry point of the project. It:
- Imports the necessary modules.
- Calls the `upload_song_data()` function from `extract_music.py` with a specified artist name to initiate the data processing pipeline.

---

## Prerequisites

- **Python Environment**: Ensure you have Python 3.8 or higher installed.
- **Dependencies**:
   - `lyricsgenius`
   - `pandas`
- **Files**:
   - `data/keys.json`: Contains your LyricsGenius API access token (`{"access_token": "your_token"}`).
   - `espaniol_NRC.csv`: A lexicon file used for emotion analysis.

To install required Python packages, run:

```bash
pip install lyricsgenius pandas
```

## Installation
1. Clone this repository and navigate to the project directory.

    ```bash
    pip clone https://github.com/haroldeustaquio/Melody-Lyric-Generator.git
    ```

    ```bash
    cd Lyrics-Generation/Lyrics-extraction
    ```

2. Set up the required files in the data directory:
    - Create a ``keys.json`` file and add your LyricsGenius API token.
    - Ensure the ``espaniol_NRC.csv`` file is present in the root directory.

3. Run the project by executing:
    ```bash
    python main.py
    ```

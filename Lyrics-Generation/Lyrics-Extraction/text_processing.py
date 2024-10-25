import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


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

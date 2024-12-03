# Melody-Lyric-Generator

## Overview

**Melody-Lyric-Generator** is designed to combine melody generation and lyric generation for creating cohesive musical content. It processes, analyzes, and generates melodies using MIDI data, while simultaneously handling lyric extraction and fine-tuning for generating Spanish-language text. This project employs advanced datasets, custom preprocessing functions, and machine learning models to produce high-quality musical and lyrical outputs.

**Content:**

- [Lyrics Generation](#lyrics-generation)
- [Melody Generation](#melody-generation)

---

## Lyrics Generation

**Lyrics Generation** processes and analyzes song lyrics using the LyricsGenius API, cleaning the data and identifying emotional content through a lexicon-based approach. Additionally, it fine-tunes the pre-trained [`datificate/gpt2-small-spanish`](https://huggingface.co/datificate/gpt2-small-spanish) model for text generation.

**Key Features:**
- **Data Cleaning**: Removes unnecessary elements such as metadata, punctuation, and stopwords.
- **Emotional Analysis**: Identifies emotions in lyrics using a specialized lexicon.
- **Fine-Tuning GPT**: Trains the model across multiple datasets, optimizing for coherent and emotionally rich text.

---

## Melody Generation

**Melody Generation** processes, analyzes, and generates melodies using the MAESTRO dataset and custom MIDI handling functions. A machine learning model is trained to predict musical notes, evaluate performance, and produce cohesive melodies.

**Key Features:**
- **Custom MIDI Functions**: Includes tools for note extraction, sequence creation, and MIDI playback.
- **Neural Network Architecture**: Trains on features like pitch, step, and duration to predict melodies.
- **Evaluation Metrics**: Uses RMSE and R² to measure the quality of generated melodies.


---

<div align="center"> 
  <em> 
    We believe in the power of collaboration. If you have ideas, suggestions, or improvements, feel free to open an issue or submit a pull request. Let’s make this project even better—your contributions are always welcome! 
  </em> 
</div>


# Lyrics Generator

## Overview

This project integrates ``lyrics extraction`` and ``fine-tuning GPT-2`` for Spanish text generation. It processes song lyrics, analyzes their emotional content, and fine-tunes a pre-trained GPT-2 model for generating coherent and relevant lyrics.

**Content:**
- [Lyrics Extraction](#lyrics-extraction)
- [Fine-Tuning GPT](#fine-tuning-gpt)

---

## Lyrics Extraction

The lyrics extraction component processes and analyzes song lyrics using the LyricsGenius API and a predefined lexicon for emotion detection.

**Key Features:**
- **Data Cleaning**: Removes unnecessary elements such as metadata, punctuation, and stopwords.
- **Emotional Analysis**: Identifies key emotions in lyrics using a specialized lexicon.
- **File Management**: Stores processed data in JSON and CSV formats for further use.

---

## Fine-Tuning GPT

This component focuses on fine-tuning the pre-trained [`datificate/gpt2-small-spanish`](https://huggingface.co/datificate/gpt2-small-spanish) model for Spanish text generation.

**Key Features:**
- Fine-tuned across four stages using different dataset subsets.
- Evaluated using metrics such as perplexity, distinct-n, lexical diversity, and local coherence.
- Optimized for tasks like generating coherent and emotionally rich lyrics.

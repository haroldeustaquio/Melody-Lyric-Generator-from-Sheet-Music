import pandas as pd
lexicon = pd.read_csv('espaniol_NRC.csv', index_col='Spanish Word')

def feelings_in_text(text):
    feelings_count = {col: 0 for col in lexicon.columns}
    words = text.split()

    for word in words:
        if word in lexicon.index:
            feeling_values = lexicon.loc[word].values
            for i, value in enumerate(feeling_values):
                feelings_count[lexicon.columns[i]] += value

    sorted_items = sorted(feelings_count.items(), key=lambda item: item[1], reverse=True)[:3]
    feelings = [item[0] for item in sorted_items]
    return feelings

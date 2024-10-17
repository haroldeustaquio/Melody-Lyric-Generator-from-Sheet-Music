import pandas as pd
from transformers import GPT2Tokenizer
from transformers import GPT2LMHeadModel
import torch
from torch.optim import AdamW

df = pd.read_csv('data/filter_data.csv')

tokenizer = GPT2Tokenizer.from_pretrained('gpt2_spa_local')

prepared_data = []

for index, row in df.iterrows():
    input_text = f"{row['lyrics']} [SENTIMENTS] {row['feelings']}"
    prepared_data.append(input_text)


tokenized_data = [tokenizer.encode(text, return_tensors='pt') for text in prepared_data]
model = GPT2LMHeadModel.from_pretrained('./gpt2_spa_local')
model.train()

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)


optimizer = AdamW(model.parameters(), lr=5e-5)

num_epochs = 3

for epoch in range(num_epochs):
    for tokenized_input in tokenized_data:
        tokenized_input = tokenized_input.to(device)

        # Forward
        outputs = model(tokenized_input, labels=tokenized_input)
        loss = outputs.loss

        # Backward
        loss.backward()

        # Actualizar los pesos
        optimizer.step()
        optimizer.zero_grad()

        print(f"Epoch: {epoch}, Loss: {loss.item()}")

model.save_pretrained('./trained_gpt2_spa_local')
tokenizer.save_pretrained('./trained_gpt2_spa_local')
# Lyrics Generator

## **Using Genius API**

1. **Download Lyrics**:
   - Utilize the Genius API to gather Spanish song lyrics. Make sure to comply with their API usage guidelines.
   - Store the downloaded lyrics in a structured format (e.g., CSV or JSON) for easy access and processing.

2. **Preprocess Lyrics**:
   - Clean the lyrics data by removing unwanted characters, formatting issues, and duplicates.
   - Normalize the text by converting all lyrics to lowercase and removing punctuation marks.

3. **Sentiment Analysis**:
   - Apply a sentiment analysis tool to categorize the lyrics based on emotional tone (e.g., happy, sad, nostalgic).
   - Store the results of the sentiment analysis along with the corresponding lyrics for future reference.

4. **Train a Model**:
   - Use the preprocessed lyrics and their sentiment labels to train a Recurrent Neural Network (RNN) or another suitable model (e.g., LSTM).
   - Fine-tune the model’s parameters to improve its performance in generating lyrics that match the desired emotional tone.

5. **Generate New Lyrics**:
   - Create a user interface where users can input specific words or phrases and select an emotional tone.
   - Use the trained model to generate new lyrics based on the input, ensuring that the generated content aligns with the specified words and sentiment.

6. **Evaluate and Refine**:
   - Review the generated lyrics for coherence and creativity. Conduct user testing to gather feedback on the quality of the output.
   - Continuously refine the model and preprocessing steps based on user feedback and performance metrics.

## **Using LLaMA 3.2**

1. **Download Model with Ollama**:
   - Use the Ollama tool to download the LLaMA 3.2 model. Ensure you have Ollama installed and configured on your system.
   - Run the appropriate command in the terminal to fetch the model, which enables you to leverage its advanced capabilities for lyric generation.

2. **Setup for Generation**:
   - Prepare the environment for using the LLaMA model by ensuring all dependencies and required libraries are installed.
   - Load the LLaMA model into your script or application, ready for lyric generation tasks.

3. **Customize Input**:
   - Allow users to specify keywords and emotional tone (e.g., sad, happy, nostalgic) for the generated lyrics.
   - Structure the input to pass both the keywords and sentiment to the LLaMA model.

4. **Generate Lyrics**:
   - Call the model to generate new lyrics based on the input criteria. Ensure the model processes the keyw

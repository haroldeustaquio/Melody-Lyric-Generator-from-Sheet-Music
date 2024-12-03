# Melody Generation

## Overview

**Melody Generation** is designed to process, analyze, and generate melodies based on MIDI data. This project utilizes the MAESTRO dataset and implements custom MIDI handling functions for tasks such as note extraction and sequence creation. A machine learning model is trained to predict musical notes and generate coherent melodies, which are evaluated using various metrics.

The workflow includes dataset preparation, where MIDI files are loaded and structured for analysis, followed by sequence creation, transforming data into sequences suitable for model training. The model is then trained using a neural network architecture to predict and generate melodies. Finally, the results are evaluated using metrics like RMSE and R², providing insights into the performance of the generated melodies.


**Content:**

- [Architecture](#architecture)
- [MAESTRO Dataset](#maestro-dataset)
- [Functions to handle MIDI](#functions-to-handle-midi)
- [Melody Generation Process](#melody-generation-process)
    - [Dataset Preparation](#dataset-preparation)
    - [Sequence Creation](#sequence-creation)
    - [Model Creation and Training](#model-creation-and-training)
    - [Melody Prediction](#melody-prediction)
- [Evaluation Metrics and Process](#evaluation-metrics-and-process)
- [Result and Analysis](#results-and-analysis)
- [Prerequisites](#prerequisites)
- [References](#references)

---

## Architecture

<p align="center">
  <img src="https://github.com/user-attachments/assets/f28c462b-b41f-4584-8c65-336545b3ac17" alt="Architecture">
</p>

<p align="center">
  <em>Figure 1: Architecture of Melody Generation</em>
</p>

---

## MAESTRO Dataset

The compressed file maestro-v3.0.0-midi.zip contains version 3.0.0 of the MAESTRO dataset (MIDI and Audio Edited for Synchronous Tracks and Organization). This dataset consists of approximately 200 hours of virtuosic piano performances, captured with a precise alignment of around 3 milliseconds between note labels and audio waveforms.

For more information about this dataset, visit: https://magenta.tensorflow.org/datasets/maestro

---

## Functions to handle MIDI

### `display_audio()`
This function:
- Generates an audio playback from a processed MIDI object using sound synthesis.
- Converts MIDI content into an audio waveform with a defined sampling rate and trims the audio to a default duration of 30 seconds.
- Returns the generated audio snippet for direct playback.


### `midi_to_notes()`
This function:
- Converts a MIDI file into a structured dataset describing its notes.
- Loads the MIDI file, selects the first instrument, and organizes the notes chronologically by their start times.
- Extracts features for each note, such as pitch, start time, end time, interval between notes (step), and duration.
- Stores the extracted information in a DataFrame for easy analysis and processing.


### `notes_to_midi()`
This function:
- Creates a MIDI file from a dataset describing musical notes and saves it to a specified output file.
- Uses input data such as pitch, step, and duration to construct individual notes.
- Assigns notes to a specified instrument with a default velocity and maintains the temporal progression.
- Adds the instrument to a MIDI object and saves it as a file, enabling playback or reuse of the generated melody.


### `create_sequence()`
This function:
- Adjusts the sequence length to `seq_length + 1`, ensuring each sequence includes both input data and a corresponding label.
- Divides the dataset into consecutive overlapping sequences using a sliding window approach.
- Groups sequences into batches of uniform length and normalizes features such as pitch by dividing them by specific values.
- Splits sequences into:
  - **Inputs**: All notes except the last one in each sequence.
  - **Labels**: The last note in each sequence, mapped to keys such as pitch, step, and duration.
- Applies defined transformations to all sequences and organizes them into shuffled batches for efficient training.


---

## Melody Generation Process

### Dataset Preparation

- **Loading MIDI Files**: A limited number of MIDI files are processed (e.g., the first `N` files). Notes and their characteristics (e.g., pitch, step, and duration) are extracted using the `midi_to_notes()` function and stored in a list.
- **Combining Data**: Extracted notes from all files are merged into a single DataFrame using `pd.concat`, creating a consolidated collection of notes from the MIDI files.
- **Organizing Features**: Specific characteristics (pitch, step, duration) are organized in a defined order, and the data is arranged into a matrix (`train_notes`), where each row represents a note and each column corresponds to a specific feature.
- **TensorFlow Dataset Creation**: The matrix is converted into a TensorFlow dataset (`notes_ds`) for efficient use in machine learning models.


### Sequence Creation

- **Sequence Length Adjustment**: Sets sequence length as `seq_length + 1`, ensuring each sequence contains both inputs and a corresponding label.
- **Sliding Window Segmentation**: The dataset is divided into overlapping sequences using a sliding window with a one-step offset between windows, preserving the temporal progression of notes.
- **Batch Grouping**: Sequences are grouped into uniform batches of size 64 for efficient processing.
- **Feature Normalization**: Features like pitch are normalized by dividing them by specific values (e.g., `vocab_size`), scaling data to a relative range.
- **Input-Label Splitting**: Sequences are split into:
  - **Inputs**: All notes except the last one in each sequence.
  - **Labels**: The last note in each sequence, mapped to their corresponding keys (pitch, step, duration).
- **Shuffling and Optimization**: Sequences are shuffled to avoid repetitive patterns, and prefetching techniques are used to minimize loading times, speeding up the training process.


### Model Creation and Training

- **Custom Loss Function**: Defines a function (`mse_with_positive_pressure`) combining Mean Squared Error (MSE) with an additional penalty for negative values in predictions, encouraging positive outputs.
- **Sparse Categorical Crossentropy**: Used as the loss function for predicting pitch (a categorical variable with 128 MIDI classes). It computes the cross-entropy between predicted probabilities and true labels efficiently.
- **Input Shape and Learning Rate**:
  - Input shape: `(seq_length, 3)`, where each sequence includes 31 steps and 3 features (pitch, step, duration).
  - Learning rate: Set to 0.005 for controlled model adjustments.
- **Model Architecture**:
  - Input layer processes musical sequences.
  - Two LSTM layers capture temporal relationships in the data.
  - Three independent dense layers output predictions for pitch, step, and duration.
- **Model Compilation**: Uses the Adam optimizer with adaptive learning rates and the defined loss functions for efficient model training.



### Melody Prediction

- **Initializing Input Data**: A sample of notes (`sample_notes`) is used as input for melody generation. These are normalized (`input_notes`) to match the model's expected format.
- **`predict_next_note()` Function**:
  - Expands the input dimensions to meet the model's requirements.
  - Predicts the next note's features (pitch, step, and duration) based on the prior sequence.
  - Applies temperature-based adjustments to pitch for increased variability.
  - Uses probabilistic sampling for pitch values from a categorical distribution.
  - Ensures step and duration predictions are non-negative.
- **Generation Parameters**:
  - **Temperature**: Set to 2.0 to control prediction randomness, enhancing diversity in generated notes.
  - **Notes to Generate**: Specifies the number of additional notes to generate, e.g., 120, for creating a complete melody.


---

## Evaluation Metrics and Process

### Metrics

- **Root Mean Square Error (RMSE)**: Measures the average magnitude of error between the predicted and actual values, particularly useful for numeric features like `duration` and `step`. Lower RMSE values indicate more accurate predictions. It is calculated as:

```math
RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}
```


- **Coefficient of Determination (R²)**: Evaluates the proportion of variance in the actual values explained by the model, R² values close to 1 indicate the model captures the underlying patterns well. It is calculated as:


```math
R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}
```


### Evaluation Process

1. **Test Data Selection**: The first 31 notes from a MIDI file are used as input to the model to predict subsequent notes.
2. **Prediction Comparison**: The predicted notes are compared with the actual notes from the same file for corresponding positions.
3. **Metric Calculation**: RMSE and R² values are computed for each feature (pitch, step, and duration) to assess the model's performance.

---

## Results and Analysis

### RMSE of Pitch

- The configuration `melody_50` consistently exhibits the lowest RMSE across all prediction stages, reaching a minimum value at 1000 predictions. This indicates that `melody_50` is the most effective in terms of pitch accuracy.
- As the number of predictions increases, all configurations show a gradual decline in RMSE, suggesting improved performance with longer sequences.
- The configuration `melody_25` follows closely in performance but remains slightly higher in RMSE compared to `melody_50`, indicating it is also effective but less precise for pitch prediction.
- Configurations with more complex data, such as `melody_75` and `melody_100`, maintain higher RMSE values throughout, reflecting the model's difficulty in managing intricate pitch relationships in these scenarios.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1bb6ac97-72d4-4c74-8390-87862136277e" alt="Architecture">
</p>

<p align="center">
  <em>Figure 2: RMSE of Pitch</em>
</p>


### RMSE of Step

- Simpler melodies (`melody_25` and `melody_50`) exhibit a significant decrease in RMSE as the number of predictions increases, highlighting their greater stability and precision in temporal representation.
- The configuration `melody_25` demonstrates the best overall performance, achieving an RMSE of 0.2270 after 1000 predictions, making it the most efficient option for tasks requiring high accuracy in simple temporal relationships.
- More complex configurations, such as `melody_75` and `melody_100`, maintain higher RMSE values throughout, indicating the model struggles with capturing more intricate temporal patterns in these cases.
- As the number of predictions grows, the divergence between simpler and more complex melodies becomes evident, emphasizing the importance of simplicity in achieving lower RMSE for step prediction.

<p align="center">
  <img src="https://github.com/user-attachments/assets/7e452450-4d59-400c-ac45-73d50a746646" alt="Architecture">
</p>

<p align="center">
  <em>Figure 3: RMSE of Step</em>
</p>



### RMSE of Duration

- Configurations `melody_25` and `melody_50` show continuous improvement in RMSE for duration as the number of predictions increases, reaching values of 0.3198 and 0.3094 respectively at 1000 predictions. This indicates the model is more efficient at handling simpler melodies with less complex temporal relationships.
- In contrast, more complex configurations like `melody_100` maintain high RMSE values throughout, with a slight increase as the number of predictions grows (from 0.6477 to 0.6639). This suggests the model struggles to capture more intricate temporal patterns in the duration feature.
- The performance gap between simple (`melody_25` and `melody_50`) and complex (`melody_75` and `melody_100`) configurations highlights the model's limitations in handling temporal complexity, emphasizing the need for improvements in data preprocessing or model architecture.
- Overall, the results suggest that for tasks requiring accurate handling of duration, simpler configurations are more suitable and yield significantly better results.


<p align="center">
  <img src="https://github.com/user-attachments/assets/237e36b5-8326-4a9f-b14b-53dc1cfa0cde" alt="Architecture">
</p>

<p align="center">
  <em>Figure 4: RMSE of Duration</em>
</p>





### R2 of Pitch

- The negative R² values across all configurations indicate insufficient model performance in predicting pitch variability. The configuration `melody_50` achieves the least negative R² value (-4.0616 at 1000 predictions), making it the most suitable among the evaluated options.
- More complex configurations, such as `melody_75` and `melody_100`, demonstrate greater difficulty in capturing relationships in pitch data, with consistently low R² values. This highlights the need to refine the model or input features to enhance predictive capabilities for more intricate melodies.
- The performance gap between simpler (`melody_50`) and complex configurations further emphasizes the importance of tailored adjustments for handling complex temporal patterns effectively.


<p align="center">
  <img src="https://github.com/user-attachments/assets/1c3cb912-c39a-4963-b347-c37ebb183328" alt="Architecture">
</p>

<p align="center">
  <em>Figure 5: R2 of Pitch</em>
</p>



### R2 of Step

- The configuration `melody_25` exhibits the least negative R² values across all predictions, reaching -0.2772 at 1000 predictions. This indicates that the model is relatively more effective at capturing temporal relationships in simple melodies, though it remains suboptimal compared to an ideal baseline.
- More complex configurations, such as `melody_75` and `melody_100`, show a significant deterioration in R² values as the number of predictions increases, dropping to -4.4354 and -12.0093 respectively at 1000 predictions. This demonstrates that the current model architecture struggles to handle complex temporal relationships effectively.
- The results emphasize the necessity of improving both the input data preprocessing and the model architecture to enhance performance for more intricate melodies.
- The stark difference between simpler and more complex configurations underscores the importance of adapting the model for varying levels of temporal complexity.


<p align="center">
  <img src="https://github.com/user-attachments/assets/750cc13a-b060-4adb-8aef-5fa7508119bb" alt="Architecture">
</p>

<p align="center">
  <em>Figure 6: R2 of Step</em>
</p>



### R2 of Duration

- Simpler configurations, such as `melody_25` and `melody_50`, exhibit less negative R² values compared to more complex configurations. For instance, `melody_25` achieves -0.4404 and `melody_50` reaches -0.3484 at 1000 predictions, indicating relatively better performance in handling melodies with lower temporal complexity.
- More complex configurations, like `melody_100`, show significant deterioration in R² values, dropping to -5.2099 at 1000 predictions. This highlights the model's inability to effectively manage complex temporal relationships in the duration feature.
- The results underscore the need for improvements in both model architecture and advanced data preprocessing techniques to handle intricate temporal dependencies more effectively.
- The gap in performance between simple and complex configurations emphasizes the importance of tailoring the model to the complexity of the temporal patterns in the data.


<p align="center">
  <img src="https://github.com/user-attachments/assets/d8840672-359f-46c4-a184-3752f77478c3" alt="Architecture">
</p>

<p align="center">
  <em>Figure 7: R2 of Duration</em>
</p>


---

## Prerequisites

To install the necessary packages for `Melody Generation`, execute the following command:


```bash
sudo apt install -y fluidsynth
pip install --upgrade pyfluidsynth pretty_midi numpy pandas seaborn tensorflow matplotlib
```

---

## References

1. Magenta (2024).  
   **"MAESTRO Dataset".**  
   URL: [https://magenta.tensorflow.org/datasets/maestro](https://magenta.tensorflow.org/datasets/maestro)  

2. Kasif, A., Sevgen, S., Ozcan, A., and Catal, C. (2024).  
   **"Hierarchical multi-head attention LSTM for polyphonic symbolic melody generation".**  
   En *Multimedia Tools and Applications*.  
   DOI: [10.1007/s11042-024-18491-7](https://doi.org/10.1007/s11042-024-18491-7)  


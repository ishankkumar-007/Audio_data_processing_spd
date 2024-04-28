# AviaryMorse Documentation

## Introduction
AviaryMorse is an AI project designed to decode Morse code messages represented by bird sounds. The project utilizes machine learning techniques to train a model on two different audio clips of bird sounds, each representing a Morse code dot and dash, respectively. Once trained, the model can identify and classify these sounds as dots and dashes, enabling the decoding of Morse code messages transmitted through bird vocalizations.

## Features and Capabilities

- **Trained Model for Morse Code Classification**: AviaryMorse includes a pre-trained model capable of accurately classifying Morse code dots and dashes represented by bird sounds.

- **Custom Dataset Creation**: Users have the ability to create their own datasets using provided code. This allows flexibility in choosing dot and dash sounds, which need not be restricted to bird sounds.

- **Feature Extraction**: The model utilizes Mel-frequency cepstral coefficients (MFCC) feature extraction from audio files for training. This technique enhances the model's ability to understand the nuances of bird sounds and Morse code patterns.

- **Flexibility in Feature Selection**: AviaryMorse offers the potential for using other prominent features for training, although this capability is not yet implemented.

- **High Prediction Accuracy**: Despite the relatively small training dataset of only 82 files, the model achieves an impressive prediction accuracy of 88%. This demonstrates the robustness and effectiveness of the model.

- **Powerful Classification**: The trained model exhibits a high level of classification accuracy, making it a reliable tool for decoding Morse code messages encoded in bird sounds.

## Usage
To use AviaryMorse, follow these steps:

1. **Training the Model**: 
   - Collect audio clips of bird sounds representing Morse code dot and dash.
   - Train the model using the provided training script or your preferred machine learning framework.

2. **Decoding Morse Code**:
   - Obtain a full audio clip containing the Morse code message encoded in bird sounds.
   - Feed the audio clip into the trained model.
   - The model will identify the bird sounds as dots and dashes, and decode the Morse code message.

## Requirements
- Python3
- Audio processing libraries (Librosa,...)


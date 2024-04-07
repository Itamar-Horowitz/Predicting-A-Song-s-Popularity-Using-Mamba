# Spotify Popularity Prediction with Mamba Model
Predicting a song's popularity based on the most popular songs on Spotify using Mamba architecure. The dataset used is a Spotify Audio Features dataset.

Based on the paper:

James Pham, Edric Kyauk, Edwin Park [Predicting Song Popularity](https://cs230.stanford.edu/files_winter_2018/projects/6970963.pdf)

Video:

[YouTube](https://youtu.be/i8Cnas7QrMc) - https://youtu.be/i8Cnas7QrMc

![spotify](https://github.com/Rebeccaazoulay/DeepLearning_04621/assets/102752965/db7feed7-7c79-4d8f-9010-470095dd2196)


Github Link : (https://github.com/Rebeccaazoulay/DeepLearning_04621)

  * [Background](#background)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Dataset](#dataset)
  * [References](#references)

## Background
Predicting the popularity of songs is crucial for businesses aiming to remain competitive
in the ever-expanding music industry. Initial attempts to predict popularity using basic
machine learning techniques, including linear regression and logistic regression, yielded
modest results. Our project explores the various factors influencing song popularity by
utilizing a dataset comprising audio features and metadata for 4,771 tracks spanning the
last 50 years. Leveraging the Mamba architecture, a deep learning model customized for
long sequence modeling, our project aimed to enhance prediction accuracy. Surprisingly,
the Mamba architecture yielded similar results to linear regression, prompting further
investigation.

## Method
### Mamba
To enable handling long data sequences, Mamba incorporates the Structured State Space sequence model (S4).S4 can effectively and efficiently model long dependencies by combining the strengths of continuous-time, recurrent, and convolutional models, enabling it to handle irregularly sampled data, have unbounded context, and remain computationally efficient both during training and testing.

Mamba, building on the S4 model, introduces significant enhancements, particularly in its treatment of time-variant operations. Central to its design is a unique selection mechanism that adapts structured state space model (SSM) parameters based on the input. This enables Mamba to selectively focus on relevant information within sequences, effectively filtering out less pertinent data. The model transitions from a time-invariant to a time-varying framework, which impacts both the computation and efficiency of the system.

To address the computational challenges introduced by this time-variance, Mamba employs a hardware-aware algorithm. This algorithm enables efficient computation on modern hardware, like GPUs, by using kernel fusion, parallel scan, and recomputation. The implementation avoids materializing expanded states in memory-intensive layers, thereby optimizing performance and memory usage. The result is an architecture that is significantly more efficient in processing long sequences compared to previous methods.

Additionally, Mamba simplifies its architecture by integrating the SSM design with MLP blocks, resulting in a homogeneous and streamlined structure, furthering the model's capability for general sequence modeling across various data types, including language, audio, and genomics, while maintaining efficiency in both training and inference.

## Dataset
We constructed a comprehensive song dataset that contains a plethora of feature types for 4,771 tracks from the last 50 years. This dataset was compiled by aggregating 50 Spotify playlist IDs, representing the annual top 100 tracks over 50 years. Through the use of Spotipy, Spotify’s web API, we were able to retrieve detailed audio features and metadata for each track. Those audio features are number-type features such as the general loudness or acousticness of a song and the metadata are string-type features such as song name, song id and the names of artists. We divided the dataset so that 80\% of the tracks were used for training and 20\% were used for testing. Additionally, normalization procedures were applied to the features with a normal distributionfeatures.

## Model Architecture
<img width="320" alt="Mamba_model" src="https://github.com/Rebeccaazoulay/Predicting-a-song-s-popularity-using-Mamba/assets/164641099/d78c8f96-1040-44ca-b8a6-80ec6d9325f0">



## Results


## Prerequisites

- Python 3.x
- PyTorch
- scikit-learn
- matplotlib
- mamba_ssm
- pandas
- numpy

## Installation

To install the necessary dependencies, run:
pip install mamba_ssm

## Usage

1. Clone the repository:
git clone https://github.com/your_username/spotify-popularity-prediction.git

2. Navigate to the project directory:
cd spotify-popularity-prediction

3. Run the provided Python script:
python train_model.py

This script trains the Mamba model on the Spotify dataset, performs hyperparameter tuning, and evaluates the model's performance.

## Dataset

The dataset used for this project is the [Spotify Audio Features dataset], made of 4,471 songs which includes various audio features of Spotify songs such as acousticness, danceability, energy, tempo, etc.

## References
* https://cs230.stanford.edu/projects_fall_2020/reports/55822810.pdf
* https://cs229.stanford.edu/proj2015/140_report.pdf
* https://github.com/MattD82/Predicting-Spotify-Song-Popularity/blob/master/README.md
* https://github.com/twillstw/Spotify-Popularity-Prediction/tree/master
* https://towardsdatascience.com/song-popularity-predictor-1ef69735e380
  

# Spotify Popularity Prediction Using Mamba Model
Predicting a song's popularity based on the most popular songs on Spotify using Mamba architecure.

<p align="center">
  <img width="500" src="https://github.com/Itamar-Horowitz/Predicting-A-Song-s-Popularity-Using-Mamba/blob/main/Images/spotify.png">
</p>

Project Explanation Video (English): https://www.youtube.com/watch?v=d8VXnhX3pAo

## Table of Contents
  * [Background](#background)
  * [Dataset](#dataset)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
  * [References](#references)
  * 



## Background
Predicting the popularity of songs is crucial for businesses aiming to remain competitive in the ever-expanding music industry. Initial attempts to predict popularity using basic machine learning techniques, including linear regression and logistic regression, yielded modest results. Our project explores the various factors influencing song popularity by utilizing a dataset comprising audio features and metadata for 4,771 tracks spanning the last 50 years. Leveraging the Mamba architecture, a deep learning model customized for long sequence modeling, our project aimed to enhance prediction accuracy. Surprisingly, the Mamba architecture yielded similar results to linear regression, prompting further investigation.

### Mamba
To enable handling long data sequences, Mamba incorporates the Structured State Space sequence model (S4).S4 can effectively and efficiently model long dependencies by combining the strengths of continuous-time, recurrent, and convolutional models, enabling it to handle irregularly sampled data, have unbounded context, and remain computationally efficient both during training and testing.

Mamba, building on the S4 model, introduces significant enhancements, particularly in its treatment of time-variant operations. Central to its design is a unique selection mechanism that adapts structured state space model (SSM) parameters based on the input. This enables Mamba to selectively focus on relevant information within sequences, effectively filtering out less pertinent data. The model transitions from a time-invariant to a time-varying framework, which impacts both the computation and efficiency of the system.

To address the computational challenges introduced by this time-variance, Mamba employs a hardware-aware algorithm. This algorithm enables efficient computation on modern hardware, like GPUs, by using kernel fusion, parallel scan, and recomputation. The implementation avoids materializing expanded states in memory-intensive layers, thereby optimizing performance and memory usage. The result is an architecture that is significantly more efficient in processing long sequences compared to previous methods.

Additionally, Mamba simplifies its architecture by integrating the SSM design with MLP blocks, resulting in a homogeneous and streamlined structure, furthering the model's capability for general sequence modeling across various data types, including language, audio, and genomics, while maintaining efficiency in both training and inference.

## Dataset
For this project, we constructed a comprehensive song dataset that contains a plethora of feature types for 4,771 tracks from the last 50 years, which includes various audio features of Spotify songs such as acousticness, danceability, energy, tempo, etc. Here are some example songs from the dataset, without any preprocessing:

| artist_name   |  track_id               |track_name    | acousticness | danceability | duration_ms | energy | instrumentalness | key | liveness | loudness | mode  | speechiness | tempo   | time_signature | valence | popularity   |
|:-------------:|:-----------------------:|:-----------:|:------------:|:------------:|:-----------:|:------:|:----------------:|:---:|:--------:|:--------:|:-----:|:-----------:|:-------:|:--------------:|:-------:|:----------:|
| Ariana Grande  | 5D34wRmbFS29AjtTOP2QJe |   yes, and?   |    0.194     |    0.785     | 214994      | 0.766  | 7        |  1  |  0.107   | -6.551   |   1   |   0.0503    | 119.029 |        4       | 0.804   |    84      |
| Mitski  | 3vkCueOmm7xQDoJ17W1Pm3 |   My Love Mine All Mine   |   0.868    |    0.504     | 137773      | 0.308  | 0.135  |  9  |  0.158   | -14.958   |   1   |   0.0321    | 113.95 |        4       | 0.121   |    96      |
| Feid  | 7bywjHOc0wSjGGbj04XbVi |   LUNA   |   0.131   |    0.774     | 196800      | 0.86  | 0  |  7  |  0.116   | -2.888   |   0   |   0.13    | 100.019 |        4       | 0.446   |    95      |


We divided the dataset so that 80\% of the tracks were used for training and 20\% were used for testing. Additionally, normalization procedures were applied to the features with a normal distributionfeatures.

## Model Architecture
<img width="320" alt="Mamba_model" src="https://github.com/Rebeccaazoulay/Predicting-a-song-s-popularity-using-Mamba/assets/164641099/d78c8f96-1040-44ca-b8a6-80ec6d9325f0">



## Results


## Prerequisites
- Python
- PyTorch
- scikit-learn
- matplotlib
- mamba_ssm
- pandas
- numpy
- GPU

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

## References
* https://github.com/state-spaces/mamba
* https://cs230.stanford.edu/projects_fall_2020/reports/55822810.pdf
* https://cs229.stanford.edu/proj2015/140_report.pdf
* https://github.com/MattD82/Predicting-Spotify-Song-Popularity/blob/master/README.md
* https://github.com/twillstw/Spotify-Popularity-Prediction/tree/master
* https://towardsdatascience.com/song-popularity-predictor-1ef69735e380
  

# Glioma Tumor Detection
## About the data:
The data was mostly put together from various sources on Kaggle. You can find some of the references [here](https://www.kaggle.com/datasets/fernando2rad/brain-tumor-mri-images-44c?resource=download). The data has two folders `image` and `labels`. Each of which have their own corresponding `train` and `validation` sub folders.
## Motivation:
Glioma brain tumors, a type of tumor that originates in the glial cells of the brain, often pose a formidable challenge in early detection due to their ability to develop without causing immediate noticeable symptoms. These tumors can grow slowly and may go unnoticed in their initial stages, allowing them to reach advanced levels before clinical manifestations become apparent. The insidious nature of gliomas underscores the critical need for advanced diagnostic tools.

Recognizing this diagnostic gap and the potential consequences of delayed detection, I embarked on developing an AI model using YOLOv8 and PyTorch. By harnessing the strengths of deep learning and computer vision, I created a model that can accurately recognize intricate details and subtle variations in brain tissue, contributing to early and accurate glioma detection.
this model stands as a proactive measure to enhance early detection and contribute to more timely intervention strategies, ultimately improving outcomes for patients facing this challenging medical condition. I am constantly working to improve the model and expand the class list to detect other types of tumors in the future.
## Data Split:
#### The data was split in the following ways
1. 75% of data for training
2. 20% of data for validation
3. 5% of data for test
# Training & Results
### F1 Plot
![F1_curve](https://github.com/rk767/yolov8-tumor-detection/assets/48916019/bda20a46-3433-4867-a8a2-055eb16adc53)
### 
### Train Metrics
![results](https://github.com/rk767/yolov8-tumor-detection/assets/48916019/ec28ea6c-3501-4035-821e-75a1175611f8)

# Getting Started
## Prerequisites
* [Python 3.11.5](https://www.python.org/downloads/release/python-3115/)
* NodeJS 20+
## Clone Repo (Requires Github CLI)
```
gh repo clone rk767/yolov8-tumor-detection
```

## Install Dependencies
```
npm i
```
```
pip install -r requirements.txt
```
## Run app.py and open local host in browser
```
localhost:8080
```

> [!NOTE] 
>* The TensorRT installation is quite a long process and therefore will not be documented here. Refer to the [docs](https://docs.nvidia.com/deeplearning/tensorrt/) for more information.
### TensorRT requirements (Only required for building & running the quantized model)
* cuDNN 8.9.0
* TensorRT 8.6.1.6
* Cuda Toolkit 11.8

[Colab Notebook](https://colab.research.google.com/drive/1OXmuHMKsWz3GRa-o-JUUcwqK-N1Plud6?usp=sharing)

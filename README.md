# CliniScan-Lung-Abnormality-Detection-on-Chest-Xrays-using-AI
This project aims to develop an AI-based system to detect and localize lung abnormalities in chest X-ray images using deep learning. Trained on the VinDr-CXR dataset, it identifies pathologies such as opacities, fibrosis, and masses, assisting radiologists with accurate, interpretable, and clinically relevant diagnostic support.

# Dataset

VinDr-CXR Dataset

Large-scale, expert-annotated chest X-ray dataset

DICOM images with bounding box annotations

Supports both classification and object detection tasks

# Technologies Used

Python,NumPy, Pandas ,OpenCV, Matplotlib,pydicom ,PyTorch (torch, torch.nn, torch.optim) ,torchvision.models,Ultralytics YOLOv8 ,os, shutil

# Workflow Summary
# 1. Data Preparation

-Loaded DICOM images using pydicom

-Converted images to PNG/JPG format

-Cleaned annotation files and removed invalid samples

# 2. Image Preprocessing

-Resized images to standard dimensions

-Applied normalization and intensity standardization

-Enhanced contrast using CLAHE

-Reduced noise using filtering techniques

# 3. Annotation Processing

-Parsed bounding box annotations from CSV files

-Converted annotations to YOLO-compatible format

-Organized dataset into structured directories

# 4. Dataset Splitting

-Patient-wise split to avoid data leakage

-Training, validation, and testing sets created

# Classification Model

-Implemented using transfer learning (ResNet, DenseNet, EfficientNet)

-Applied data augmentation to improve generalization

-Evaluated using accuracy, precision, recall, F1-score, and ROC-AUC

-Final model saved for inference and deployment

# Detection Model

-Implemented using YOLOv8

-Trained to localize lung abnormalities with bounding boxes

-Evaluated using mAP and loss metrics

-Model validated on unseen chest X-ray images

# Interpretability

-Grad-CAM used to visualize regions influencing predictions

-Helps ensure predictions focus on clinically relevant areas

# Streamlit Deployment

-Developed a Streamlit web application for real-time inference

-Allows image upload and displays predictions with bounding boxes

-Supports visualization of model outputs for demonstration and prototyping

# Final Outcome

-The project delivers a reliable and interpretable AI system for lung abnormality detection and localization, suitable for research, clinical support, and deployment-oriented applications.

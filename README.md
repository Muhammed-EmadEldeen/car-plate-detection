# Car License Plate Detection and Text Recognition

## Overview
This project focuses on detecting license plates in images and extracting the alphanumeric characters from them. It has various practical applications, with one notable example being surveillance cameras for monitoring public streets.

## Getting Started
To use this project, follow these simple steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.

```
git clone https://github.com/Muhammed-EmadEldeen/car-plate-detection.git;
cd car-license-plate-detection;
cd main 
```
Run the license_text_recognize.py script.

```
python license_text_recognize.py
```
When prompted, enter the path to the image you want to process.

## Project Development

Here's a summary of the key steps in developing this project:

1. Data Acquisition: I collected a high-quality dataset from Roboflow to train the license plate detection model.

2. Model Training: The YOLOv8 model was trained using Google Colab. You can find the training notebook here [Link](https://colab.research.google.com/drive/1fs0aoH9PVJy9tPIHfYjsw87U3awvyg2N?usp=sharing).

3. Model Deployment: After training, the model was downloaded from the cloud and prepared for use.

4. Image Processing: OpenCV was employed to process images, identify license plates, and crop them from the original images.

5. Text Recognition: The Tesseract library was utilized for Optical Character Recognition (OCR) to extract letters and numbers from the license plates.

Feel free to explore the codebase for more details on each step of the project.

### Dependencies

* Python 3.6+
* OpenCV
* Tesseract
* YOLOv8


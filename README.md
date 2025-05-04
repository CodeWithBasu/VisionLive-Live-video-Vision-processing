# Simple Object Detection with MobileNet-SSD

This project uses OpenCV and the MobileNet-SSD neural network to perform real-time object detection through your webcam. It can detect 20 common object classes and categorize them.

## Features

- Real-time object detection using MobileNet-SSD
- Detection of 20 common object classes
- FPS (Frames Per Second) counter
- Object categorization (electronics, furniture, vehicles, animals, household)
- Simple and easy to use interface

## Requirements

- Python 3.x
- OpenCV
- NumPy
- imutils

## Installation

1. Install the required packages:
   ```
   pip install opencv-python numpy imutils
   ```

2. Make sure you have the model files in the project directory:
   - MobileNetSSD_deploy.prototxt
   - MobileNetSSD_deploy (1).caffemodel

## Usage

Run the script:
```
python main.py
```

### Controls

- Press `Esc` to exit the application

## How It Works

1. The webcam feed is processed frame by frame
2. Each frame is resized and passed through the MobileNet-SSD neural network
3. Objects with confidence above the threshold (0.25) are identified and highlighted
4. Categories of detected objects are displayed at the bottom of the screen
5. FPS is shown in the top-left corner

## Detectable Objects

The model can detect the following 20 object classes:
- background
- aeroplane
- bicycle
- bird
- boat
- bottle
- bus
- car
- cat
- chair
- cow
- diningtable
- dog
- horse
- motorbike
- person
- pottedplant
- sheep
- sofa
- train
- tvmonitor

## Notes

- The accuracy of detection depends on lighting conditions and camera quality
- The confidence threshold can be adjusted in the code to balance between detection accuracy and false positives 
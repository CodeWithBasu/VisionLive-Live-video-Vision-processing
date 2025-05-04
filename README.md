# **📷 Real-Time Object Detection:**

A lightweight yet powerful real-time object detection system leveraging MobileNet-SSD and OpenCV. Designed for developers, students, and AI enthusiasts to explore deep learning applications in computer vision through live webcam feeds.

---

## 🚀 Features

* ⚡ Fast and accurate object detection using pre-trained **MobileNet-SSD**
* 🏷️ Displays object class names and confidence scores
* 📈 Real-time FPS (Frames Per Second) counter for performance tracking
* 🎯 Color-coded bounding boxes for intuitive visualization

---

## 📦 Requirements

Ensure you have Python 3.6 or above installed. Then install the dependencies:

```bash
pip install numpy opencv-python imutils
```

---

## 🛠️ Installation

Set up the project in just a few steps:

```bash
git clone https://github.com/CodeWithBasu/VisionLive-Live-video-Vision-processing.git
cd VisionLive-Live-video-Vision-processing

# Download and place the following files in the root directory:
# - MobileNetSSD_deploy.prototxt
# - MobileNetSSD_deploy.caffemodel

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

> 📌 Ensure your webcam is connected and accessible.

---

## 🔧 Model Setup

Download the model architecture and weights from the official repository:

* [MobileNetSSD\_deploy.prototxt](https://github.com/chuanqi305/MobileNet-SSD/blob/master/MobileNetSSD_deploy.prototxt)
* [MobileNetSSD\_deploy.caffemodel](https://github.com/chuanqi305/MobileNet-SSD/blob/master/MobileNetSSD_deploy.caffemodel)

Place both files in your project root. Rename the `.caffemodel` if necessary to match the expected filename: `MobileNetSSD_deploy.caffemodel`

---

## ▶️ Running the Application

To start object detection:

```bash
python main.py
```

* The live camera feed will open with detected objects highlighted.
* Press `Esc` to terminate the session.

---

## 🔍 Live Output Highlights

* 🟩 Bounding boxes for detected objects
* 🧾 Labels with object names and confidence percentages
* ⏱ Real-time FPS counter displayed on the screen

---

## 🌟 Future Enhancements

* 🚀 Upgrade to YOLOv8 or EfficientDet for better speed and accuracy
* 🔊 Integrate voice-based alerts for detected classes
* 🖥️ Add GUI support for toggling model settings in real-time
* 📊 Implement data logging or video recording features

---

## 👤 Author

**Basudev**
Computer Science Enthusiast | Passionate about AI, Python, and Computer Vision

---

## 📄 License

Distributed under the [MIT License](LICENSE). Use it freely for personal or commercial projects.

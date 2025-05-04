import numpy as np
import cv2
import imutils
import time

# Path to model files
prototxt = "MobileNetSSD_deploy.prototxt"
model = "MobileNetSSD_deploy (1).caffemodel"
confThresh = 0.25  # Confidence threshold

# Classes that the model was trained on
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]  # Fixed "tvmonitor" class

# Simple categories for objects
CATEGORIES = {
    "electronics": ["tvmonitor"],
    "furniture": ["chair", "sofa", "diningtable"],
    "vehicles": ["car", "bus", "motorbike", "bicycle", "train", "aeroplane", "boat"],
    "animals": ["cat", "dog", "bird", "cow", "sheep"],
    "household": ["bottle", "pottedplant"]
}

# Generate consistent colors for all classes
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("Loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt, model)

print("Model Loaded Successfully")
print("Starting Camera Feed...")

# Open the camera
vs = cv2.VideoCapture(0)
time.sleep(2.0)  # Wait for camera to initialize

# FPS tracking
frame_count = 0
fps_start_time = time.time()
fps = 0

while True:
    # Read a frame from the camera
    ret, frame = vs.read()
    if not ret:
        print("Failed to grab frame")
        break
        
    # Calculate FPS
    frame_count += 1
    if frame_count >= 10:  # Calculate FPS every 10 frames
        fps = frame_count / (time.time() - fps_start_time)
        fps_start_time = time.time()
        frame_count = 0

    # Resize the frame for processing
    frame = imutils.resize(frame, width=1000)
    (h, w) = frame.shape[:2]

    # Create a blob from the frame and pass it through the network
    resized_frame = cv2.resize(frame, (300, 300))
    blob = cv2.dnn.blobFromImage(resized_frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()
    
    # Store detected objects for category analysis
    detected_objects = []

    # Process each detection
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections
        if confidence > confThresh:
            idx = int(detections[0, 0, i, 1])
            if idx < len(CLASSES):  # Ensure index is valid
                class_name = CLASSES[idx]
                detected_objects.append(class_name)
                
                # Get the bounding box coordinates
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # Display class name and confidence
                label = f"{class_name}: {confidence * 100:.2f}%"
                cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
                
                # Add label at the top of bounding box
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    
    # Display FPS on frame
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Add category information if objects are detected
    if detected_objects:
        # Find categories that have detected objects
        categories = []
        for category, objects in CATEGORIES.items():
            if any(obj in detected_objects for obj in objects):
                categories.append(category)
        
        if categories:
            category_text = "Categories present: " + ", ".join(categories)
            cv2.putText(frame, category_text, (10, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Show the output frame
    cv2.imshow("Object Detection", frame)
    
    # Handle key presses
    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit
        break

# Clean up
vs.release()
cv2.destroyAllWindows()

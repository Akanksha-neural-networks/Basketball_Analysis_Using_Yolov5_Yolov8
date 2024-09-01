# Basketball_Analysis_Using_Yolov5_Yolov8

# Explanation for YOLOv5 Code

<b>YOLOv5 Overview:</b> YOLOv5, is a sophisticated object detection system renowned for its accuracy and quickness. Instead of sifting through different areas of the image, it processes the full image at once to detect things in real time. YOLOv5 is widely utilized in real-world applications such as autonomous driving and video surveillance since it is simple to deploy.

<b>Code Explanation (YOLOv5): </b>
<b>Installation: </b> 
To start, the libraries for deep learning and image processing are installed: torch, torchvision, and opencv-python. To use the trained model, a clone of the YOLOv5 GitHub repository is created.
<b>Model Loading: </b>
The pre-trained YOLOv5s (small version) model is loaded from the Ultralytics GitHub repository using the torch.hub.load() function.
<b>Video Processing: </b>
OpenCV's cv2 is used to capture the input video.Use VideoCapture(). Basic video metadata is extracted, including frame rate (FPS), frame width, and frame height.
<b>Object Detection: </b>
Processing is done on the video frame by frame. The YOLOv5 model finds items in each frame and provides the names and bounding box coordinates. This label (label 32) identifies basketballs. The discovered object is surrounded by a rectangle, and the frame shows the object's confidence score.
<b>Frame Display: </b>
Using cv2.cvtColor(), each processed frame is converted to RGB for display in a Jupyter notebook. It is then saved as an image and shown using IPython.display in the notebook.

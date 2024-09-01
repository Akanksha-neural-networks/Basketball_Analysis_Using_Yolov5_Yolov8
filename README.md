# Basketball_Analysis_Using_Yolov5_Yolov8

# Explanation for YOLOv5 Code

<b>YOLOv5 Overview:</b> YOLOv5, is a sophisticated object detection system renowned for its accuracy and quickness. Instead of sifting through different areas of the image, it processes the full image at once to detect things in real time. YOLOv5 is widely utilized in real-world applications such as autonomous driving and video surveillance since it is simple to deploy.

<b>Code Explanation (YOLOv5):</b>

<b>Installation:</b> First, torch, torchvision, and opencv-python libraries are installed to handle deep learning and image processing tasks. The YOLOv5 GitHub repository is cloned to use the pre-trained model.

<b>Model Loading:</b> The torch.hub.load() function is used to load the pre-trained YOLOv5s (small version) model from the Ultralytics GitHub repository.

<b>Video Processing:</b> The input video is captured using OpenCV’s cv2.VideoCapture(). Basic information about the video, such as frames per second (FPS), width, and height of the frames, is extracted.

<b>Object Detection:</b> The video is processed frame-by-frame. For each frame, the YOLOv5 model detects objects and returns the bounding box coordinates and labels. Here, basketballs are identified (label 32). A rectangle is drawn around the detected object, and its confidence score is displayed on the frame.

<b>Frame Display:</b> Each processed frame is converted to RGB for display in a Jupyter notebook using cv2.cvtColor() and then saved as an image, which is displayed in the notebook using IPython.display.

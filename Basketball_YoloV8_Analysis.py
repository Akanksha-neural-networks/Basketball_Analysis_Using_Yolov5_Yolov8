#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ultralytics')


# In[2]:


import torch
import cv2
from ultralytics import YOLO
from IPython.display import display, Image


# In[3]:


model = YOLO('yolov8s.pt')


# In[4]:


video_path = 'InputVideo.mp4'
cap = cv2.VideoCapture(video_path)


# In[5]:


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# In[ ]:


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)  

    for result in results:
        boxes = result.boxes.xyxy  
        confidences = result.boxes.conf  
        labels = result.boxes.cls  

        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box)
            conf = confidences[i]
            label = int(labels[i])

            if label == 32:  
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, f'Basketball {conf:.2f}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    img_path = 'current_frame.jpg'
    cv2.imwrite(img_path, frame_rgb)
    display(Image(filename=img_path))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:





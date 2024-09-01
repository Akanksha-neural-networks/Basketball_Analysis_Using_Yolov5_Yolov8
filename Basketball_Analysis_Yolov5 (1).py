#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install torch torchvision opencv-python')


# In[2]:


get_ipython().system('git clone https://github.com/ultralytics/yolov5')
get_ipython().system('cd yolov5')


# In[3]:


import torch
import cv2


# In[4]:


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


# In[5]:


video_path = 'InputVideo.mp4'
cap = cv2.VideoCapture(video_path)


# In[6]:


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# In[ ]:


from IPython.display import display, Image
import numpy
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    labels, cords = results.xyxyn[0][:, -1].cpu().numpy(), results.xyxyn[0][:, :-1].cpu().numpy()
    for i in range(len(labels)):
        if labels[i] == 32:
            x1, y1, x2, y2, conf = cords[i]
            x1, y1, x2, y2 = int(x1 * width), int(y1 * height), int(x2 * width), int(y2 * height)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f'Basketball {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_path = 'current_frame.jpg'
    cv2.imwrite(img_path, frame_rgb)
    display(Image(filename=img_path))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


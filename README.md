# 📌 Project Overview

Dental diseases detection is an important step toward automated dental diagnosis.  
In this project, we use a deep learning-based object detection model (YOLOv8) to identify and classify dental conditions from augmented dataset images.

## 🎯 Detected Classes

Healthy Teeth  
Caries  
Impacted Teeth  
Broken Down / Crow Root  
Infection  
Fractured Teeth  

---

## ⚙️ Installation

Clone the repository and install dependencies:
```Bash
git clone https://github.com/your-username/dental-caries-detection-yolov8.git
```
```Bash
cd dental-caries-detection-yolov8  
```  
```Bash
pip install -r requirements.txt  
```
## 📦 Requirements  

opencv-python  
matplotlib  
ultralytics  

---

## 🚀 Training the Model  

To train YOLOv8 on your dataset:  

```Bash  
python train.py  
```
---

## 🧠 Training Configuration  

```Python  
model = YOLO("yolov8n.pt")  

model.train(  
    data="data.yaml",  
    epochs=50,  
    imgsz=640,  
    batch=16  
)  
```
---

## 🔍 Inference (Prediction)  

Run inference on test images:  

```Bash  
python src/predict.py  
```
---

## 📌 Prediction Code  

```Python  
model = YOLO("../models/best.pt")  

model.predict(  
    source="Augmented_Data/test/images",  
    conf=0.25,  
    save=True  
)  
```
Output results will be saved automatically in the runs/ directory.  

---

## 📊 Visualization of Results  

To visualize random prediction results:  

```Bash  
python visualize_prediction.py  
```
This script:  
- Loads random predicted images from demo/  
- Displays them using Matplotlib  
- Prints image path  

---

## 🗂 Dataset Configuration (data.yaml)  

```YAML  
path: Augmented_Data  

train: train/images  
val: valid/images  
test: test/images  

names:  
  0: Healthy_Teeth  
  1: Caries  
  2: Impacted_Teeth  
  3: Broken_Down_Crow_Root  
  4: Infection  
  5: Fractured_Teeth  
```
---

## 🧪 Results  

After training, the best model weights are saved at:  

models/best.pt  

Predictions are stored in:  

runs/detect/predict/  

---

## 🚫 .gitignore Highlights  

This project ignores:  
- Python cache files  
- YOLO output runs  
- Model weights (.pt, .pth)  
- System files  
- Logs  

---

## ⚠️ Disclaimer

This project is an experimental and demo-level implementation for educational and research purposes only.  
It is **not intended for real clinical or medical use** and should not be relied upon for professional dental diagnosis or treatment decisions.

---
## 👨‍💻 Author  

Developed using Ultralytics YOLOv8 for educational and research purposes.  





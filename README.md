در ادامه یک فایل README.md حرفه‌ای، مهندسی و مناسب برای پروژه YOLOv8 شما آماده کرده‌ام. طوری نوشته شده که هم برای GitHub جذاب باشد و هم برای رزومه قابل ارائه 👇


---

# 🦷 Dental Caries Detection using YOLOv8

This project implements an object detection system for dental diseases using YOLOv8 (Ultralytics).  
The model is trained to detect multiple dental conditions from images, including caries, fractures, infections, and impacted teeth.

---

## 📌 Project Overview

Dental diseases detection is an important step toward automated dental diagnosis.  
In this project, we use a deep learning-based object detection model (YOLOv8) to identify and classify dental conditions from augmented dataset images.

### 🎯 Detected Classes

- Healthy Teeth  
- Caries  
- Impacted Teeth  
- Broken Down / Crow Root  
- Infection  
- Fractured Teeth  

---

## 📁 Project Structure

dental-caries-detection-yolov8/ │ ├── demo/                     # Output prediction images ├── models/ │   └── best.pt               # Trained YOLOv8 model weights │ ├── src/ │   └── predict.py           # Inference script │ ├── train.py                 # Training script ├── visualize_prediction.py  # Random result visualization ├── data.yaml                # Dataset configuration ├── requirements.txt        # Dependencies ├── .gitignore └── README.md

---

## ⚙️ Installation

Clone the repository and install dependencies:

`bash
git clone https://github.com/your-username/dental-caries-detection-yolov8.git
cd dental-caries-detection-yolov8

pip install -r requirements.txt


---

📦 Requirements

opencv-python
matplotlib
ultralytics


---

🚀 Training the Model

To train YOLOv8 on your dataset:

python train.py

🧠 Training Configuration

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)


---

🔍 Inference (Prediction)

Run inference on test images:

python src/predict.py

📌 Prediction Code

model = YOLO("../models/best.pt")

model.predict(
    source="Augmented_Data/test/images",
    conf=0.25,
    save=True
)

Output results will be saved automatically in the runs/ directory.


---

📊 Visualization of Results

To visualize random prediction results:

python visualize_prediction.py

This script:

Loads random predicted images from demo/

Displays them using Matplotlib

Prints image path



---

🗂 Dataset Configuration (data.yaml)

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


---

🧪 Results

After training, the best model weights are saved at:

models/best.pt

Predictions are stored in:

runs/detect/predict/


---

🚫 .gitignore Highlights

This project ignores:

Python cache files

YOLO output runs

Model weights (.pt, .pth)

System files

Logs



---

📌 Future Improvements

Improve dataset balance

Use YOLOv8m/l for higher accuracy

Add real-time webcam detection

Deploy model using Flask / FastAPI

Add web UI for dental diagnosis



---

👨‍💻 Author

Developed using Ultralytics YOLOv8 for educational and research purposes.


---

⭐ If you like this project

Give it a star ⭐ on GitHub to support further improvements.

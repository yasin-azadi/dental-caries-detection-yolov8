from ultralytics import YOLO

model = YOLO("../runs/detect/train/weights/best.pt")

model.predict(
    source="Augmented_Data/test/images",
    conf=0.25,
    save=True
)
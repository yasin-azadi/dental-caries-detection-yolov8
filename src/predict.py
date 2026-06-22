from ultralytics import YOLO

model = YOLO("models/best.pt")

model.predict(
    source="Augmented_Data/test/images",
    conf=0.25,
    save=True
)

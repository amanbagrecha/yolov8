from ultralytics import YOLO


model = YOLO("runs/detect/train/weights/best.pt")
model.predict(source="datasets/images/test/1.png", save=True)

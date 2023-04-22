from ultralytics import YOLO


model = YOLO("yolov8n.pt")
model.train(data="dataset.yaml", imgsz=(640, 640), epochs=3)

from ultralytics import YOLO


model = YOLO("yolov8s.pt")
model.train(data="dataset.yaml", imgsz=(640, 640), epochs=10)

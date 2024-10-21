from ultralytics import YOLO

model = YOLO('yolov10n.pt')

model.train(data="custom_data.yaml", epochs=100, batch=16)
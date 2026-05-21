from ultralytics import YOLO

model = YOLO("runs/detect/detect_coffe/weights/best.pt")

result = model.predict(
    source="input_images",
    conf=0.25,
    save=True,
    show=False,
    project="output",
    exist_ok=True
)

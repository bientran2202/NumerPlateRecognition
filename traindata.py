if __name__ == '__main__':
    from ultralytics import YOLO

    model = YOLO('../Yolo-Weights/yolov8l.pt')
    results = model.train(data='data.yaml', epochs=1, imgsz=640, device=0)

# Create a new YOLO model fro   m scratch
# model = YOLO('../Yolo-Weights/yolov8l.pt')
#
# # Train the model using the 'data.yaml' dataset for 1 epoch
# results = model.train(data='data.yaml', epochs=1, imgsz=640, device=0)

# # Evaluate the model's performance on teh validation set
# results = model.val()
#
# # Perform object detection on a imange using the model
# results = model('https://oto360.net/images/bai-viet/a_164337.jpg')

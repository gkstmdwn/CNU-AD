from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(data = 'D:\Data\SignLanguage MNIST\sign_mnist_train', epochs=100)
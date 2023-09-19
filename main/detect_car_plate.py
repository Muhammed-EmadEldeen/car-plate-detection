import cv2 as cv
from ultralytics import YOLO


def return_sliced_images(model,img_path):
    img = cv.imread(img_path)
    car_plate_rectangles = detect_car_plate_images(model,img)
    sliced_images = []
    for rect in car_plate_rectangles:
        sliced_images.append(img[int(rect[1].item()):int(rect[3].item()),int(rect[0].item()):int(rect[2].item())])
    return sliced_images



def detect_car_plate_images(model,image):
    rectangles = []
    results = model(image)
    for box in results[0].boxes:
        if int(box.cls[0].item()) == 1:
            rectangles.append(box.xyxy[0])
    return rectangles




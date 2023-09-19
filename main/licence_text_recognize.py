from detect_car_plate import return_sliced_images
from ultralytics import YOLO
import pytesseract
import cv2


model = YOLO('../model/best.pt')
img = '../assets/grouped/Cars64.png'

images = return_sliced_images(model,img)
for image in images:
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    cv2.imshow('img',image)
    print(pytesseract.image_to_string(img_rgb))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

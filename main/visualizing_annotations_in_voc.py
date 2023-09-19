import cv2 as cv
import numpy as np
import os
import xml.dom.minidom

img  = cv.imread('../assets/images/Cars8.png')
xml_path = '../assets/annotations/Cars8.xml'

dom = xml.dom.minidom.parse(xml_path)
root = dom.documentElement
objects = root.getElementsByTagName('object')


for object in objects:
    bndbox = object.getElementsByTagName('bndbox')[0]
    xmin = int(bndbox.getElementsByTagName('xmin')[0].childNodes[0].data)
    ymin = int(bndbox.getElementsByTagName('ymin')[0].childNodes[0].data)
    xmax = int(bndbox.getElementsByTagName('xmax')[0].childNodes[0].data)
    ymax = int(bndbox.getElementsByTagName('ymax')[0].childNodes[0].data)
    cv.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
    name = object.getElementsByTagName('name')[0].childNodes[0].data



cv.imshow('Image', img)

cv.waitKey(0)


import os
import xml.dom.minidom


def get_coordinates(xml_path):
    dom = xml.dom.minidom.parse(xml_path)
    root = dom.documentElement
    objects = root.getElementsByTagName('object')
    current_size = root.getElementsByTagName('size')[0]
    width = int(current_size.getElementsByTagName('width')[0].childNodes[0].data)
    height = int(current_size.getElementsByTagName('height')[0].childNodes[0].data)
    current_object = objects[0]


    bndbox = current_object.getElementsByTagName('bndbox')[0]
    xmin = int(bndbox.getElementsByTagName('xmin')[0].childNodes[0].data)
    ymin = int(bndbox.getElementsByTagName('ymin')[0].childNodes[0].data)
    xmax = int(bndbox.getElementsByTagName('xmax')[0].childNodes[0].data)
    ymax = int(bndbox.getElementsByTagName('ymax')[0].childNodes[0].data)

    return (xmin, ymin, xmax, ymax, width, height )

def create_new_coordinate(xmin, ymin, xmax, ymax,img_width, img_height ):
    width = (xmax - xmin)/img_width
    height = (ymax - ymin)/img_height
    x_center = (xmin + xmax)/(2*img_width)
    y_center = (ymin + ymax)/(2*img_height)

    return (x_center, y_center, width, height)


def create_annotation_txt(xml_path, txt_path):
    coordinates = get_coordinates(xml_path)
    new_coordinates = create_new_coordinate(*coordinates)

    with open(txt_path, 'w') as f:
        f.write(f'0 {new_coordinates[0]} {new_coordinates[1]} {new_coordinates[2]} {new_coordinates[3]}')
        # 0 here for class id


for annot in os.listdir('../assets/annotations/'):
    xml_path = os.path.join('../assets/annotations/', annot)
    txt_path = os.path.join('../assets/annotations_txt/', annot[:-4] + '.txt')
    create_annotation_txt(xml_path, txt_path)


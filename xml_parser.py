import xml.etree.ElementTree as ET
import numpy as np

def retrieve_data(xml_file):
    mytree = ET.parse(xml_file)
    myroot = mytree.getroot()

    image_data = {}

    # Image Class
    foo = myroot[6]
    name = foo[0].text

    # Image Distance
    folder = myroot[0].text

    # Image Size
    size = myroot[4]
    width, height = int(size[0].text), int(size[1].text)

    # Bounding Box location
    object_ = myroot[6]
    bndbox = object_[4]
    xmin, ymin, xmax, ymax = int(bndbox[0].text), int(bndbox[1].text), int(bndbox[2].text), int(bndbox[3].text)   

# Calculate necessary measurements
    box_width = xmax - xmin
    box_height = ymax - ymin
    box_diagonal = np.sqrt(np.square(box_width) + np.square(box_height))
    image_diagonal = np.sqrt(np.square(width) + np.square(height))

    # Fill the dictionary to be returned
    image_data['class'] = name

    image_data['width'] = width
    image_data['height'] = height

    image_data['box_width'] = float(box_width / width)
    image_data['box_height'] = float(box_height / height)
    image_data['box_diagonal'] = np.round(box_diagonal, 1) / image_diagonal
    
    image_data['distance'] = int(folder)
    return image_data

'''All values needed for pre-processing we now have from the .xml files'''


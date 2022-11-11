import xml.etree.ElementTree as ET
import numpy as np

def retrieve_data(xml_file):
    mytree = ET.parse(xml_file)
    myroot = mytree.getroot()

    image_data = {}

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

    # Fill the dictionary to be returned
    image_data[width] = width
    image_data[height] = height

    image_data[box_width] = box_width
    image_data[box_height] = box_height
    image_data[box_diagonal] = box_diagonal
    
    return image_data

'''All values needed for pre-processing we now have from the .xml files'''

import xml_parser as parser

# DisNET architecture
import pathlib
import numpy as np
import glob
import shutil
import PIL.Image
import pandas as pd

# Import opencv
import cv2 

# Import uuid
import uuid

# Import Operating System
import os

import matplotlib.pyplot as plt

# Training and Test paths
TRAIN_PATH = os.path.join('data', 'train')
TEST_PATH = os.path.join('data', 'test')

FULL_PATH = os.getcwd()

train_dir = os.path.join(FULL_PATH, TRAIN_PATH)
test_dir = os.path.join(FULL_PATH, TEST_PATH)

train_dir = pathlib.Path(train_dir)
test_dir = pathlib.Path(test_dir)

train_xml_files = list(train_dir.glob('*.xml'))
test_xml_files = list(test_dir.glob('*.xml'))

'''
Averages of Soldering box and Expo box
soldering box:
    height: 3.079
    width: 2.619
    breadth: 2.619

Expo box :
    height: 4.928
    width: 3.084
    breadth: 2.241
'''
soldering_stats = {'height': 3.079, 'width': 2.619, 'breadth': 2.619}
expo_stats = {'height': 4.928, 'width': 3.084, 'breadth': 2.241}

box_widths = []
box_heights = []
box_diagonals = []

class_height = []
class_width = []
class_depth = []

distances = []

for xml_file in train_xml_files:
    print(xml_file)
    temp_map = parser.retrieve_data(xml_file)
    box_widths.append(temp_map['box_width'])
    box_heights.append(temp_map['box_height'])
    box_diagonals.append(temp_map['box_diagonal'])
    distances.append(temp_map['distance'])

    # Class characteristics
    if temp_map['class'] == 'soldering_box':
        class_height.append(soldering_stats['height'])
        class_width.append(soldering_stats['width'])         
        class_depth.append(soldering_stats['breadth']) 
    else:
        class_height.append(expo_stats['height'])
        class_width.append(expo_stats['width'])         
        class_depth.append(expo_stats['breadth']) 

for xml_file in test_xml_files:
    temp_map = parser.retrieve_data(xml_file)
    box_widths.append(temp_map['box_width'])
    box_heights.append(temp_map['box_height'])
    box_diagonals.append(temp_map['box_diagonal'])
    distances.append(temp_map['distance'])

    # Class characteristics
    if temp_map['class'] == 'soldering_box':
        class_height.append(soldering_stats['height'])
        class_width.append(soldering_stats['width'])         
        class_depth.append(soldering_stats['breadth']) 
    else:
        class_height.append(expo_stats['height'])
        class_width.append(expo_stats['width'])         
        class_depth.append(expo_stats['breadth']) 

widths = pd.Series(box_widths)
heights = pd.Series(box_heights)
diagonals = pd.Series(box_diagonals)
distances = pd.Series(distances)

class_heights = pd.Series(class_height)
class_widths = pd.Series(class_width)
class_depths = pd.Series(class_depth)

frame = {'box_width': widths, 'box_height': heights, 'box_diagonal': diagonals, 'class_height': class_heights, 'class_width': class_widths, 'class_depths': class_depths, 'distance': distances}

result = pd.DataFrame(frame)
print(result)
result.to_csv('output.csv', index=False)





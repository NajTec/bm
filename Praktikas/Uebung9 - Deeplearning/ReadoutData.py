# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:22:06 2019

@author: emb-lab
"""

import cv2
import os
from tqdm import tqdm

PATH_TO_X_TRAIN_DATA  = "E:/bm-labor/Uebung9 - Deeplearning/UnetData/images/"
PATH_TO_Y_TRAIN_DATA = "E:/bm-labor/Uebung9 - Deeplearning/UnetData/Masks/"

PATH_TO_X_VAL_DATA = "E:/bm-labor/Uebung9 - Deeplearning/UnetData/imagesValidation/"
PATH_TO_Y_VAL_DATA = "E:/bm-labor/Uebung9 - Deeplearning/UnetData/MasksValidation/"


# get filenames for training data
training_data = os.listdir(PATH_TO_X_TRAIN_DATA)

#get all filenames for validation data
validation_data = os.listdir(PATH_TO_X_VAL_DATA)

x_train = []
y_train = []

x_val = []
y_val = []

# Loop for loading training data in RAM
for filename in tqdm(training_data):

    x_img = cv2.imread(PATH_TO_X_TRAIN_DATA + filename)
    if x_img is None:
        print("No Input image loaded!",filename)
        raise ValueError("No pic found!")
    y_img = cv2.imread(PATH_TO_Y_TRAIN_DATA + filename)

    x_train.append(x_img)
    y_train.append(y_img)

# Loop for loading validation data in RAM
for filename in tqdm(validation_data):

    x_img = cv2.imread(PATH_TO_X_VAL_DATA + filename)
    if x_img is None:
        print("No Input image loaded!",filename)
        raise ValueError("No pic found!")
    y_img = cv2.imread(PATH_TO_Y_VAL_DATA + filename)

    x_val.append(x_img)
    y_val.append(y_img)
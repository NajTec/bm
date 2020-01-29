# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:22:06 2019

@author: emb-lab
"""

import cv2
import os
from tqdm import tqdm
import numpy as np

PATH_TO_X_TRAIN_DATA  = "E:/bm-labor/Uebung9 - Deeplearning/UnetData/images/"
PATH_TO_Y_TRAIN_DATA = "E:/bm-labor/Uebung9 - Deeplearning/UnetData/Masks/"

PATH_TO_X_VAL_DATA = "E:/bm-labor/Uebung9 - Deeplearning/UnetData/imagesValidation/"
PATH_TO_Y_VAL_DATA = "E:/bm-labor/Uebung9 - Deeplearning/UnetData/MasksValidation/"


# get filenames for training data
training_data = os.listdir(PATH_TO_X_TRAIN_DATA)

#get all filenames for validation data
validation_data = os.listdir(PATH_TO_X_VAL_DATA)

x_train = np.zeros(shape=(len(training_data),256,256,3))
y_train = np.zeros(shape=(len(training_data),256,256,1))

x_val = np.zeros(shape=(len(validation_data),256,256,3))
y_val = np.zeros(shape=(len(validation_data),256,256,1))

# Loop for loading training data in RAM
for cnt,filename in tqdm(enumerate(training_data)):

    x_img = cv2.resize(cv2.imread(PATH_TO_X_TRAIN_DATA + filename),(256,256))
    if x_img is None:
        print("No Input image loaded!",filename)
        raise ValueError("No pic found!")
    y_img = cv2.resize(cv2.imread(PATH_TO_Y_TRAIN_DATA + filename,-1),(256,256))

    x_train[cnt] = x_img
    y_train[cnt] = np.expand_dims(y_img,-1)

# Loop for loading validation data in RAM
for cnt,filename in tqdm(enumerate(validation_data)):

    x_img = cv2.resize(cv2.imread(PATH_TO_X_VAL_DATA + filename),(256,256))
    if x_img is None:
        print("No Input image loaded!",filename)
        raise ValueError("No pic found!")
    y_img = cv2.resize(cv2.imread(PATH_TO_Y_VAL_DATA + filename,-1),(256,256))
    
    x_val[cnt] = x_img
    y_val[cnt] = np.expand_dims(y_img,-1)
    
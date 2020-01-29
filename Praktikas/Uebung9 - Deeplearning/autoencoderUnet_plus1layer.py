# -*- coding: utf-8 -*-
"""
Created on Tue May 22 15:36:17 2018

@author: bkraus
"""

from keras.layers import BatchNormalization, Activation, Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Conv2DTranspose, concatenate
from keras.models import Model
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import numpy as np

from ReadoutScaled import x_train
from ReadoutScaled import y_train
from ReadoutScaled import x_val
from ReadoutScaled import y_val

x_train = x_train / 255
#y_train = y_train / 255
x_val = x_val / 255
#y_val = y_val / 255

batch_size = 32
num_classes = 10
epochs = 100

output_dim = 1
input_dim = 3
#loss = ....


inputs = Input((None,None,input_dim))   #(32, 32, 3))
conv1 = Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
conv1 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv1)
pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)


conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(pool1)
conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv2)
pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)


conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(pool2)
conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv3)
pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)


conv4 = Conv2D(256, (3, 3), activation='relu', padding='same')(pool3)
conv4 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv4)
pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)


conv5 = Conv2D(512, (3, 3), activation='relu', padding='same')(pool4)
conv5 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv5)
pool5 = MaxPooling2D(pool_size=(2, 2))(conv5)

# tiefster Punkt

conv6 = Conv2D(1024, (3, 3), activation='relu', padding='same')(pool5)
conv6 = Conv2D(1024, (3, 3), activation='relu', padding='same')(conv6)
up7 = concatenate([Conv2DTranspose(512, (2, 2), strides=(2, 2), padding='same', name='concat1')(conv6), conv5], axis=3)

conv7 = Conv2D(512, (3, 3), activation='relu', padding='same')(up7)
conv7 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv7)
up8 = concatenate([Conv2DTranspose(256, (2, 2), strides=(2, 2), padding='same', name='concat2')(conv7), conv4], axis=3)

conv8 = Conv2D(256, (3, 3), activation='relu', padding='same')(up8)
conv8 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv8)
up9 = concatenate([Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same', name='concat3')(conv8), conv3], axis=3)

conv9 = Conv2D(128, (3, 3), activation='relu', padding='same')(up9)
conv9 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv9)
up10 = concatenate([Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same', name='concat4')(conv9), conv2], axis=3)

conv10 = Conv2D(64, (3, 3), activation='relu', padding='same')(up10)
conv10 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv10)
up11 = concatenate([Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same', name='concat5')(conv10), conv1], axis=3)

conv11 = Conv2D(32, (3, 3), activation='relu', padding='same')(up11)
conv11 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv11)
conv12 = Conv2D(output_dim, (3, 3), activation='sigmoid', padding='same')(conv11)

model = Model(inputs=[inputs], outputs=[conv12])
model.compile(optimizer='adam', loss="binary_crossentropy")

# load pretrained weights# load p #
saveDir = './'
es_cb = EarlyStopping(monitor='val_loss', patience=10, verbose=1, mode='auto')
#chkpt = saveDir + 'AutoEncoder_SampleData_Deep_weights.{epoch:02d}-{loss:.2f}-{val_loss:.2f}.hdf5'
#cp_cb = ModelCheckpoint(filepath = chkpt, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')



history = model.fit( x_train,y_train,  #x_train_noise, x_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    callbacks=[es_cb],
                    shuffle=True, validation_data = (x_val, y_val))



#score = model.evaluate(x_test_noise, x_test, verbose=1)
#print(score)
def plotHist(hist):
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

plotHist(history)


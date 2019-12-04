# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:23:47 2019

@author: rglabor07
"""

import itk

fixedImageFile = "fixed.png"
movingImageFile = "moving.png"
outputImageFile = "output.png"
differenceImageAfterFile = "after.png"
differenceImageBeforeFile = "before.png"


PixelType = itk.ctype('float')
fixedImage = itk.imread(fixedImageFile, PixelType)
movingImage = itk.imread(movingImageFile, PixelType)
Dimension = fixedImage.GetImageDimension()
FixedImageType = itk.Image[PixelType, Dimension]
MovingImageType = itk.Image[PixelType, Dimension]

TransformType = itk.TranslationTransform[itk.D, Dimension]
initialTransform = TransformType.New()

optimizer = itk.RegularStepGradientDescentOptimizerv4.New(LearningRate=4,MinimumStepLength=0.001,RelaxationFactor=0.5,NumberOfIterations=200)

metric = itk.MeanSquaresImageTolmageMetricv4[FixedImageType, MovingImageType].New()

registration = itk.ImageRegistrationMethodv4.New(FixedImage=fixedImage,MovingImage=movingImage,Metric=metric,Optimizer=optimizer,InitialTransform=initialTransform)

movingInitialTransform = TransformType.New()
initialParameters = movingInitialTransform.GetParameters()
initialParameters[0] = 0
initialParameters[1] = 0
movingInitialTransform.SetParameters(initialParameters)
registration.SetMovingInitialTransform(movingInitialTransform)
identityTransform = TransformType.New()
identityTransform.SetIdentity()


# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:43:29 2019

@author: 1627405
"""

import vtk
#import random
#import math

def cylinderFactory(height, radius, resolution):
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetHeight(height)
    cylinder.SetRadius(radius)
    cylinder.SetResolution(resolution)
    
    return cylinder

def cubeFactory(xLength, yLength, zLength):
    cube = vtk.vtkCubeSource()
    cube.SetXLength(xLength)
    cube.SetYLength(yLength)
    cube.SetZLength(zLength)
    
    return cube

cylinder = cylinderFactory(5, 0.5, 100)   
    
cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())
    
cylinderActor1 = vtk.vtkActor()
cylinderActor2 = vtk.vtkActor()
cylinderActor3 = vtk.vtkActor()

cylinderActor1.SetMapper(cylinderMapper)
cylinderActor2.SetMapper(cylinderMapper)
cylinderActor3.SetMapper(cylinderMapper)

cylinderActor1.SetOrigin(1, 1, 1)
cylinderActor2.SetOrigin(1, 2, 1)
cylinderActor3.SetOrigin(1, 3, 1)

cube = cubeFactory(2 , 2, 2)

cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())

cubeActor1 = vtk.vtkActor()
cubeActor2 = vtk.vtkActor()
cubeActor3 = vtk.vtkActor()

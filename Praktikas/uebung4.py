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
cylinder2 = cylinderFactory(5, 0.5, 100)   
cylinder3 = cylinderFactory(5, 0.5, 100)
    
#Mapping
cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())
cylinderMapper.SetInputConnection(cylinder2.GetOutputPort())
cylinderMapper.SetInputConnection(cylinder3.GetOutputPort())
    
#Actorerstellung
cylinderActor1 = vtk.vtkActor()
cylinderActor2 = vtk.vtkActor()
cylinderActor3 = vtk.vtkActor()

#Farben

cylinderActor1.GetProperty().SetColor(0 , 0 , 0)
cylinderActor2.GetProperty().SetColor(0.3 , 0.3 , 0.3)
cylinderActor3.GetProperty().SetColor(0.6 , 0.6 , 0.6)


#Postionierung

cylinderActor1.SetPosition(1.0, 2.0, 2.0)
cylinderActor2.SetPosition(1.0, 2.0, 4.0)
cylinderActor3.SetPosition(1.0, 2.0, 6.0)


#Verknüpfen des Actors
cylinderActor1.SetMapper(cylinderMapper)
cylinderActor2.SetMapper(cylinderMapper)
cylinderActor3.SetMapper(cylinderMapper)


cube = cubeFactory(2 , 2, 8)
cube2 = cubeFactory(2, 2, 8)

#Mapping
cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())
cubeMapper.SetInputConnection(cube2.GetOutputPort())

#Actorerstellung
cubeActor1 = vtk.vtkActor()
cubeActor2 = vtk.vtkActor()

#Verknüpfung
cubeActor1.SetMapper(cubeMapper)
cubeActor2.SetMapper(cubeMapper)

#Positionierung
cubeActor1.SetPosition(1.0, 4.0, 4.0)
cubeActor2.SetPosition(1.0, -1.0, 4.0)

##assembly
assembly = vtk.vtkAssembly()
assembly.AddPart(cylinderActor1)
assembly.AddPart(cylinderActor2)
assembly.AddPart(cylinderActor3)
assembly.AddPart(cubeActor1)
assembly.AddPart(cubeActor2)
assembly.SetPosition(0, 0, 8.5)
assembly.RotateY(90)

##assembly2

assembly2 = vtk.vtkAssembly()
assembly2.ShallowCopy(assembly)
assembly.AddPart(assembly2)
#assembly2.AddPart(assembly)



ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

#ren.AddActor(cylinderActor1)
#ren.AddActor(cylinderActor2)
#ren.AddActor(cylinderActor3)
#ren.AddActor(cubeActor1)
#ren.AddActor(cubeActor2)
ren.AddActor(assembly)
ren.AddActor(assembly2)


ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(200,200)

iren.Initialize()

ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()

iren.Start()

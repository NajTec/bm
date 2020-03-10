# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:22:54 2019

@author: Agando
"""

import vtk
import os



pngReader1 = vtk.vtkPNGReader()
pngReader1.SetFileName("output.png")
pngReader1.Update()

#RenderWindow

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

#ImageViewer

imageViewer = vtk.vtkImageViewer2()
imageViewer.SetInputConnection(pngReader1.GetOutputPort())

windowInteractor = vtk.vtkRenderWindowInteractor()
imageViewer.SetupInteractor(windowInteractor)
imageViewer.Render()
imageViewer.GetRenderer().ResetCamera()
imageViewer.Render()

windowInteractor.Start()
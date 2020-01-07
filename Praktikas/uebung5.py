# -*- coding: utf-8 -*-

import vtk
import os


#Pfadname

folder = os.path.join(os.path.dirname(__file__), "Marching Man" )

#filename

file = os.path.join(os.path.dirname(__file__),"Marching Man", "MarchingMan06.dcm")

#print(folder)

reductionFactor = 1.0
independentComponents = True

colors = vtk.vtkNamedColors()


#renderer

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

#Dicom

DICOMImageReader = vtk.vtkDICOMImageReader()
DICOMImageReader.SetDirectoryName(folder)
#DICOMImageReader.SetFileName(file)
DICOMImageReader.Update()


locator = vtk.vtkMergePoints()
locator.SetDivisions(64, 64, 92)
locator.SetNumberOfPointsPerBucket(2)
locator.AutomaticOff()

iso = vtk.vtkMarchingCubes()
iso.SetInputConnection(DICOMImageReader.GetOutputPort())
iso.ComputeGradientsOn()
iso.ComputeScalarsOff()
iso.SetValue(0, 1150)
iso.SetLocator(locator)

#vtkplane

plane = vtk.vtkPlane()
plane.SetOrigin(100,0,0)
plane.SetNormal(1,0,0)

#create cutter

cutter=vtk.vtkCutter()
cutter.SetCutFunction(plane)
cutter.SetInputConnection(DICOMImageReader.GetOutputPort())
cutter.Update()
cutterMapper=vtk.vtkPolyDataMapper()
cutterMapper.SetInputConnection(cutter.GetOutputPort())


#3d-Mapper

isoMapper = vtk.vtkPolyDataMapper()
isoMapper.SetInputConnection(iso.GetOutputPort())
isoMapper.ScalarVisibilityOff()

#2D-Mapper

imageSliceMapper = vtk.vtkImageSliceMapper()
imageSliceMapper.SetInputConnection(DICOMImageReader.GetOutputPort())
imageSliceMapper.SetSliceNumber(14)

#3D-Actor
isoActor = vtk.vtkActor()
isoActor.SetMapper(isoMapper)
isoActor.GetProperty().SetColor(colors.GetColor3d("Wheat"))

#2D-Actor

imgActor= vtk.vtkImageActor()
imgActor.SetMapper(imageSliceMapper)

#create plane-Actor

planeActor = vtk.vtkActor()
planeActor.SetMapper(cutterMapper)

outline = vtk.vtkOutlineFilter()
outline.SetInputConnection(DICOMImageReader.GetOutputPort())

outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outline.GetOutputPort())

outlineActor = vtk.vtkActor()
outlineActor.SetMapper(outlineMapper)

# Add the actors to the renderer, set the background and size.
#
ren.AddActor(planeActor)
ren.AddActor(imgActor)
ren.AddActor(outlineActor)
ren.AddActor(isoActor)
ren.SetBackground(colors.GetColor3d("SlateGray"))
ren.GetActiveCamera().SetFocalPoint(0, 0, 0)
ren.GetActiveCamera().SetPosition(0, -1, 0)
ren.GetActiveCamera().SetViewUp(0, 0, -1)
ren.ResetCamera()
ren.GetActiveCamera().Dolly(1.5)
ren.ResetCameraClippingRange()

renWin.SetSize(640, 480)

renWin.Render()
iren.Start()
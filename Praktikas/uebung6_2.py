# -*- coding: utf-8 -*-
import vtk
import os

folder = os.path.join(os.path.dirname(__file__), "Marching Man" )

colors = vtk.vtkNamedColors()

#Dicom

DICOMImageReader = vtk.vtkDICOMImageReader()
DICOMImageReader.SetDirectoryName(folder)
#DICOMImageReader.SetFileName(file)
DICOMImageReader.Update()

imageShift = vtk.vtkImageShiftScale()
imageShift.SetInputConnection(DICOMImageReader.GetOutputPort())
imageShift.SetOutputScalarTypeToUnsignedShort()


mapper = vtk.vtkGPUVolumeRayCastMapper()
mapper.SetInputConnection(imageShift.GetOutputPort())


volumeColor = vtk.vtkColorTransferFunction()
volumeColor.AddRGBPoint(100, 0.0, 0.0, 0.0)
volumeColor.AddRGBPoint(950, 1.0, 0.5, 0.3)
volumeColor.AddRGBPoint(1200, 1.0, 0.5, 0.3)
volumeColor.AddRGBPoint(1550, 1.0, 1.0, 0.9)

scalarOpacity = vtk.vtkPiecewiseFunction()
scalarOpacity.AddPoint(100, 0.00)
scalarOpacity.AddPoint(950, 0.05)
scalarOpacity.AddPoint(1200, 0.01)
scalarOpacity.AddPoint(1550, 0.80)

volumeGradientOpacity = vtk.vtkPiecewiseFunction()
volumeGradientOpacity.AddPoint(0, 0.0)
volumeGradientOpacity.AddPoint(20, 0.5)
volumeGradientOpacity.AddPoint(30, 1.0)


volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetColor(volumeColor)
volumeProperty.SetScalarOpacity(scalarOpacity)
volumeProperty.SetGradientOpacity(volumeGradientOpacity)

volume = vtk.vtkVolume()
volume.SetProperty(volumeProperty)
volume.SetMapper(mapper)

#renderer

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.AddVolume(volume)
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



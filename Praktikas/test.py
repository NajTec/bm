
import vtk
from vtk.util import numpy_support
import os
import numpy
from matplotlib import pyplot, cm


folder = os.path.join(os.path.dirname(__file__), "Marching Man" )

colors = vtk.vtkNamedColors()

#renderer

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

DICOMImageReader = vtk.vtkDICOMImageReader()
DICOMImageReader.SetDirectoryName(folder)
#DICOMImageReader.SetFileName(file)
DICOMImageReader.Update()

ImageViewer = vtk.vtkImageViewer2()
ImageViewer.SetInputConnection(DICOMImageReader.GetOutputPort())
ImageViewer.SetSlice(1)


imgActor= vtk.vtkImageActor()

ImageViewer.SetupInteractor(iren)
ImageViewer.Render()

iren.Initialize()
iren.Start()


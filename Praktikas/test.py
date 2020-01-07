
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

#ImageSliceMapper
imageSliceMapper = vtk.vtkImageSliceMapper()
imageSliceMapper.SetInputConnection(DICOMImageReader.GetOutputPort())
imageSliceMapper.SetSliceNumber(14)

imgActor= vtk.vtkImageActor()
imgActor.SetMapper(imageSliceMapper)


ren.AddActor(imgActor)
iren.Initialize()
iren.Start()


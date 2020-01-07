import vtk
import os

file = os.path.join(os.path.dirname(__file__),"output.png")

reader = vtk.vtkPNGReader()
reader.SetFileName(file)


imageViewer = vtk.vtkImageViewer2()
imageViewer.SetInputConnection(reader.GetOutputPort())

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
imageViewer.SetupInteractor(renderWindowInteractor)
imageViewer.Render()
imageViewer.GetRenderer().ResetCamera()
imageViewer.Render()

renderWindowInteractor.Start()
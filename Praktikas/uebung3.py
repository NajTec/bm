# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import vtk
import random
import math

colors = vtk.vtkNamedColors()

class MouseInteractorHighLightActor(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self, parent=None):
        self.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent)

        self.LastPickedActor = None
        self.LastPickedProperty = vtk.vtkProperty()

    def leftButtonPressEvent(self, obj, event):
        clickPos = self.GetInteractor().GetEventPosition()
        picker = vtk.vtkPropPicker()
        picker.Pick(clickPos[0], clickPos[1], 0, self.GetDefaultRenderer())

        # get the new
        self.NewPickedActor = picker.GetActor()

        # If something was selected
        if self.NewPickedActor:
            # If we picked something before, reset its property
            if self.LastPickedActor:
                self.LastPickedActor.GetProperty().DeepCopy(self.LastPickedProperty)

            # Save the property of the picked actor so that we can
            # restore it next time
            self.LastPickedProperty.DeepCopy(self.NewPickedActor.GetProperty())
            # Highlight the picked actor by changing its properties
            self.NewPickedActor.GetProperty().SetColor(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
            self.NewPickedActor.GetProperty().SetDiffuse(1.0)
            self.NewPickedActor.GetProperty().SetSpecular(0.0)

            # save the last picked actor
            self.LastPickedActor = self.NewPickedActor

        self.OnLeftButtonDown()
        return





#zylinder wird erstellt

cylinder = vtk.vtkCylinderSource() 
cylinder.SetResolution(100)
cylinder.SetRadius(0.5)
cylinder.SetHeight(5)


#zylinder 2 wird erstellt

cylinder2 = vtk.vtkCylinderSource()
cylinder2.SetResolution(100)
cylinder2.SetRadius(0.5)
cylinder2.SetHeight(5)

#rotationsmatrix x-Achse

matrix = vtk.vtkMatrix4x4()

matrix.SetElement(0, 0, 1)
matrix.SetElement(1, 1, math.cos(45))
matrix.SetElement(1, 2, -math.sin(45))
matrix.SetElement(2, 1, math.sin(45))
matrix.SetElement(2, 2, math.cos(45))

#rotationsmatrix y-Achse

matrix2 = vtk.vtkMatrix4x4()

matrix2.SetElement(0, 0, math.cos(45))
matrix2.SetElement(0, 2, math.sin(45))
matrix2.SetElement(1, 1, 1)
matrix2.SetElement(2, 0, -math.sin(45))
matrix2.SetElement(2, 2, math.cos(45))



# The mapper is responsible for pushing the geometry into the graphics
# library. It may also do color mapping, if scalars or other
# attributes are defined
cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

cylinder2Mapper = vtk.vtkPolyDataMapper()
cylinder2Mapper.SetInputConnection(cylinder2.GetOutputPort())

# The actor is a grouping mechanism: besides the geometry (mapper), it
# also has a property, transformation matrix, and/or texture map.
# Here we set its color and rotate it  degrees
cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.GetProperty().SetColor(0 , 0 , 0)
cylinderActor.SetOrigin(1, 3, 1)
#cylinderActor.RotateX(45.0)
cylinderActor.SetUserMatrix(matrix)

cylinder2Actor = vtk.vtkActor()
cylinder2Actor.SetMapper(cylinder2Mapper)
cylinder2Actor.GetProperty().SetColor(0, 0, 0)
cylinder2Actor.SetOrigin(1, 1, 1)
#cylinder2Actor.RotateY(45.0)
cylinder2Actor.SetUserMatrix(matrix2)

# Create the graphics structure. The renderer renders into the render
# window. The render window interactor captures mouse events and will
# perform appropriate camera or actor manipulation depending on the
# nature of the events

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)


#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)

####################################

#add the custom style

style = MouseInteractorHighLightActor()
style.SetDefaultRenderer(ren)
interactor.SetInteractorStyle(style)

ren.AddActor(cylinderActor)
ren.AddActor(cylinder2Actor)
ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(200,200)

interactor.Initialize()

ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()

interactor.Start()


import vtk
import pynocchio as pyn
from pynocchio import skeletons


reader = vtk.vtkOBJReader()
reader.SetFileName('data/girl.obj')
reader.Update()
poly_data = reader.GetOutput()

points = pyn.Points()
for i in range(poly_data.GetPoints().GetNumberOfPoints()):
    p = poly_data.GetPoints().GetPoint(i)
    points.append(pyn.Vector3(p[0], p[1], p[2]))
triangles = pyn.Indices()

for i in range(poly_data.GetNumberOfCells()):
    p_ids = vtk.vtkIdList()
    poly_data.GetCellPoints(i, p_ids)
    for p_id in range(p_ids.GetNumberOfIds()):
        triangles.append(p_ids.GetId(p_id))

skeleton = skeletons.HumanSkeleton()
skeleton.scale(.7)

# mesh = pyn.Mesh('data/girl.obj')
mesh = pyn.Mesh(points, triangles)
pyn.auto_rig(skeleton, mesh)

import unittest

from pynocchio import Mesh, MeshVertex, MeshEdge, Vector3, Points, Indices


class MeshTest(unittest.TestCase):
    def test_empty(self):
        mesh = Mesh()
        self.assertIsNotNone(mesh)

    def test_invalid_filename(self):
        mesh = Mesh('invalid_name')
        self.assertIsNotNone(mesh)
        self.assertEqual(len(mesh.vertices), 0)
        self.assertEqual(len(mesh.edges), 0)

    @unittest.skip("requires external .obj file")
    def test_cube_filename(self):
        mesh = Mesh('data/cube.obj')
        self.assertIsNotNone(mesh)
        for vertex in mesh.vertices:
            self.assertNotEqual(sum(vertex.normal), 0.)

    def test_from_data(self):
        points = Points()
        points.append(Vector3(0., 0., 0.))
        points.append(Vector3(1., 1., 1.))
        points.append(Vector3(1., 1., 0.))
        indices = Indices()
        indices.append(0)
        indices.append(1)
        indices.append(2)
        mesh = Mesh(points, indices)
        self.assertIsNotNone(mesh)

    def test_mesh_vertex(self):
        v = MeshVertex()
        self.assertEqual(v.position[0], 0.)
        self.assertEqual(v.position[1], 0.)
        self.assertEqual(v.position[2], 0.)
        v = MeshVertex(Vector3(1., 2., 3.))
        self.assertEqual(v.position[0], 1.)
        self.assertEqual(v.position[1], 2.)
        self.assertEqual(v.position[2], 3.)

    def test_mesh_edge(self):
        e = MeshEdge()
        self.assertEqual(e.vertex, -1)
        e = MeshEdge(100)
        self.assertEqual(e.vertex, 100)

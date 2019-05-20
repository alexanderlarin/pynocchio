import unittest

from pynocchio import Mesh


class MeshTest(unittest.TestCase):
    def test_empty(self):
        mesh = Mesh()
        self.assertIsNotNone(mesh)

    def test_invalid_filename(self):
        mesh = Mesh('invalid_name')
        self.assertIsNotNone(mesh)
        self.assertEqual(len(mesh.vertices), 0)
        self.assertEqual(len(mesh.edges), 0)

    def test_cube_filename(self):
        mesh = Mesh('data/cube.obj')
        self.assertIsNotNone(mesh)
        for vertex in mesh.vertices:
            self.assertNotEqual(sum(vertex.normal), 0.)

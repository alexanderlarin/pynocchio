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

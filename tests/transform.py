import unittest

from pynocchio import Vector3, Transform


class TransformTest(unittest.TestCase):
    def test_translate(self):
        v = Transform(Vector3(1., 2., 3.)) * Vector3(0., 0., 0.)
        self.assertEqual(v[0], 1.)
        self.assertEqual(v[1], 2.)
        self.assertEqual(v[2], 3.)

        v = Transform(Vector3(-1., -2., -3.)) * v
        self.assertEqual(v[0], 0.)
        self.assertEqual(v[1], 0.)
        self.assertEqual(v[2], 0.)

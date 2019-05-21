import unittest

from pynocchio import Vector3, Transform


class TransformTest(unittest.TestCase):
    def test_translate(self):
        translate = Vector3(1., 2., 3.)
        transform = Transform(translate)

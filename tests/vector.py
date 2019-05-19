import unittest

from pynocchio import Vector3


class Vector3Test(unittest.TestCase):
    def setUp(self):
        self.v = Vector3(1., 2., 3.)

    def test_len_func(self):
        self.assertEqual(len(self.v), 3)

    def test_get_by_index(self):
        self.assertEqual(self.v[0], 1.)
        self.assertEqual(self.v[1], 2.)
        self.assertEqual(self.v[2], 3.)

    def test_set_by_index(self):
        self.v[0] = 3.
        self.v[1] = 2.
        self.v[2] = 1.
        self.assertEqual(self.v[0], 3.)
        self.assertEqual(self.v[1], 2.)
        self.assertEqual(self.v[2], 1.)

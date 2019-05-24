import unittest

from pynocchio import skeletons


class SkeletonsTest(unittest.TestCase):
    def test_skeleton(self):
        self.assertIsNotNone(skeletons.Skeleton())

    def test_human_skeleton(self):
        s = skeletons.HumanSkeleton()
        self.assertIsNotNone(s)
        self.assertEqual(len(s.vertices), 18)
        self.assertEqual(s.parent_indices[0], -1)

    def test_file_skeleton(self):
        self.assertIsNotNone(skeletons.FileSkeleton('test_skeleton'))

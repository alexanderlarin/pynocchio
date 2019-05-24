import unittest

from pynocchio import skeletons


class SkeletonsTest(unittest.TestCase):
    def test_skeleton(self):
        self.assertIsNotNone(skeletons.Skeleton())

    def test_human_skeleton(self):
        self.assertIsNotNone(skeletons.HumanSkeleton())

    def test_file_skeleton(self):
        self.assertIsNotNone(skeletons.FileSkeleton('test_skeleton'))

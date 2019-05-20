import unittest

from pynocchio import auto_rig, HumanSkeleton, Mesh


class AutoRigTests(unittest.TestCase):
    def setUp(self):
        pass

    @unittest.skip
    def test_data(self):
        mesh = Mesh('data/sveta.obj')
        skeleton = HumanSkeleton()
        attach = auto_rig(skeleton, mesh)

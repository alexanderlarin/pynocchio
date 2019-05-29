import unittest

from pynocchio import auto_rig, Mesh
from pynocchio import skeletons


@unittest.skip
class AutoRigTests(unittest.TestCase):
    def test_data(self):
        mesh = Mesh('data/sveta.obj')
        skeleton = skeletons.HumanSkeleton()
        attach = auto_rig(skeleton, mesh)

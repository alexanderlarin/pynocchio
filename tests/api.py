import unittest

from pynocchio import auto_rig, HumanSkeleton, Mesh


class AutoRigTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_data(self):
        mesh = Mesh('./example/data/sveta.obj')
        skeleton = HumanSkeleton()
        attach = auto_rig(skeleton, mesh)
        print(len(attach.get_embedding()))

import unittest

from pynocchio import skeletons, Vector3


class SkeletonsTest(unittest.TestCase):
    def test_human_skeleton(self):
        s = skeletons.HumanSkeleton()
        self.assertIsNotNone(s)
        self.assertEqual(len(s.vertices), 18)
        # self.assertEqual(s.parent_indices[0], -1)

    def test_quad_skeleton(self):
        s = skeletons.QuadSkeleton()
        self.assertEqual(len(s.vertices), 18)

    def test_horse_skeleton(self):
        s = skeletons.HorseSkeleton()
        self.assertEqual(len(s.vertices), 20)

    def test_centaur_skeleton(self):
        s = skeletons.CentaurSkeleton()
        self.assertEqual(len(s.vertices), 25)

    def test_file_skeleton(self):
        self.assertIsNotNone(skeletons.FileSkeleton('test_skeleton'))

    def test_custom_skeleton(self):
        class CustomSkeleton(skeletons.SkeletonBase):
            def __init__(self):
                super(CustomSkeleton, self).__init__()
                self._make_joint('shoulders', Vector3(0., 0.5, 0.))
                self._make_joint('back', Vector3(0., 0.15, 0.), 'shoulders')
                self._make_joint('hips', Vector3(0., 0., 0.), 'back')
                self._make_joint('head', Vector3(0., 0.7, 0.), 'shoulders')

                self._make_joint('lthigh', Vector3(-0.1, 0., 0.), 'hips')
                self._make_joint('lknee', Vector3(-0.15, -0.35, 0.), 'lthigh')
                self._make_joint('lankle', Vector3(-0.15, -0.8, 0.), 'lknee')
                self._make_joint('lfoot', Vector3(-0.15, -0.8, 0.1), 'lankle')

                self._make_joint('rthigh', Vector3(0.1, 0., 0.), 'hips')
                self._make_joint('rknee', Vector3(0.15, -0.35, 0.), 'rthigh')
                self._make_joint('rankle', Vector3(0.15, -0.8, 0.), 'rknee')
                self._make_joint('rfoot', Vector3(0.15, -0.8, 0.1), 'rankle')

                self._make_joint('lshoulder', Vector3(-0.2, 0.5, 0.), 'shoulders')
                self._make_joint('lelbow', Vector3(-0.4, 0.25, 0.075), 'lshoulder')
                self._make_joint('lhand', Vector3(-0.6, 0.0, 0.15), 'lelbow')

                self._make_joint('rshoulder', Vector3(0.2, 0.5, 0.), 'shoulders')
                self._make_joint('relbow', Vector3(0.4, 0.25, 0.075), 'rshoulder')
                self._make_joint('rhand', Vector3(0.6, 0.0, 0.15), 'relbow')

                self._make_symmetric('lthigh', 'rthigh')
                self._make_symmetric('lknee', 'rknee')
                self._make_symmetric('lankle', 'rankle')
                self._make_symmetric('lfoot', 'rfoot')

                self._make_symmetric('lshoulder', 'rshoulder')
                self._make_symmetric('lelbow', 'relbow')
                self._make_symmetric('lhand', 'rhand')

                self._make_compressed()

                self._set_foot('lfoot')
                self._set_foot('rfoot')

                self._set_fat('hips')
                self._set_fat('shoulders')
                self._set_fat('head')

        s = CustomSkeleton()
        self.assertEqual(len(s.vertices), 18)
        self.assertEqual(len(s.parent_indices), len(s.vertices))
        self.assertEqual(s.parent_indices[0], -1)


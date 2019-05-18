import pynocchio


assert pynocchio.__version__ == '0.0.1'
assert pynocchio.Mesh('test_mesh')
assert pynocchio.Skeleton()
assert pynocchio.HumanSkeleton()
assert pynocchio.FileSkeleton('test_skeleton')
v = pynocchio.Vector3(0., 1., 2.)
assert len(v) == 3
assert v[0] == 0.
assert v[1] == 1.
assert v[2] == 2.
v[1] = 5.
assert v[1] == 5.

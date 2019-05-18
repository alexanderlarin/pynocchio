import pynocchio


assert pynocchio.__version__ == '0.0.1'
assert pynocchio.Mesh('test_mesh')
assert pynocchio.Skeleton()
assert pynocchio.HumanSkeleton()
assert pynocchio.FileSkeleton('test_skeleton')

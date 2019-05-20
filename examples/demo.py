import pyglet
from pyglet.gl import *
from pynocchio import auto_rig, Mesh, HumanSkeleton


class Model:
    def __init__(self, mesh):
        self._batch = pyglet.graphics.Batch()
        vertices = [edge.vertex for edge in mesh.edges]
        positions = []
        for vertex in mesh.vertices:
            position = vertex.position
            positions.append(position[0])
            positions.append(position[1])
            positions.append(position[2])
        self._batch.add_indexed(len(mesh.vertices), GL_TRIANGLES, None,
                                vertices, ('v3d', tuple(positions)))

    def draw(self):
        self._batch.draw()


class Bones:
    def __init__(self, skeleton, embedding):
        self._batch = pyglet.graphics.Batch()
        positions = []
        for i in range(1, len(skeleton.parent_indices)):
            j = skeleton.parent_indices[i]
            v1 = embedding[i]
            v2 = embedding[j]
            positions.append(v1[0])
            positions.append(v1[1])
            positions.append(v1[2])
            positions.append(v2[0])
            positions.append(v2[1])
            positions.append(v2[2])
        self._batch.add((len(skeleton.parent_indices) - 1) * 2, GL_LINES, None, ('v3d', positions))

    def draw(self):
        self._batch.draw()


mesh = Mesh('data/sveta.obj')
skeleton = HumanSkeleton()
skeleton.scale(0.7)
attach = auto_rig(skeleton, mesh)

model = Model(mesh)
bones = Bones(skeleton, attach.embedding)
window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
    glTranslatef(window.width // 2, window.height // 2, 0.)
    glScalef(200., 200., 0.)
    model.draw()
    glColor3d(0, 5., 0)
    glLineWidth(5.)
    bones.draw()


pyglet.app.run()

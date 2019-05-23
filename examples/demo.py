import signal

import pyglet
from pyglet.gl import *
from pynocchio import auto_rig, Mesh, HumanSkeleton, Vector3, Transform, VectorTransform


class Animation:
    def __init__(self, transforms_count, axis, stretch, delta):
        self._axis = axis
        self._stretch = stretch
        self._delta = delta
        self._delta_sign = 1.
        self._transform_index = 0

        self._translates = [[0., 0., 0.] for i in range(transforms_count)]

    def step(self):
        value = self._translates[self._transform_index][self._axis]
        value = value + self._delta_sign * self._delta
        if value >= self._stretch:
            value = self._stretch
            self._delta_sign = self._delta_sign * -1
        if value <= 0.:
            value = 0.
            if self._delta_sign < 0:
                self._delta_sign = self._delta_sign * -1
                self._transform_index = 0 \
                    if self._transform_index + 1 == len(self._translates) else self._transform_index + 1
        self._translates[self._transform_index][self._axis] = value
        return VectorTransform([Transform(Vector3(t[0], t[1], t[2])) for t in self._translates])


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
        self._vertex_list = self._batch.add_indexed(len(mesh.vertices), GL_TRIANGLES, None,
                                                    vertices, ('v3d', tuple(positions)))

    def update(self, mesh):
        positions = []
        for vertex in mesh.vertices:
            position = vertex.position
            positions.append(position[0])
            positions.append(position[1])
            positions.append(position[2])
        self._vertex_list.vertices = positions

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


human_mesh = Mesh('data/sveta.obj')
human_skeleton = HumanSkeleton()
human_skeleton.scale(0.7)
attach = auto_rig(human_skeleton, human_mesh)

model = Model(human_mesh)
bones = Bones(human_skeleton, attach.embedding)
window = pyglet.window.Window()
animation = Animation(len(attach.embedding), 0, 0.5, 0.05)


def setup():
    glTranslatef(window.width // 2, window.height // 2, 0.)
    glScalef(200., 200., 1.)


def update(dt):
    mesh = attach.deform(human_mesh, animation.step())
    global model
    model.update(mesh)


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
    glColor3f(1., 1., 1.)
    model.draw()
    # glColor3f(0., .5, 0.)
    # bones.draw()


pyglet.clock.schedule_interval(update, 1. / 60)
setup()
pyglet.app.run()

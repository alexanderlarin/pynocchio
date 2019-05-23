#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>

#include "attachment.h"
#include "mesh.h"
#include "pinocchioApi.h"
#include "skeleton.h"
#include "vector.h"
#include "transform.h"


namespace py = pybind11;

PYBIND11_MAKE_OPAQUE(std::vector<Vector3>);
PYBIND11_MAKE_OPAQUE(std::vector<int>);
PYBIND11_MAKE_OPAQUE(std::vector<Transform<double> >);
PYBIND11_MAKE_OPAQUE(std::vector<MeshVertex>);
PYBIND11_MAKE_OPAQUE(std::vector<MeshEdge>);

PYBIND11_MODULE(pynocchio, m)
{
#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif

    py::class_<Vector3>(m, "Vector3")
        .def(py::init<double, double, double>())
        .def("__getitem__", [](const Vector3 &v, int i) {
            if (i >= v.size())
                throw py::index_error();
            return v[i];
        })
        .def("__setitem__", [](Vector3 &v, int i, double value) {
            if (i >= v.size())
                throw py::index_error();
            v[i] = value;
        })
        .def("__len__", &Vector3::size);
    py::bind_vector<std::vector<Vector3> >(m, "Points");
    py::bind_vector<std::vector<int> >(m, "Indices");

    py::class_<Transform<double> >(m, "Transform")
        .def(py::init<>())
        .def(py::init<const Vector3 &>());
    py::bind_vector<std::vector<Transform<double> > >(m, "VectorTransform");

    py::class_<MeshVertex>(m, "MeshVertex")
        .def(py::init<>())
        .def(py::init<const Vector3 &>())
        .def_readwrite("position", &MeshVertex::pos)
        .def_readwrite("normal", &MeshVertex::normal);
    py::bind_vector<std::vector<MeshVertex> >(m, "VectorMeshVertex");

    py::class_<MeshEdge>(m, "MeshEdge")
        .def(py::init<>())
        .def(py::init<int>())
        .def_readwrite("vertex", &MeshEdge::vertex);
    py::bind_vector<std::vector<MeshEdge> >(m, "VectorMeshEdge");
    
    py::class_<Mesh>(m, "Mesh")
        .def(py::init<>())
        .def(py::init<const std::string &>())
        .def(py::init<const std::vector<Vector3> &, const std::vector<int> &>())
        .def_readwrite("vertices", &Mesh::vertices)
        .def_readwrite("edges", &Mesh::edges)
        .def("calculate_normals", &Mesh::computeVertexNormals);

    py::class_<Skeleton> skeleton(m, "Skeleton");
    skeleton
        .def(py::init<>())
        .def("scale", &Skeleton::scale)
        .def_property_readonly("parent_indices", &Skeleton::fPrev);

    py::class_<HumanSkeleton>(m, "HumanSkeleton", skeleton)
        .def(py::init<>());

    py::class_<FileSkeleton>(m, "FileSkeleton", skeleton)
        .def(py::init<const std::string &>());

    py::class_<Attachment>(m, "Attachment")
        .def(py::init<>())
        .def_property_readonly("embedding", &Attachment::getEmbedding)
        .def("deform", &Attachment::deform);

    m.def("auto_rig", &autorig);
}

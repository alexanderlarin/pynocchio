#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "attachment.h"
#include "mesh.h"
#include "pinocchioApi.h"
#include "skeleton.h"
#include "vector.h"


namespace py = pybind11;

PYBIND11_MODULE(pynocchio, m)
{
#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif

    py::class_<Mesh>(m, "Mesh")
        .def(py::init<const std::string &>());

    py::class_<Skeleton> skeleton(m, "Skeleton");
    skeleton
        .def(py::init<>());

    py::class_<HumanSkeleton>(m, "HumanSkeleton", skeleton)
        .def(py::init<>());

    py::class_<FileSkeleton>(m, "FileSkeleton", skeleton)
        .def(py::init<const std::string &>());

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

    py::class_<Attachment>(m, "Attachment")
        .def(py::init<>())
        .def("get_embedding", &Attachment::getEmbedding);

    m.def("auto_rig", &autorig);
}
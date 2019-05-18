#include <pybind11/pybind11.h>
#include "mesh.h"
#include "skeleton.h"
#include "vector.h"

namespace py = pybind11;

PYBIND11_MODULE(pynocchio, m)
{
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

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}
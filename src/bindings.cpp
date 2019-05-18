#include <pybind11/pybind11.h>
#include "mesh.h"

namespace py = pybind11;

PYBIND11_MODULE(pynocchio, m)
{
    py::class_<Mesh>(m, "Mesh")
        .def(py::init<const std::string &>());

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}
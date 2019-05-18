#include <pybind11/pybind11.h>
#include "math.hpp"

namespace py = pybind11;

PYBIND11_MODULE(pynocchio, m)
{
    m.def("add", &add);
    m.def("subtract", &subtract);

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}
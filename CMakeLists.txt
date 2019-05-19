cmake_minimum_required(VERSION 2.8.12)
project(pynocchio)

SET(SOURCE_DIR "src")

# Tell cmake that headers are in alse in source_dir
include_directories(${SOURCE_DIR})
SET(SOURCES "${SOURCE_DIR}/mesh.cpp"
    "${SOURCE_DIR}/skeleton.cpp"
    "${SOURCE_DIR}/lsqSolver.cpp"
    "${SOURCE_DIR}/attachment.cpp"
    "${SOURCE_DIR}/discretization.cpp"
    "${SOURCE_DIR}/embedding.cpp"
    "${SOURCE_DIR}/graphutils.cpp"
    "${SOURCE_DIR}/indexer.cpp"
    "${SOURCE_DIR}/intersector.cpp"
    "${SOURCE_DIR}/refinement.cpp"
    "${SOURCE_DIR}/pinocchioApi.cpp")

# Generate python module
add_subdirectory(lib/pybind11)
pybind11_add_module(pynocchio ${SOURCES} "${SOURCE_DIR}/bindings.cpp")

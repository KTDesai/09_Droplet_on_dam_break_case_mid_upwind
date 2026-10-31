cmake_minimum_required(VERSION 3.11...3.28)

project(DropletDamBreak CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Executable goes to <case>/bin; run it from the case directory so that
# mesh/ and results/ resolve (see src/paths.hh).
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)

file(GLOB SOURCES CONFIGURE_DEPENDS ${PROJECT_SOURCE_DIR}/src/*.cc)
add_executable(main ${SOURCES})
target_include_directories(main PRIVATE ${PROJECT_SOURCE_DIR}/src)

# Eigen: pass -DEigen3_DIR=<path> to cmake if it is installed elsewhere.
find_package(Eigen3 REQUIRED
  HINTS $ENV{CONDA_PREFIX}/share/eigen3/cmake
        $ENV{HOME}/miniconda3/share/eigen3/cmake
        /usr/local/lib/cmake/eigen3
        /usr/lib/cmake/eigen3)
target_link_libraries(main PUBLIC Eigen3::Eigen)

find_package(OpenMP)
if(OpenMP_CXX_FOUND)
  target_link_libraries(main PUBLIC OpenMP::OpenMP_CXX)
endif()

# Keep a compile_commands.json next to the sources for editor tooling.
execute_process(
  COMMAND ${CMAKE_COMMAND} -E create_symlink
    ${CMAKE_BINARY_DIR}/compile_commands.json
    ${CMAKE_SOURCE_DIR}/compile_commands.json
)

# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/lcm

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/lcm/build

# Include any dependencies generated for this target.
include test/cpp/CMakeFiles/test-cpp-client.dir/depend.make

# Include the progress variables for this target.
include test/cpp/CMakeFiles/test-cpp-client.dir/progress.make

# Include the compile flags for this target's objects.
include test/cpp/CMakeFiles/test-cpp-client.dir/flags.make

test/cpp/CMakeFiles/test-cpp-client.dir/client.cpp.o: test/cpp/CMakeFiles/test-cpp-client.dir/flags.make
test/cpp/CMakeFiles/test-cpp-client.dir/client.cpp.o: ../test/cpp/client.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/cpp/CMakeFiles/test-cpp-client.dir/client.cpp.o"
	cd /home/ubuntu/lcm/build/test/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-cpp-client.dir/client.cpp.o -c /home/ubuntu/lcm/test/cpp/client.cpp

test/cpp/CMakeFiles/test-cpp-client.dir/client.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-cpp-client.dir/client.cpp.i"
	cd /home/ubuntu/lcm/build/test/cpp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ubuntu/lcm/test/cpp/client.cpp > CMakeFiles/test-cpp-client.dir/client.cpp.i

test/cpp/CMakeFiles/test-cpp-client.dir/client.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-cpp-client.dir/client.cpp.s"
	cd /home/ubuntu/lcm/build/test/cpp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ubuntu/lcm/test/cpp/client.cpp -o CMakeFiles/test-cpp-client.dir/client.cpp.s

test/cpp/CMakeFiles/test-cpp-client.dir/common.cpp.o: test/cpp/CMakeFiles/test-cpp-client.dir/flags.make
test/cpp/CMakeFiles/test-cpp-client.dir/common.cpp.o: ../test/cpp/common.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object test/cpp/CMakeFiles/test-cpp-client.dir/common.cpp.o"
	cd /home/ubuntu/lcm/build/test/cpp && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-cpp-client.dir/common.cpp.o -c /home/ubuntu/lcm/test/cpp/common.cpp

test/cpp/CMakeFiles/test-cpp-client.dir/common.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-cpp-client.dir/common.cpp.i"
	cd /home/ubuntu/lcm/build/test/cpp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ubuntu/lcm/test/cpp/common.cpp > CMakeFiles/test-cpp-client.dir/common.cpp.i

test/cpp/CMakeFiles/test-cpp-client.dir/common.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-cpp-client.dir/common.cpp.s"
	cd /home/ubuntu/lcm/build/test/cpp && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ubuntu/lcm/test/cpp/common.cpp -o CMakeFiles/test-cpp-client.dir/common.cpp.s

# Object files for target test-cpp-client
test__cpp__client_OBJECTS = \
"CMakeFiles/test-cpp-client.dir/client.cpp.o" \
"CMakeFiles/test-cpp-client.dir/common.cpp.o"

# External object files for target test-cpp-client
test__cpp__client_EXTERNAL_OBJECTS =

test/cpp/test-cpp-client: test/cpp/CMakeFiles/test-cpp-client.dir/client.cpp.o
test/cpp/test-cpp-client: test/cpp/CMakeFiles/test-cpp-client.dir/common.cpp.o
test/cpp/test-cpp-client: test/cpp/CMakeFiles/test-cpp-client.dir/build.make
test/cpp/test-cpp-client: lcm/liblcm.so.1.4.0
test/cpp/test-cpp-client: test/gtest/libgtest_main.so
test/cpp/test-cpp-client: test/gtest/libgtest.so
test/cpp/test-cpp-client: test/cpp/CMakeFiles/test-cpp-client.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable test-cpp-client"
	cd /home/ubuntu/lcm/build/test/cpp && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-cpp-client.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/cpp/CMakeFiles/test-cpp-client.dir/build: test/cpp/test-cpp-client

.PHONY : test/cpp/CMakeFiles/test-cpp-client.dir/build

test/cpp/CMakeFiles/test-cpp-client.dir/clean:
	cd /home/ubuntu/lcm/build/test/cpp && $(CMAKE_COMMAND) -P CMakeFiles/test-cpp-client.dir/cmake_clean.cmake
.PHONY : test/cpp/CMakeFiles/test-cpp-client.dir/clean

test/cpp/CMakeFiles/test-cpp-client.dir/depend:
	cd /home/ubuntu/lcm/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/lcm /home/ubuntu/lcm/test/cpp /home/ubuntu/lcm/build /home/ubuntu/lcm/build/test/cpp /home/ubuntu/lcm/build/test/cpp/CMakeFiles/test-cpp-client.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/cpp/CMakeFiles/test-cpp-client.dir/depend


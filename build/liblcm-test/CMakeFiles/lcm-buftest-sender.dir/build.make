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
include liblcm-test/CMakeFiles/lcm-buftest-sender.dir/depend.make

# Include the progress variables for this target.
include liblcm-test/CMakeFiles/lcm-buftest-sender.dir/progress.make

# Include the compile flags for this target's objects.
include liblcm-test/CMakeFiles/lcm-buftest-sender.dir/flags.make

liblcm-test/CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.o: liblcm-test/CMakeFiles/lcm-buftest-sender.dir/flags.make
liblcm-test/CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.o: ../liblcm-test/buftest-sender.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object liblcm-test/CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.o"
	cd /home/ubuntu/lcm/build/liblcm-test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.o   -c /home/ubuntu/lcm/liblcm-test/buftest-sender.c

liblcm-test/CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.i"
	cd /home/ubuntu/lcm/build/liblcm-test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/liblcm-test/buftest-sender.c > CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.i

liblcm-test/CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.s"
	cd /home/ubuntu/lcm/build/liblcm-test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/liblcm-test/buftest-sender.c -o CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.s

# Object files for target lcm-buftest-sender
lcm__buftest__sender_OBJECTS = \
"CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.o"

# External object files for target lcm-buftest-sender
lcm__buftest__sender_EXTERNAL_OBJECTS =

liblcm-test/lcm-buftest-sender: liblcm-test/CMakeFiles/lcm-buftest-sender.dir/buftest-sender.c.o
liblcm-test/lcm-buftest-sender: liblcm-test/CMakeFiles/lcm-buftest-sender.dir/build.make
liblcm-test/lcm-buftest-sender: lcm/liblcm.so.1.4.0
liblcm-test/lcm-buftest-sender: /usr/lib/aarch64-linux-gnu/libglib-2.0.so
liblcm-test/lcm-buftest-sender: liblcm-test/CMakeFiles/lcm-buftest-sender.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable lcm-buftest-sender"
	cd /home/ubuntu/lcm/build/liblcm-test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/lcm-buftest-sender.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
liblcm-test/CMakeFiles/lcm-buftest-sender.dir/build: liblcm-test/lcm-buftest-sender

.PHONY : liblcm-test/CMakeFiles/lcm-buftest-sender.dir/build

liblcm-test/CMakeFiles/lcm-buftest-sender.dir/clean:
	cd /home/ubuntu/lcm/build/liblcm-test && $(CMAKE_COMMAND) -P CMakeFiles/lcm-buftest-sender.dir/cmake_clean.cmake
.PHONY : liblcm-test/CMakeFiles/lcm-buftest-sender.dir/clean

liblcm-test/CMakeFiles/lcm-buftest-sender.dir/depend:
	cd /home/ubuntu/lcm/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/lcm /home/ubuntu/lcm/liblcm-test /home/ubuntu/lcm/build /home/ubuntu/lcm/build/liblcm-test /home/ubuntu/lcm/build/liblcm-test/CMakeFiles/lcm-buftest-sender.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : liblcm-test/CMakeFiles/lcm-buftest-sender.dir/depend


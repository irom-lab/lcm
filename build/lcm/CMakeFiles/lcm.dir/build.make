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
include lcm/CMakeFiles/lcm.dir/depend.make

# Include the progress variables for this target.
include lcm/CMakeFiles/lcm.dir/progress.make

# Include the compile flags for this target's objects.
include lcm/CMakeFiles/lcm.dir/flags.make

lcm/CMakeFiles/lcm.dir/eventlog.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/eventlog.c.o: ../lcm/eventlog.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object lcm/CMakeFiles/lcm.dir/eventlog.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/eventlog.c.o   -c /home/ubuntu/lcm/lcm/eventlog.c

lcm/CMakeFiles/lcm.dir/eventlog.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/eventlog.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/eventlog.c > CMakeFiles/lcm.dir/eventlog.c.i

lcm/CMakeFiles/lcm.dir/eventlog.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/eventlog.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/eventlog.c -o CMakeFiles/lcm.dir/eventlog.c.s

lcm/CMakeFiles/lcm.dir/lcm.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/lcm.c.o: ../lcm/lcm.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object lcm/CMakeFiles/lcm.dir/lcm.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/lcm.c.o   -c /home/ubuntu/lcm/lcm/lcm.c

lcm/CMakeFiles/lcm.dir/lcm.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/lcm.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/lcm.c > CMakeFiles/lcm.dir/lcm.c.i

lcm/CMakeFiles/lcm.dir/lcm.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/lcm.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/lcm.c -o CMakeFiles/lcm.dir/lcm.c.s

lcm/CMakeFiles/lcm.dir/lcm_file.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/lcm_file.c.o: ../lcm/lcm_file.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object lcm/CMakeFiles/lcm.dir/lcm_file.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/lcm_file.c.o   -c /home/ubuntu/lcm/lcm/lcm_file.c

lcm/CMakeFiles/lcm.dir/lcm_file.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/lcm_file.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/lcm_file.c > CMakeFiles/lcm.dir/lcm_file.c.i

lcm/CMakeFiles/lcm.dir/lcm_file.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/lcm_file.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/lcm_file.c -o CMakeFiles/lcm.dir/lcm_file.c.s

lcm/CMakeFiles/lcm.dir/lcm_memq.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/lcm_memq.c.o: ../lcm/lcm_memq.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object lcm/CMakeFiles/lcm.dir/lcm_memq.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/lcm_memq.c.o   -c /home/ubuntu/lcm/lcm/lcm_memq.c

lcm/CMakeFiles/lcm.dir/lcm_memq.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/lcm_memq.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/lcm_memq.c > CMakeFiles/lcm.dir/lcm_memq.c.i

lcm/CMakeFiles/lcm.dir/lcm_memq.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/lcm_memq.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/lcm_memq.c -o CMakeFiles/lcm.dir/lcm_memq.c.s

lcm/CMakeFiles/lcm.dir/lcm_mpudpm.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/lcm_mpudpm.c.o: ../lcm/lcm_mpudpm.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object lcm/CMakeFiles/lcm.dir/lcm_mpudpm.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/lcm_mpudpm.c.o   -c /home/ubuntu/lcm/lcm/lcm_mpudpm.c

lcm/CMakeFiles/lcm.dir/lcm_mpudpm.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/lcm_mpudpm.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/lcm_mpudpm.c > CMakeFiles/lcm.dir/lcm_mpudpm.c.i

lcm/CMakeFiles/lcm.dir/lcm_mpudpm.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/lcm_mpudpm.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/lcm_mpudpm.c -o CMakeFiles/lcm.dir/lcm_mpudpm.c.s

lcm/CMakeFiles/lcm.dir/lcm_tcpq.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/lcm_tcpq.c.o: ../lcm/lcm_tcpq.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building C object lcm/CMakeFiles/lcm.dir/lcm_tcpq.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/lcm_tcpq.c.o   -c /home/ubuntu/lcm/lcm/lcm_tcpq.c

lcm/CMakeFiles/lcm.dir/lcm_tcpq.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/lcm_tcpq.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/lcm_tcpq.c > CMakeFiles/lcm.dir/lcm_tcpq.c.i

lcm/CMakeFiles/lcm.dir/lcm_tcpq.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/lcm_tcpq.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/lcm_tcpq.c -o CMakeFiles/lcm.dir/lcm_tcpq.c.s

lcm/CMakeFiles/lcm.dir/lcm_udpm.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/lcm_udpm.c.o: ../lcm/lcm_udpm.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building C object lcm/CMakeFiles/lcm.dir/lcm_udpm.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/lcm_udpm.c.o   -c /home/ubuntu/lcm/lcm/lcm_udpm.c

lcm/CMakeFiles/lcm.dir/lcm_udpm.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/lcm_udpm.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/lcm_udpm.c > CMakeFiles/lcm.dir/lcm_udpm.c.i

lcm/CMakeFiles/lcm.dir/lcm_udpm.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/lcm_udpm.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/lcm_udpm.c -o CMakeFiles/lcm.dir/lcm_udpm.c.s

lcm/CMakeFiles/lcm.dir/ringbuffer.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/ringbuffer.c.o: ../lcm/ringbuffer.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building C object lcm/CMakeFiles/lcm.dir/ringbuffer.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/ringbuffer.c.o   -c /home/ubuntu/lcm/lcm/ringbuffer.c

lcm/CMakeFiles/lcm.dir/ringbuffer.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/ringbuffer.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/ringbuffer.c > CMakeFiles/lcm.dir/ringbuffer.c.i

lcm/CMakeFiles/lcm.dir/ringbuffer.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/ringbuffer.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/ringbuffer.c -o CMakeFiles/lcm.dir/ringbuffer.c.s

lcm/CMakeFiles/lcm.dir/udpm_util.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/udpm_util.c.o: ../lcm/udpm_util.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building C object lcm/CMakeFiles/lcm.dir/udpm_util.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/udpm_util.c.o   -c /home/ubuntu/lcm/lcm/udpm_util.c

lcm/CMakeFiles/lcm.dir/udpm_util.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/udpm_util.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/udpm_util.c > CMakeFiles/lcm.dir/udpm_util.c.i

lcm/CMakeFiles/lcm.dir/udpm_util.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/udpm_util.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/udpm_util.c -o CMakeFiles/lcm.dir/udpm_util.c.s

lcm/CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.o: ../lcm/lcmtypes/channel_port_map_update_t.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Building C object lcm/CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.o   -c /home/ubuntu/lcm/lcm/lcmtypes/channel_port_map_update_t.c

lcm/CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/lcmtypes/channel_port_map_update_t.c > CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.i

lcm/CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/lcmtypes/channel_port_map_update_t.c -o CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.s

lcm/CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.o: lcm/CMakeFiles/lcm.dir/flags.make
lcm/CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.o: ../lcm/lcmtypes/channel_to_port_t.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_11) "Building C object lcm/CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.o"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.o   -c /home/ubuntu/lcm/lcm/lcmtypes/channel_to_port_t.c

lcm/CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.i"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/lcm/lcm/lcmtypes/channel_to_port_t.c > CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.i

lcm/CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.s"
	cd /home/ubuntu/lcm/build/lcm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/lcm/lcm/lcmtypes/channel_to_port_t.c -o CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.s

# Object files for target lcm
lcm_OBJECTS = \
"CMakeFiles/lcm.dir/eventlog.c.o" \
"CMakeFiles/lcm.dir/lcm.c.o" \
"CMakeFiles/lcm.dir/lcm_file.c.o" \
"CMakeFiles/lcm.dir/lcm_memq.c.o" \
"CMakeFiles/lcm.dir/lcm_mpudpm.c.o" \
"CMakeFiles/lcm.dir/lcm_tcpq.c.o" \
"CMakeFiles/lcm.dir/lcm_udpm.c.o" \
"CMakeFiles/lcm.dir/ringbuffer.c.o" \
"CMakeFiles/lcm.dir/udpm_util.c.o" \
"CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.o" \
"CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.o"

# External object files for target lcm
lcm_EXTERNAL_OBJECTS =

lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/eventlog.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/lcm.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/lcm_file.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/lcm_memq.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/lcm_mpudpm.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/lcm_tcpq.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/lcm_udpm.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/ringbuffer.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/udpm_util.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/lcmtypes/channel_port_map_update_t.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/lcmtypes/channel_to_port_t.c.o
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/build.make
lcm/liblcm.so.1.4.0: /usr/lib/aarch64-linux-gnu/libglib-2.0.so
lcm/liblcm.so.1.4.0: lcm/CMakeFiles/lcm.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/lcm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_12) "Linking C shared library liblcm.so"
	cd /home/ubuntu/lcm/build/lcm && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/lcm.dir/link.txt --verbose=$(VERBOSE)
	cd /home/ubuntu/lcm/build/lcm && $(CMAKE_COMMAND) -E cmake_symlink_library liblcm.so.1.4.0 liblcm.so.1 liblcm.so

lcm/liblcm.so.1: lcm/liblcm.so.1.4.0
	@$(CMAKE_COMMAND) -E touch_nocreate lcm/liblcm.so.1

lcm/liblcm.so: lcm/liblcm.so.1.4.0
	@$(CMAKE_COMMAND) -E touch_nocreate lcm/liblcm.so

# Rule to build all files generated by this target.
lcm/CMakeFiles/lcm.dir/build: lcm/liblcm.so

.PHONY : lcm/CMakeFiles/lcm.dir/build

lcm/CMakeFiles/lcm.dir/clean:
	cd /home/ubuntu/lcm/build/lcm && $(CMAKE_COMMAND) -P CMakeFiles/lcm.dir/cmake_clean.cmake
.PHONY : lcm/CMakeFiles/lcm.dir/clean

lcm/CMakeFiles/lcm.dir/depend:
	cd /home/ubuntu/lcm/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/lcm /home/ubuntu/lcm/lcm /home/ubuntu/lcm/build /home/ubuntu/lcm/build/lcm /home/ubuntu/lcm/build/lcm/CMakeFiles/lcm.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lcm/CMakeFiles/lcm.dir/depend


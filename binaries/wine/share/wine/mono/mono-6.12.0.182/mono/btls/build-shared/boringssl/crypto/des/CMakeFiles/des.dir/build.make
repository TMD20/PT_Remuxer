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
CMAKE_SOURCE_DIR = /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared

# Include any dependencies generated for this target.
include boringssl/crypto/des/CMakeFiles/des.dir/depend.make

# Include the progress variables for this target.
include boringssl/crypto/des/CMakeFiles/des.dir/progress.make

# Include the compile flags for this target's objects.
include boringssl/crypto/des/CMakeFiles/des.dir/flags.make

boringssl/crypto/des/CMakeFiles/des.dir/des.c.o: boringssl/crypto/des/CMakeFiles/des.dir/flags.make
boringssl/crypto/des/CMakeFiles/des.dir/des.c.o: /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/external/boringssl/crypto/des/des.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object boringssl/crypto/des/CMakeFiles/des.dir/des.c.o"
	cd /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared/boringssl/crypto/des && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/des.dir/des.c.o   -c /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/external/boringssl/crypto/des/des.c

boringssl/crypto/des/CMakeFiles/des.dir/des.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/des.dir/des.c.i"
	cd /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared/boringssl/crypto/des && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/external/boringssl/crypto/des/des.c > CMakeFiles/des.dir/des.c.i

boringssl/crypto/des/CMakeFiles/des.dir/des.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/des.dir/des.c.s"
	cd /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared/boringssl/crypto/des && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/external/boringssl/crypto/des/des.c -o CMakeFiles/des.dir/des.c.s

des: boringssl/crypto/des/CMakeFiles/des.dir/des.c.o
des: boringssl/crypto/des/CMakeFiles/des.dir/build.make

.PHONY : des

# Rule to build all files generated by this target.
boringssl/crypto/des/CMakeFiles/des.dir/build: des

.PHONY : boringssl/crypto/des/CMakeFiles/des.dir/build

boringssl/crypto/des/CMakeFiles/des.dir/clean:
	cd /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared/boringssl/crypto/des && $(CMAKE_COMMAND) -P CMakeFiles/des.dir/cmake_clean.cmake
.PHONY : boringssl/crypto/des/CMakeFiles/des.dir/clean

boringssl/crypto/des/CMakeFiles/des.dir/depend:
	cd /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/external/boringssl/crypto/des /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared/boringssl/crypto/des /usr/local/bin/mine/remux/binaries/wine/mono/mono-6.12.0.182/mono/btls/build-shared/boringssl/crypto/des/CMakeFiles/des.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : boringssl/crypto/des/CMakeFiles/des.dir/depend

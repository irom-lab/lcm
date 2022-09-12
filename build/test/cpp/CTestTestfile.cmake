# CMake generated Testfile for 
# Source directory: /home/ubuntu/lcm/test/cpp
# Build directory: /home/ubuntu/lcm/build/test/cpp
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(CPP::memq_test "/home/ubuntu/lcm/build/test/cpp/test-cpp-memq_test")
set_tests_properties(CPP::memq_test PROPERTIES  _BACKTRACE_TRIPLES "/home/ubuntu/lcm/test/cpp/CMakeLists.txt;12;add_test;/home/ubuntu/lcm/test/cpp/CMakeLists.txt;0;")
add_test(CPP::client_server "/usr/bin/python" "/home/ubuntu/lcm/test/cpp/../run_client_server_test.py" "/home/ubuntu/lcm/build/test/c/test-c-server" "/home/ubuntu/lcm/build/test/cpp/test-cpp-client")
set_tests_properties(CPP::client_server PROPERTIES  _BACKTRACE_TRIPLES "/home/ubuntu/lcm/test/cpp/CMakeLists.txt;15;add_test;/home/ubuntu/lcm/test/cpp/CMakeLists.txt;0;")

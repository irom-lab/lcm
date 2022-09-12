# CMake generated Testfile for 
# Source directory: /home/ubuntu/lcm/test/python
# Build directory: /home/ubuntu/lcm/build/test/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(Python::bool_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/ubuntu/lcm/build/test/types:/home/ubuntu/lcm/build/lib/python3.8/site-packages" "/usr/bin/python" "/home/ubuntu/lcm/test/python/bool_test.py")
set_tests_properties(Python::bool_test PROPERTIES  _BACKTRACE_TRIPLES "/home/ubuntu/lcm/test/python/CMakeLists.txt;17;add_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;22;add_python_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;0;")
add_test(Python::byte_array_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/ubuntu/lcm/build/test/types:/home/ubuntu/lcm/build/lib/python3.8/site-packages" "/usr/bin/python" "/home/ubuntu/lcm/test/python/byte_array_test.py")
set_tests_properties(Python::byte_array_test PROPERTIES  _BACKTRACE_TRIPLES "/home/ubuntu/lcm/test/python/CMakeLists.txt;17;add_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;23;add_python_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;0;")
add_test(Python::lcm_file_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/ubuntu/lcm/build/test/types:/home/ubuntu/lcm/build/lib/python3.8/site-packages" "/usr/bin/python" "/home/ubuntu/lcm/test/python/lcm_file_test.py")
set_tests_properties(Python::lcm_file_test PROPERTIES  _BACKTRACE_TRIPLES "/home/ubuntu/lcm/test/python/CMakeLists.txt;17;add_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;24;add_python_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;0;")
add_test(Python::lcm_memq_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/ubuntu/lcm/build/test/types:/home/ubuntu/lcm/build/lib/python3.8/site-packages" "/usr/bin/python" "/home/ubuntu/lcm/test/python/lcm_memq_test.py")
set_tests_properties(Python::lcm_memq_test PROPERTIES  _BACKTRACE_TRIPLES "/home/ubuntu/lcm/test/python/CMakeLists.txt;17;add_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;25;add_python_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;0;")
add_test(Python::lcm_thread_test "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/ubuntu/lcm/build/test/types:/home/ubuntu/lcm/build/lib/python3.8/site-packages" "/usr/bin/python" "/home/ubuntu/lcm/test/python/lcm_thread_test.py")
set_tests_properties(Python::lcm_thread_test PROPERTIES  _BACKTRACE_TRIPLES "/home/ubuntu/lcm/test/python/CMakeLists.txt;17;add_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;26;add_python_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;0;")
add_test(Python::client_server "/usr/bin/cmake" "-E" "env" "PYTHONPATH=/home/ubuntu/lcm/build/test/types:/home/ubuntu/lcm/build/lib/python3.8/site-packages" "/usr/bin/python" "/home/ubuntu/lcm/test/run_client_server_test.py" "/home/ubuntu/lcm/build/test/c/test-c-server" "/usr/bin/python" "/home/ubuntu/lcm/test/python/client.py")
set_tests_properties(Python::client_server PROPERTIES  _BACKTRACE_TRIPLES "/home/ubuntu/lcm/test/python/CMakeLists.txt;17;add_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;28;add_python_test;/home/ubuntu/lcm/test/python/CMakeLists.txt;0;")

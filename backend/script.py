import subprocess

cpp_file = "wow.cpp"
output = "program"

compile_command = ["g++", cpp_file, "-o", output]
compilation = subprocess.run(compile_command, capture_output = True)

if compilation.returncode == 0:
    execution = subprocess.run(["./" + output], capture_output = True, text = True)
    print("wow")

    print(execution.stdout)
else:
    print("error")
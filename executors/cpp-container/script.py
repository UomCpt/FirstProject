import subprocess
import json
import sys

if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

cpp_file = sys.argv[1]
output = "program"

compile_command = ["g++", cpp_file, "-o", output]
compilation = subprocess.run(compile_command, capture_output = True, text = True)

cases = []

def generate_cases(case_id, stdout, stderr, returncode):
    cases.append({
        "case_id": case_id,
        "stdout": stdout,
        "stderr": stderr,
        "returncode": returncode
    })

test_cases = [
    (10, 2),
    (10, 5),
    (15, 5),
    (5, 0),
    (50, 2)
]

results = [5, 2, 3, -1, 25]

i = -1
success = 0
fails = 0
for num1, num2 in test_cases:

    if compilation.returncode == 0:
        i += 1
        input_data = f"{num1} {num2}\n"
        execution = subprocess.run(
            ["./" + output], input=input_data, capture_output=True, text=True)
        
        if int(execution.stdout) ==  results[i]:
            success += 1
            generate_cases(i + 1, execution.stdout, execution.stderr, 0)
        else:
            fails += 1
            generate_cases(i + 1, execution.stdout, execution.stderr, 1)
            break
else:
    print("error")

data = {
    "total_runs": i + 1,
    "success" : success,
    "fails": fails,
    "cases": cases
}

print(json.dumps(data))
import subprocess
import os

UPLOAD_DIR = "uploaded_java_files"
java_file = os.path.join(UPLOAD_DIR, "Main.java")

# Βεβαιωθείτε ότι το αρχείο υπάρχει
if not os.path.isfile(java_file):
    print(f"File {java_file} wasn't found!")
else:
    # Μεταγλώττιση Java
    compile_result = subprocess.run(["javac", java_file], capture_output=True, text=True)

    if compile_result.returncode != 0:
        print("Error at compiling:")
        print(compile_result.stderr)
    else:
        # Εκτέλεση Java (με καθορισμένο classpath)
        run_result = subprocess.run(["java", "-cp", UPLOAD_DIR, "Main"], capture_output=True, text=True)
        
        print("Έξοδος προγράμματος:")
        print(run_result.stdout)
        if run_result.stderr:
            print("Error:")
            print(run_result.stderr)
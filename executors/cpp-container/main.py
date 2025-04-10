from fastapi import FastAPI, File, UploadFile
import subprocess
import shutil
import os
import json
import platform

app = FastAPI()

UPLOAD_DIR = "/app/uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR, exist_ok = True)

@app.post("/upload-cpp")
async def upload_cpp(file: UploadFile = File(...)):
    #Save uploaded file into /app/uploads
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return {"error": str(e)}

    #Run compilation script
    try:
        results = script(file_path)
        return results
    except json.JSONDecodeError as e:
        return {"error": "Failed to decode JSON"}
    except Exception as e:
        return {"error": f"Script execution failed: {str(e)}"}

#Compilation and execution function
def script(file_path):
    cpp_file = file_path
    #cpp.exe can cause problems with linux or macOs systems
    output_file = "cpp.exe" if platform.system() == "Windows" else "cpp_output"

    compile_command = ["g++", cpp_file, "-o", output_file]
    try:
        compilation = subprocess.run(
            compile_command, capture_output = True, text = True, timeout = 30)
    except subprocess.TimeoutExpired:
        return {
            "error": "Compilation time out after 30 seconds"
        }
    
    #if compilation successfull
    if compilation.returncode == 0:
        try:
            execution = subprocess.run(
                ["./" + output_file], capture_output=True, text=True, timeout = 30)
            
            return {
                "stdout": execution.stdout,
                "stderr": execution.stderr,
                "returncode": execution.returncode
            }
        
        except subprocess.TimeoutExpired:
            return {
                "error": "Execution timed out after 30 seconds"
            }
    #if compilation fails
    else:
        return {
            "stdout": compilation.stdout,
            "stderr": compilation.stderr,
            "returncode": compilation.returncode
        }
    

    


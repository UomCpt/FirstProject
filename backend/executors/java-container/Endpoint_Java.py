from fastapi import FastAPI, File, UploadFile # type: ignore
import os
import subprocess

app = FastAPI()

UPLOAD_DIR = "uploaded_java_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure the directory exists

@app.post("/upload/")
async def upload_and_execute(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Get the class name (remove .java extension)
        class_name = os.path.splitext(file.filename)[0]

        # Compile the Java file
        compile_process = subprocess.run(
            ["javac", file_path], capture_output=True, text=True
        )

        if compile_process.returncode != 0:
            return {
                "message": "Compilation failed",
                "error": compile_process.stderr
            }

        # Run the compiled Java program
        run_process = subprocess.run(
            ["java", "-cp", UPLOAD_DIR, class_name], capture_output=True, text=True, timeout=30
        )

        return {
           
            "stdout": run_process.stdout,
            "stderr": run_process.stderr if run_process.stderr else None,
            "returncode": run_process.returncode
        }
    
    except subprocess.TimeoutExpired:
        return {
            "message": "Execution timed out after 30 seconds."
        }

    except Exception as e:
        return {"message": "An error occurred", "error": str(e)}
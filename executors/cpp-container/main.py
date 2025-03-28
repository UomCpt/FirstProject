from fastapi import FastAPI, File, UploadFile
import subprocess
import shutil
import os
import json

app = FastAPI()

UPLOAD_DIR = "/app/uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR, exist_ok = True)

@app.post("/upload-cpp")
async def upload_cpp(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"filename": file.filename, "message": "File uploaded successfully"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/run-script")
def run_script(file_name: str):
    try:
        file_path = os.path.join(UPLOAD_DIR, file_name)

        if not os.path.exists(file_path):
            return {"error": "File not found"}
        
        # Run the script using subprocess
        result = subprocess.run(
            ["python3", "script.py", file_path],  # Command to run the script
            capture_output=True,  # Capture the output of the script
            text=True,            # Decode output as text
            check=True            # Raise an error if the script fails
        )
        try:
            # Return the output of the script
            results = result.stdout.strip()
            json_results = json.loads(results)
            return json_results
        except json.JSONDecodeError:
            return {"error": "Failed to decode JSON from script output"}
    except subprocess.CalledProcessError as e:
        # Handle script errors
        return {"error": f"Script failed with error: {e.stderr}"}


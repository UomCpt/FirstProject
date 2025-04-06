from fastapi import FastAPI, UploadFile, File
import subprocess
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploaded_scripts"  # Φάκελος αποθήκευσης

# Δημιουργούμε τον φάκελο αν δεν υπάρχει
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_and_run(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Αποθηκεύουμε το αρχείο στο σύστημα
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Εκτελούμε το αρχείο Python με subprocess
    result = subprocess.run(["python", file_path], capture_output=True, text=True)

    return {
        "filename": file.filename,
        "output": result.stdout,
        "errors": result.stderr,
        "exit_code": result.returncode
    }

from fastapi import FastAPI, File, UploadFile
import shutil
import os
import subprocess

app = FastAPI()

@app.post("/upload/")
async def upload_and_execute(file: UploadFile = File(...)):
    # Temporarily save the file uploaded by the user in the variable file_temp
    file_temp = f"temp_{file.filename}"
    
    # Open the temporary file 
    with open(file_temp, "wb") as buffer:
        # Take the content of the file uploaded by the user and write it to the temporary file
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # Execute the temporary file and store the output in the variable result
        result = subprocess.run(['python', file_temp], capture_output=True, text=True, timeout=30, )
    except:
        # Delete the temporary file
        os.remove(file_temp)

        # Return the results
        return {"stdout": "",
                "stderr": "Time out",
                "returncode": ""
                }
        


    # Delete the temporary file
    os.remove(file_temp)

    # Return the results
    return {"stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode 
            }

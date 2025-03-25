from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/run-script")
def run_script():
    try:
        # Run the script using subprocess
        result = subprocess.run(
            ["python3", "script.py"],  # Command to run the script
            capture_output=True,  # Capture the output of the script
            text=True,            # Decode output as text
            check=True            # Raise an error if the script fails
        )
        # Return the output of the script
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Handle script errors
        return {"error": f"Script failed with error: {e.stderr}"}


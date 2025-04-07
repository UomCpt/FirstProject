from fastapi import FastAPI, File, UploadFile  # Εισαγωγή του FastAPI και του UploadFile για τη διαχείριση αρχείων
import uvicorn  # Χρήση του Uvicorn ως ASGI server για την εκτέλεση του API
import shutil  # Χρήση του shutil για προσωρινή αποθήκευση του αρχείου
import subprocess  # Για την εκτέλεση εξωτερικών εντολών συστήματος (gcc)
import os  # Διαχείριση αρχείων και διαδρομών

# Δημιουργία instance της FastAPI
app = FastAPI()

# Root endpoint (βασικό URL "/") που επιστρέφει ένα απλό μήνυμα
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}  # Επιστρέφει μήνυμα σε JSON μορφή

# Συνάρτηση που μεταγλωττίζει ένα αρχείο C με χρήση του GCC
def compile_c_file(c_file):
    if not os.path.isfile(c_file):
        print(f"Το αρχείο {c_file} δεν βρέθηκε.")
        return {"error": "File not found"}
    
    output_file = os.path.splitext(c_file)[0]  # Δημιουργεί το όνομα του εκτελέσιμου χωρίς την κατάληξη .c
    command = ["gcc", c_file, "-o", output_file]  # Δημιουργεί τη λίστα εντολών για το gcc

    try:
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"Η μεταγλώττιση ήταν επιτυχής. Το εκτελέσιμο αρχείο είναι: {output_file}")
            return {"message": "Compilation successful", "output_file": output_file}
        else:
            print("Σφάλμα κατά τη μεταγλώττιση:")
            print(result.stderr)
            return {"error": "Compilation failed", "details": result.stderr}

    except FileNotFoundError:
        print("Το gcc δεν βρέθηκε. Βεβαιώσου ότι είναι εγκατεστημένο.")
        return {"error": "GCC not found"}
    except Exception as e:
        print(f"Παρουσιάστηκε σφάλμα: {e}")
        return {"error": str(e)}

# Endpoint που δέχεται ένα αρχείο C μέσω POST request και το μεταγλωττίζει
@app.post("/CheckResultsC")
async def check_results(file: UploadFile = File(...)):
    """
    Το endpoint δέχεται ένα αρχείο C μέσω ενός POST request, το αποθηκεύει και προσπαθεί να το μεταγλωττίσει με GCC.
    """
    # Δημιουργία του φακέλου temp αν δεν υπάρχει
    os.makedirs("temp", exist_ok=True)

    # Ορισμός του μονοπατιού αποθήκευσης του αρχείου
    file_location = f"temp/{file.filename}"

    # Αποθήκευση του αρχείου στον φάκελο "temp/"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Κλήση της compile_c_file για μεταγλώττιση
    compile_result = compile_c_file(file_location)

    # Επιστροφή JSON με πληροφορίες για το αρχείο και τη μεταγλώττιση
    return {
        "filename": file.filename,  # Όνομα του αρχείου που ανέβηκε
        "content_type": file.content_type,  # Τύπος αρχείου
        "message": "File uploaded successfully!",
        "compilation_result": compile_result  # Αποτέλεσμα μεταγλώττισης
    }

# Εκκίνηση του server αν εκτελούμε το script απευθείας
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

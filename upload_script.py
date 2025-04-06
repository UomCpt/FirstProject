import requests

url = "http://127.0.0.1:8000/upload/"
files = {"file": open("message.py", "rb")}  # Εδώ μπορείς να αλλάξεις το όνομα του αρχείου αν θέλεις

response = requests.post(url, files=files)
print(response.json())  # Εκτυπώνει την έξοδο από το API

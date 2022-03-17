import requests

file_url = "https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/3710216.pdf"

r = requests.get(file_url, stream=True)

with open("python-syllabus.pdf", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        # writing one chunk at a time to pdf file
        if chunk:
            pdf.write(chunk)
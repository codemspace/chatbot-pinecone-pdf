import requests

url = "https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
local_filename = "bootstrap.min.css"

response = requests.get(url)

if response.status_code == 200:
    with open(local_filename, "wb") as file:
        file.write(response.content)
    print(f"File '{local_filename}' downloaded successfully.")
else:
    print("Failed to download the file.")
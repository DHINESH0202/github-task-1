import requests

response = requests.get("https://pypi.org/pypi/requests/json")

if response.status_code == 200:
    data = response.json()
    print("Package Name:", data["info"]["name"])
    print("Latest Version:", data["info"]["version"])
    print("Summary:", data["info"]["summary"])
else:
    print("Failed to fetch data from PyPI")
print("Temporary change")
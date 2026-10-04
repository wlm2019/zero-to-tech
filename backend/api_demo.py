import requests

resp = requests.get("https://api64.ipify.org?format=json")
print(resp.json())

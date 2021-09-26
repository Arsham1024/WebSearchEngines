import requests

# Stating URL
seed = "https://www.apple.com/"
pages = 3000

r = requests.get(seed)
print(r.text)

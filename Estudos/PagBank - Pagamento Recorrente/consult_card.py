import requests

url = "https://sandbox.api.pagseguro.com/tokens/cards"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer ecf9b8a3-3291-402d-8da4-992608e687a18a994d8f4923931df105ec8ed1bf1ba80985-164c-4037-806d-554b1e506a54"
}

payload = {
    "encrypted": "a4Dq2ZdzgCj042hNoipKXSh2gr0wyiZ5DGzY5j7GiMry7wWVnyfdnsKTfvxeHb33pwP/P1YRqdugmrEeBtHqsWEv/rtxrM9Q3kj7alU2+vpOVu8lmh2tEVenir3zusP4T5gLa80QbAUk0r9rMlLU5/i9hRhv2JxN8x/3VFMSWjZi3kNTaiUaPl0EuYBuNLoCTvemVUJjfk7oufmQhmkek9FiD9mlAvfVt4goDeUj8Mp/aR/lJpczMVRceJRULqIIy/XJ9pnY6KlG0c3rOU33jhEpTXYaGE3pYSsTb7oZYrCX7zT62peTSSg5PRU+6m8ZXGJpUQvDIa5OCzjsDO/FNQ=="
}

resp = requests.post(url, json=payload, headers=headers)

print(resp.status_code)
print(resp.text)

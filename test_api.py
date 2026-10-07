import json
from urllib.request import urlopen

BASE_URL = "http://127.0.0.1:5000"

def get_json(path: str):
    with urlopen(BASE_URL + path, timeout=5) as response:
        return response.status, json.loads(response.read().decode("utf-8"))

if __name__ == "__main__":
    status, payload = get_json("/health")
    print("GET /health ->", status)
    print(json.dumps(payload, indent=2))

    status, payload = get_json("/")
    print("GET / ->", status)
    print(json.dumps(payload, indent=2))

"""
Dependencies: json-rpc
    pip install json-rpc
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You must provide the method.")
        exit(1)
    else:
        method = sys.argv[1]
        params = sys.argv[2:]

    url = "http://127.0.0.1:8332"
    headers = {}
    payload = {
        "method": method,
        "params": params,
        "id": 1,
    }
    # Credentials
    auth = ("","")

    # Request
    response = requests.post(url, data=json.dumps(payload), headers=headers,
                             auth=auth).json()

    # Print response
    print(response['result'])

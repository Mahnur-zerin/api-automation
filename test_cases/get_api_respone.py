from json import JSONDecodeError

import requests

import json


def get_api_response(request_type, api_url, payload=None, headers=None):
    if headers is None:
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {get_auth_token()}"}

    else:
        headers = headers

    get_response = requests.request(request_type, api_url, headers=headers, data=payload)

    try:
        print("Response", json.dumps(get_response.json(), indent=4))
    except JSONDecodeError:
        print("Response", get_response)
    return get_response




def get_auth_token(email="mleaping@leapinglogic.com", password="siterocks"):
    auth_url = "https://rentmyapidevteam1.leaperdev.rocks/api/su-admin/users/login"
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json"}
    auth_payload = json.dumps({
        "email": email,
        "password": password
    })
    auth_request = requests.post(auth_url, headers=headers, data=auth_payload)
    token = json.loads(auth_request.text)["result"]["token"]
    print(token)
    return token


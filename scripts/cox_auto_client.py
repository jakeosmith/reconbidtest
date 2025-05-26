import os
import requests

TOKEN_URL = "https://authorize.coxautoinc.com/oauth2/aus132uaxy2eomhmi357/v1/token"
API_ENDPOINT = "https://api.coxautoinc.com/example"  # placeholder

CLIENT_ID = os.environ.get("COX_CLIENT_ID")
CLIENT_SECRET = os.environ.get("COX_CLIENT_SECRET")
SCOPE = "driveq.autograde.grading.read"

if not CLIENT_ID or not CLIENT_SECRET:
    raise SystemExit("Please set COX_CLIENT_ID and COX_CLIENT_SECRET environment variables")


def get_access_token():
    response = requests.post(
        TOKEN_URL,
        auth=(CLIENT_ID, CLIENT_SECRET),
        data={"grant_type": "client_credentials", "scope": SCOPE},
    )
    response.raise_for_status()
    return response.json()["access_token"]


def call_api(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(API_ENDPOINT, headers=headers)
    response.raise_for_status()
    return response.json()


def main():
    token = get_access_token()
    print("Fetched access token")
    data = call_api(token)
    print("API response:")
    print(data)


if __name__ == "__main__":
    main()

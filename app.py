import os
import requests
from flask import Flask, jsonify

TOKEN_URL = "https://authorize.coxautoinc.com/oauth2/aus132uaxy2eomhmi357/v1/token"
API_ENDPOINT = "https://api.coxautoinc.com/example"  # placeholder
SCOPE = "driveq.autograde.grading.read"

CLIENT_ID = os.environ.get("COX_CLIENT_ID")
CLIENT_SECRET = os.environ.get("COX_CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    raise SystemExit("Please set COX_CLIENT_ID and COX_CLIENT_SECRET environment variables")

app = Flask(__name__)


def get_access_token():
    response = requests.post(
        TOKEN_URL,
        auth=(CLIENT_ID, CLIENT_SECRET),
        data={"grant_type": "client_credentials", "scope": SCOPE},
    )
    response.raise_for_status()
    return response.json()["access_token"]


def fetch_data(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(API_ENDPOINT, headers=headers)
    response.raise_for_status()
    return response.json()


@app.route("/")
def index():
    token = get_access_token()
    data = fetch_data(token)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

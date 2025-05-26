import os
import requests

# Replace TENANT_ID with your tenant or environment identifier
TOKEN_URL = "https://authorize.coxautoinc.com/oauth2/TENANT_ID/token"
# Example protected API endpoint
API_URL = "https://api.example.com/hello"

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
SCOPES = os.environ.get("SCOPES", "")  # e.g. "scope1 scope2"

if not CLIENT_ID or not CLIENT_SECRET:
    raise SystemExit("Please set CLIENT_ID and CLIENT_SECRET environment variables")

payload = {
    "grant_type": "client_credentials",
    "scope": SCOPES,
}

# Acquire an access token
resp = requests.post(TOKEN_URL, data=payload, auth=(CLIENT_ID, CLIENT_SECRET))
resp.raise_for_status()
token = resp.json().get("access_token")
print(f"Access token: {token}")

# Call a protected endpoint
headers = {"Authorization": f"Bearer {token}"}
api_resp = requests.get(API_URL, headers=headers)
print("API response status:", api_resp.status_code)
print(api_resp.text)

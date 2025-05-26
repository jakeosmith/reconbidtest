# ReconBid Test

This repository provides a simple example of how to retrieve an OAuth access token from Cox Automotive and use it to call a protected API. The example script lives in `scripts/get_token.py`.

## Requirements

- Python 3
- The `requests` library (install with `pip install requests`)

## Usage

1. Set your client ID and client secret as environment variables:

```bash
export CLIENT_ID="your-client-id"
export CLIENT_SECRET="your-client-secret"
export SCOPES="desired scopes here"  # e.g. "inventory:read"
```

2. Edit the `TOKEN_URL` and `API_URL` constants inside `scripts/get_token.py` to match your environment and the endpoint you want to call.

3. Run the script:

```bash
python scripts/get_token.py
```

The script will POST to `https://authorize.coxautoinc.com/oauth2/.../token` with `grant_type=client_credentials`, print the retrieved `access_token`, and then call `API_URL` using that token.

Be sure to keep your client secret secure and avoid committing it to source control.

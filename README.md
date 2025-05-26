# reconbidtest

This repository demonstrates how to obtain an OAuth token from the Cox Auto API and make a sample API call. It includes a simple Flask app and a command-line script that show how to authenticate using the `client_credentials` grant.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Export your credentials as environment variables:
   ```bash
   export COX_CLIENT_ID="your-client-id"
   export COX_CLIENT_SECRET="your-client-secret"
   ```

## Usage

### Command line example

Run the sample client script:

```bash
python scripts/cox_auto_client.py
```

The script fetches an access token and calls a placeholder API endpoint. Replace `API_ENDPOINT` in `scripts/cox_auto_client.py` with the real endpoint you wish to use.

### Flask web app

You can also run a simple Flask application that returns the API response at `/`:

```bash
python app.py
```

Visit `http://localhost:5000/` in your browser to trigger the token fetch and API request. Update `API_ENDPOINT` in `app.py` with the endpoint you intend to call.

import os
import requests
from dotenv import load_dotenv

load_dotenv()


def refresh_access_token():
    url = "https://api.twitter.com/2/oauth2/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": os.getenv("TWITTER_REFRESH_TOKEN"),
        "client_id": os.getenv("TWITTER_CLIENT_ID"),
        "client_secret": os.getenv("TWITTER_CLIENT_SECRET"),
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        token_data = response.json()
        new_access_token = token_data.get("access_token")
        new_refresh_token = token_data.get(
            "refresh_token", os.getenv("TWITTER_REFRESH_TOKEN")
        )

        with open(".env", "r") as f:
            lines = f.readlines()

        with open(".env", "w") as f:
            for line in lines:
                if line.startswith("TWITTER_ACCESS_TOKEN="):
                    f.write(f"TWITTER_ACCESS_TOKEN={new_access_token}\n")
                elif line.startswith("TWITTER_REFRESH_TOKEN="):
                    f.write(f"TWITTER_REFRESH_TOKEN={new_refresh_token}\n")
                else:
                    f.write(line)

        print("✅ Access token refreshed.")
        return new_access_token
    else:
        print(f"❌ Failed to refresh token: {response.status_code} - {response.text}")
        return None

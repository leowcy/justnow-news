import os
import requests
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("TWITTER_ACCESS_TOKEN")


def post_tweet_v2(text: str):
    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    payload = {"text": text}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201 or response.status_code == 200:
        tweet_id = response.json()["data"]["id"]
        print(
            f"✅ Tweet posted successfully: https://twitter.com/user/status/{tweet_id}"
        )
    else:
        print(f"❌ Failed to post tweet: {response.status_code}")
        print(response.text)

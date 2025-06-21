import os
import tweepy
from flask import Flask, request
from dotenv import load_dotenv

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

load_dotenv()

app = Flask(__name__)

client_id = os.getenv("TWITTER_CLIENT_ID")
client_secret = os.getenv("TWITTER_CLIENT_SECRET")
redirect_uri = os.getenv("TWITTER_REDIRECT_URI")
scopes = os.getenv("TWITTER_SCOPES").split()

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=client_id,
    redirect_uri=redirect_uri,
    scope=scopes,
    client_secret=client_secret,
)


@app.route("/")
def index():
    auth_url = oauth2_user_handler.get_authorization_url()
    return f"""
        <h2>Twitter Auth Bot</h2>
        <p><a href="{auth_url}">Click Twitter</a></p>
    """


@app.route("/callback")
def callback():
    try:
        token = oauth2_user_handler.fetch_token(request.url)
        return f"""
            <h2>✅ Success </h2>
            <p><strong>Access Token:</strong><br>{token.get("access_token")}</p>
            <p><strong>Refresh Token:</strong><br>{token.get("refresh_token")}</p>
            <p>Copy above Token to .env </p>
        """
    except Exception as e:
        return f"<h2>❌ Auth Failed</h2><pre>{str(e)}</pre>"


if __name__ == "__main__":
    print("🚀 Visit http://localhost:8000 to Twitter Auth")
    app.run(port=8000)

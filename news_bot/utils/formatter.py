import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_tweet_prompt(title: str, link: str) -> str:
    system_prompt = (
        "You are a skilled social media copywriter. Your job is to turn news headlines into engaging, catchy tweets. "
        "Keep the tweet under 280 characters, include the link at the end, and make sure it's eye-catching and easy to understand."
    )
    user_prompt = f"News Headline: {title}\\nURL: {link}\\nWrite an engaging tweet for this news."


    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=150,
    )

    tweet = response["choices"][0]["message"]["content"]
    return tweet.strip()

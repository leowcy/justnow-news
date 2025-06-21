import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_tweet_prompt(title: str, link: str) -> str:
    system_prompt = "你是一位具有新闻编辑能力的社交媒体运营人员，负责将新闻标题转化为简洁有趣、吸引人的推文，风格口语化，控制在280字符以内。"
    user_prompt = (
        f"以下是一则新闻：\n标题：{title}\n链接：{link}\n请将它改写成一条吸引人的推文："
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",  # 或 gpt-3.5-turbo
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=150,
    )

    tweet = response["choices"][0]["message"]["content"]
    return tweet.strip()

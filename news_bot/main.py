from dotenv import load_dotenv
import schedule
import time

from utils.news import fetch_news
from utils.x import post_tweet_v2

load_dotenv()

def job():
    news_list = fetch_news()
    for news in news_list:
        content = f"{news['title']}\\n{news['link']}"
        post_tweet_v2(content)

# 每小时运行一次
schedule.every().hour.do(job)

if __name__ == "__main__":
    print("🚀 JustNow Bot Started...")
    job()
    while True:
        schedule.run_pending()
        time.sleep(10)

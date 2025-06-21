# 📰 JustNow News Bot

An automated Twitter/X bot that fetches breaking news and posts it to your account in a **clean, engaging, AI-enhanced format**.

---

## ✅ Features

- ⏱ Fetches the latest headlines from RSS feeds (e.g. NYTimes)
- 🧠 Uses **ChatGPT (OpenAI)** to rewrite headlines into catchy tweets
- 🐦 Posts them automatically to your X (Twitter) account using **OAuth 2.0 User Context**
- 🔄 Runs hourly with `schedule`
- ✅ Supports **Tweepy** or native `requests` for posting
- 🔐 Environment-configurable for flexibility and security

---

## 🚀 How to Run

### 1. Clone the project

```bash
git clone <your-repo-url>
cd justnow-news
```

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set up environment variables
Copy
cp .env.example .env
Update your .env with:

Copy
TWITTER_CLIENT_ID=xxx
TWITTER_CLIENT_SECRET=xxx
TWITTER_ACCESS_TOKEN=xxx
OPENAI_API_KEY=sk-xxxx

### 4. Start the bot
python main.py

🚀 JustNow Bot Started...
✅ Tweet posted: https://x.com/user/status/123...
✨ Sample Tweet Output
🚨 “AI Revolution Is Here” — Here’s what OpenAI just announced today.
Read more: https://nytimes.com/...

🛠 Optional Enhancements
🧠 Add GPT summaries

🔁 De-duplicate tweet history

🗃️ Log to SQLite or CSV

☁️ Deploy with Docker / systemd

🔔 Add Telegram alert on error

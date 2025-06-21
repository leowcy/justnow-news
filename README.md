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
make install

### 3. Set up environment variables
Copy
cp .env.example .env
Update your .env with:

### 4. Run X auth
python news_bot/utils/auth_flow.py

Click authorize and copy and secrets into
TWITTER_ACCESS_TOKEN=
TWITTER_REFRESH_TOKEN=

### 5. Start the bot
make run

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

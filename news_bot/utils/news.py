import feedparser

def fetch_news(rss_url="https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", limit=3):
    feed = feedparser.parse(rss_url)
    return [{
        "title": entry.title,
        "link": entry.link
    } for entry in feed.entries[:limit]]

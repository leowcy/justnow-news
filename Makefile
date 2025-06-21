# === JustNow News Bot Makefile ===

.PHONY: install run

## ⚙️ Setup Python environment & install dependencies
install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

## 🚀 Run the main scheduled bot (every hour)
run:
	@echo "🚀 Running JustNow News Bot..."
	python news_bot/main.py

import feedparser
import os
from telegram import Bot

TOKEN = os.getenv("TOKEN")
CHANNEL = os.getenv("CHANNEL")

bot = Bot(token=TOKEN)

feed = feedparser.parse(
    "https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru"
)

for entry in feed.entries[:3]:
    text = f"📰 {entry.title}\n\n{entry.link}"
    bot.send_message(chat_id=CHANNEL, text=text)
# restart

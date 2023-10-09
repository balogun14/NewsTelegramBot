import os
import requests
import telebot

# This gets my token from my .env file to use this just change the token
BOT_TOKEN = os.environ.get("BOT_TOKEN")
Api_key = os.environ.get("API_KEY")
bot = telebot.TeleBot(BOT_TOKEN)

# This gets the most recent news from the api and returns returns the json or the string
def get_daily_news(search: str):
    url = f"https://newsapi.org/v2/everything?q=${search}&sortBy=popularity&apiKey=3fc3482200ca420dace9c853f28540a9"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "No result found"

# This fetches the news and sends it to the user
def fetch_daily_news(message):
    """
        This fetches the json object returned by the get_daily_news method
        
    Args:
        message (string): This is a type of string the message text
    """
    search = message.text
    result = get_daily_news(search)
    articles = result.get("articles")
    total_result = result.get("totalResults")
    if total_result != 0:
        for article in articles:
            author = article.get("author")
            title = article.get("title")
            description = article.get("description")
            url = article.get("url")
            published_at = article.get("publishedAt")
            content = article.get("content")
        news_message = f"Auhor:{author}\n*Title:{title}*\nDescription:{description}\nContent:{content}\nPublished At: {published_at}\nCountinue reading:{url}"  # noqa: E501
        bot.send_message(message.chat.id, "Here is the result")
        bot.send_message(message.chat.id, news_message, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "No result found")


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing? \nType /news to search")


@bot.message_handler(commands=["news"])
def search_handler(message):
    text = "What do you want to get the news for e.g Google, facebook e.t.c"
    sent_message = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_message, fetch_daily_news)


bot.infinity_polling()

# test = get_daily_news("Google")
# print(test)

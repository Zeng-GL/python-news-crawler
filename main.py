from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import settings
import crawl
import db

app = Flask(__name__)

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

UDN = crawl.News.scrape(crawl.News,'https://udn.com/news/cate/2/6638')
db.db_obj.insert_data(db.db_obj,UDN)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    # Query the database based on the user's message
    # Retrieve data and send a response
    response = get_data_from_database(user_message)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response)
    )

def get_data_from_database(user_message):
    # Implement logic to query the database and retrieve data
    # Use the 'conn' object created earlier to execute SQL queries
    # Return the data as a string
    if user_message == '新聞' or 'news':
        result = db.db_obj.query_all(db.db_obj)
        return result

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
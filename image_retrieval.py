from pymessenger.bot import Bot
from flask import Flask, request

app = Flask(__name__)

ACCESS_TOKEN = "EAANx8rgACWsBAOk0w559riIR26VoF0zmfbCVK1MuZCZAiGZBXW2zRF6ZAtnN8fNleE6y8Saw393ZBtnZCWFNDDwXeZCR3s0ZCszDGXo7hCxpsT59YEaJj1dmoxm8hfKdZBQ6BR3ZBAGItGx4GkzLdK3qOWtDP9QKXyLQosJ5QdzFxeugZDZD"
VERIFY_TOKEN = "bless_up"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        bot.send_text_message(recipient_id, message)
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=5002, debug=True)
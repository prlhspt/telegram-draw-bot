import random

from flask import Flask, request
import requests

app = Flask(__name__)

token = 'BOT_TOKEN'
api_url = 'https://api.telegram.org'


@app.route('/', methods=['GET'])
def hello():
    return 'hello', 200


@app.route('/', methods=['POST'])
def webhook2():

    get_json = request.get_json()

    message = get_json.get('message')
    if message:
        if message.get('from'):
            last_name = message.get('from').get('last_name')
            if not last_name:
                last_name = ''
            first_name = message.get('from').get('first_name')
            if not first_name:
                first_name = ''

        chat = message.get('chat')
        if chat:
            chat_id = chat.get('id')

            text = message.get('text')
            if text and '/draw' in text:
                result = random.sample(range(1, 11), 1)
                requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}'
                             f'&text={last_name}{first_name} : {result}')

    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')

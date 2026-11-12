from flask import Flask, request, jsonify


my_secret_token = 'meu_token_whatsapp_123'


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, server!</p>"

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':

        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        desafio = request.args.get('hub.challenge')

        if mode == 'subscribe' and token == my_secret_token:
            print(request.args)
            return desafio
        else:
            return 'Token inválido', 403

    if request.method == 'POST':
        dados = request.get_json()
        print(" JSON Recebido no POST:", dados)
        #enviar para gemini + gspread

        return "EVENT_RECEIVED", 200
from flask import Flask, request, jsonify
from services.gemini_service import interpretar_mensagem
from services.sheets_service import inserirLinha

my_secret_token = 'meu_token_whatsapp_123'


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, server!</p>"

@app.route("/webhook", methods=['GET','POST'])
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
        dados = request.get_json() or {}

        entries = dados.get('entry', [])
        if not entries:
            return "ENTRIES NULL", 200

        changes  = entries[0].get('changes', [])
        if not changes:
            return "CHANGES NULL", 200

        value = changes[0].get('value', {})
        messages = value.get('messages', [])
        if not messages:
            print("Evento sem mensagens, ignorado")
            return "EVENT_RECEIVED", 200

        message = messages[0]

        if message.get('type') == 'text':
            rawMessage = message.get('text', {}).get('body')

            if rawMessage:
                geminiResponse = interpretar_mensagem(rawMessage)
                inserirLinha(geminiResponse)

                print(geminiResponse)

        return "EVENT_RECEIVED", 200
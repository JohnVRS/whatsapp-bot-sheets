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
        jsonData = request.get_json() or {}

        entries = jsonData.get('entry', [])
        if not entries:
            return "ENTRY NULL", 200

        changes = entries[0].get('changes', [])
        if not changes:
            return "CHANGES NULL", 200

        value = changes[0].get('value', {})
        rawMessage = value.get('messages', [])
        if not rawMessage:
            print("Evento sem mensagens ignorado.")
            return "EVENT_RECEIVED", 200
        message = rawMessage[0]

        if message.get('type') == 'text':
            messageBody = message.get('text', {}).get('body')

            if messageBody:
                geminiResponse = interpretar_mensagem(messageBody)
                if geminiResponse:
                    print(geminiResponse)
                    inserirLinha(geminiResponse)


        #message = rawMessage["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        

       
            #enviar para gemini + gspread
        #data_json = interpretar_mensagem(message)
        #inserirLinha(data_json)
        #print(data_json)
        

        return "EVENT_RECEIVED", 200
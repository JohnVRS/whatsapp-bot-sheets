from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, server!</p>"

@app.route("/webhook", methods=['GET'])
def verificarMetodo():
    if request.method() == 'GET':
        token = request.args.get('hub.verify_token')
        desafio = request.args.get('hub.challenge')

        print(request.args)

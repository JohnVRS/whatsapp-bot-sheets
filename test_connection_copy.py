from codecs import utf_8_encode
from datetime import datetime
import gspread
import json
from core_geminai_connection import interpretar_mensagem
from google.oauth2.service_account import  Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credenciais = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
cliente = gspread.authorize(credenciais)

NAME_SHEET = "Gestão da grana - EM CONSTRUÇÃO"

try:

    sheet = cliente.open(NAME_SHEET)
    aba_base = sheet.worksheet("BASE PRINCIPAL")

    data_atual = datetime.now().strftime("%d/%m/%Y")
    hora_atual = datetime.now().strftime("%H:%M:%S")
    mensagem_teste = "Assinei um serviço de streaming da Amazon, 24 Reais mensal"
    print(f" Testante frase: '{mensagem_teste}'\n")

    data_json = interpretar_mensagem(mensagem_teste)
    #lista = json.loads(data_json)
    #print(type(data_json))
    new_line = [
            data_json['Data'],
            data_json['Horário'],
            data_json['Item'],
            data_json['Valor'],
            data_json['Categoria'],
            data_json['Método de Pagamento'],
            data_json['Mensal'],
            data_json['Parcelado'],
            data_json['Parcela'],
            data_json['Tipo'],
            data_json['Origem'],
            data_json['Mensagem Raw'],
        ]
    print(new_line)
    print(type(new_line))
    aba_base.append_row(new_line)
    print("✅ Sucesso! Linha de teste inserida com sucesso na aba BASE!")

except gspread.exceptions.SpreadsheetNotFound:
    print(
        f"❌ Erro: Planilha '{NAME_SHEET}' não foi encontrada. Verifique o nome ou se compartilhou com o e-mail da Service Account."
    )
except gspread.exceptions.WorksheetNotFound:
    print(
        "❌ Erro: Aba 'BASE' não foi encontrada dentro da planilha. Verifique a grafia exata (letras maiúsculas/minúsculas)."
    )
except Exception as e:
    print(f"❌ Ocorreu um erro inesperado: {e}")


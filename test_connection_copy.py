from codecs import utf_8_encode
from datetime import datetime
import gspread
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
    mensagem_teste = "Comprei uma bicicleta parcelada em 8x 100 reais. Valor total R$800.00"
    print(f" Testante frase: '{mensagem_teste}'\n")

    ##PAREI AQUi
    
    data_json = interpretar_mensagem(mensagem_teste)

    for obj in data_json:
        print(data_json)
        print(len(data_json))

        if (len[data_json] - 1):
            aba_base.append_row(utf_8_encode(str(data_json)))
        else:    
            aba_base.append_row(utf_8_encode(data_json))
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


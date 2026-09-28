from datetime import datetime
import gspread
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


    new_line = [
        data_atual,
        hora_atual,
        "TESTANDO CONEXÃO",
        "1000",
        "TESTE",
        "PIX",
        "SIM",
        "Não",
        "15",
        "1/15",
        "Saída",
        "Automatico",
        "TESTE TESTE SCRIPT",
    ]
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


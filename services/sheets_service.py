from codecs import utf_8_encode
from datetime import datetime
import gspread
import json
import traceback
from services.gemini_service import interpretar_mensagem
from google.oauth2.service_account import  Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credenciais = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
cliente = gspread.authorize(credenciais)

NAME_SHEET = "Gestão da grana - EM CONSTRUÇÃO"


def inserirLinha(data_json):
    try:
        sheet = cliente.open(NAME_SHEET)
        aba_base = sheet.worksheet("BASE PRINCIPAL")

        new_line = [
            data_json.get("Data", "00/00/0000") or data_json.get("data", "00/00/0000"),
            data_json.get("Horário", "00:00:00") or data_json.get("horario", "00:00:00"),
            data_json.get("Item", "") or data_json.get("item", ""),
            data_json.get("Valor", "") or data_json.get("valor", ""),
            data_json.get("Categoria", "") or data_json.get("categoria", ""),
            data_json.get("Método de Pagamento") or data_json.get("metodo_de_pagamento", ""),
            data_json.get("Mensal", "") or data_json.get("mensal", ""),
            data_json.get("Parcelado", "") or data_json.get("parcelado", ""),
            data_json.get("Parcela", "") or data_json.get("parcela", ""),
            data_json.get("Número de parcelas", "") or data_json.get("numero_de_parcelas", ""),
            data_json.get("Tipo", "") or data_json.get("tipo", ""),
            data_json.get("Origem", "") or data_json.get("origem", ""),
            data_json.get("Mensagem Raw", "") or data_json.get("mensagem_raw", "")

        ]

        if new_line[7] == "Sim":
            parcelas = int(new_line[8]) + 1 
            for i in range(1,  parcelas):
                new_line[9] = f"{i}/{parcelas - 1}"
                aba_base.append_row(new_line)    
            print("✅ Sucesso! Linha de teste inserida com sucesso na aba BASE!")
        else:
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
        


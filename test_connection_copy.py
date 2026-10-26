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
    mensagem_teste = "Recebi meu salário no valor de 2000 na data 15/01/2002 as 14:00"
    print(f" Testante frase: '{mensagem_teste}'\n")

    #data_json = interpretar_mensagem(mensagem_teste)


    # CRIAR lógica para verificar se o item é parcelado, caso seja, inserir x vezes na planilha
    # SE FOR MENSAL - inserir a quantidade restante de mêses do ano atual.
    # Ajustar Horário.

    
    #new_line = [
           # data_json['Data'],
           # data_json['Horário'],
           # data_json['Item'],
           # data_json['Valor'],
           # data_json['Categoria'],
           # data_json['Método de Pagamento'],
          #  data_json['Mensal'],
          #  data_json['Parcelado'],
         #   data_json['Parcela'],
         #   data_json['Número de parcelas'],
        #    data_json['Tipo'],
       #     data_json['Origem'],
      #      data_json['Mensagem Raw'],
     #   ]

    #print(data_json)

    new_line = [
        "01/09/2026",
        "14:00",
        "Bicicleta",
        "1200",
        "Compras",
        "Cartão de Crédito",
        "Não",
        "Sim",
        "4",
        "1/4",
        "Saída",
        "Manual",
        "Comprei uma bicicleta parcelada no cartão de crédito em 4x de 300 reais."
    ]

    if new_line[7] == "Sim":

        for i in range(1,  int(new_line[8]) + 1 ):
            new_line[9] = f"{i}/{new_line[8]}"
            print(new_line[9])
            aba_base.append_row(new_line)    


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


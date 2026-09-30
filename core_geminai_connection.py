from datetime import datetime
import json
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv

client = genai.Client()

def interpretar_mensagem(texto_mensagem: str) -> dict:
    """
    Recebe um texto livre do WhatsApp e retorna um dicionário
    estruturado para inserir na aba BASE PRINCIPAL no Google Sheets.
    """
    data_hoje = datetime.now().strftime("%d%m%Y")

    prompt = f"""
        Você é um assistente financeiro altamente preciso.
        Sua tarefa é extrair informações de mensagem enviadas por um usuário do whatspp e organizá-las.

        Data de hoje para referência: {data_hoje}

        Mensagem do usuário: "{texto_mensagem}"
        Você DEVE retornar APENAS objeto JSON com as seguintes chaves exatas:
        -"Item": Nome curto ou descrição do item/serviço.
        -"Valor": Valor númerico(ex.: 45.50). apenas números int/float.
        -"Categoria": Classifique em uma destas: Alimentação, Transporte, Moradia, Lazer, Compras, Saúde, Eletrônicos, Serviços, Outros.
        -"Tipo": "Sáida" (se for gasto/despesas) ou "Entrada" (se PIX, Sálario,rendimentos)
        -"Parcelado": "Sim" ou "Não".
        -"Parcela": "Texto informando quantas parcelas, se não informar nada é apenas 1/1".

        Exemplo de Saída esperada:
        {{
            "item": "Boné",
            "valor": 250.50,
            "categoria": "Compras",
            "tipo": "Saída",
            "parcelado": "Não",
            "parcela"; "0"
        }}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(  
                response_mime_type="application/json",
                temperature=0.1
            )
        )
        dados = json.load(response.text)
        return dados
    except Exception as e:
        print(f"Erro ao processar mensagem com Gemini: {e}")
    return None

#BLOCO DE TESTES 
if __name__ == "__main__":
    mensagem_teste = "Comprei uma bicicleta parcelada em 8x"
    print(f" Testante frase: '{mensagem_teste}'\n")

    resultado = interpretar_mensagem(mensagem_teste)
    print(" Resposta estruturada do Gemini:")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
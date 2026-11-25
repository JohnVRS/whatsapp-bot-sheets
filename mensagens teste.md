curl -i -X POST http://127.0.0.1:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "object": "whatsapp_business_account",
    "entry": [{
      "id": "123456789",
      "changes": [{
        "value": {
          "messaging_product": "whatsapp",
          "metadata": {
            "display_phone_number": "15550001234",
            "phone_number_id": "10987654321"
          },
          "contacts": [{
            "profile": { "name": "Vitor" },
            "wa_id": "5551999999999"
          }],
          "messages": [{
            "from": "5551999999999",
            "id": "wamid.HBgNNTU1MTk5OTk5OTk5ORUCABIY...",
            "timestamp": "1731530000",
            "text": { "body": "Fiz rancho com 500 reais parcelado " },
            "type": "text"
          }]
        },
        "field": "messages"
      }]
    }]
  }'


  curl -i -X POST http://127.0.0.1:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "object": "whatsapp_business_account",
    "entry": [{
      "id": "123456789",
      "changes": [{
        "value": {
          "messaging_product": "whatsapp",
          "metadata": {
            "display_phone_number": "15550001234",
            "phone_number_id": "10987654321"
          },
          "statuses": []
        },
        "field": "messages"
      }]
    }]
  }'
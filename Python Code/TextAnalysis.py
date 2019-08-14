import http.client, urllib.request, urllib.parse, urllib.error, base64, json.encoder

AzureEndPoint = "{Your-API-EndPoint}"
API_Key = "{Your-API-Key}"

headers = {
    # Request headers
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": API_Key,
}

params = urllib.parse.urlencode({})

body = json.dumps(
    {
        "documents": [
            {"id": "1", "text": "Hello world"},
            {"id": "2", "text": "Bonjour tout le monde"},
            {
                "id": "3",
                "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer.",
            },
            {"id": "4", "text": ":) :( :D"},
        ]
    }
)

try:
    conn = http.client.HTTPSConnection(AzureEndPoint)
    conn.request("POST", "/text/analytics/v2.0/languages?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

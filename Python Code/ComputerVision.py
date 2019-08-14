import http.client, urllib.request, urllib.parse, urllib.error, base64, time, json

AzureEndPoint = "{Your-API-EndPoint}"
API_Key = "{Your-API-Key}"

headers = {
    # Request headers
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": API_Key,
}

params = urllib.parse.urlencode(
    {
        # Request parameters
        "mode": "Printed"
    }
)

body = open(
    "C:\\Users\\mikeho\\OneDrive\\Documents\\Coast Meetup Demo\\Sample Data\\Computer Vision\\ShakespeareSonnet.png",
    "rb",
)

try:
    conn = http.client.HTTPSConnection(AzureEndPoint)
    conn.request("POST", "/vision/v2.0/recognizeText?%s" % params, body, headers)
    response = conn.getresponse()
    textRespponseOperationlocation = response.headers["Operation-Location"]
    print(textRespponseOperationlocation)
    conn.close

    time.sleep(3)

    conn = http.client.HTTPSConnection(AzureEndPoint)
    conn.request(
        "GET",
        textRespponseOperationlocation,
        body=None,
        headers={"Ocp-Apim-Subscription-Key": API_Key},
    )
    response = conn.getresponse()
    data_string = response.read().decode("utf-8")
    json_data = json.loads(data_string)

    for result in json_data["recognitionResult"]["lines"]:
        print(result["text"])
    conn.close()

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

import http.client, urllib.request, urllib.parse, urllib.error, base64

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
        "returnFaceId": "true",
        "returnFaceLandmarks": "false",
        "returnFaceAttributes": "age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise",
        "recognitionModel": "recognition_01",
        "returnRecognitionModel": "false",
        "detectionModel": "detection_01",
    }
)

body = open(
    "C:\\Users\\mikeho\\OneDrive\\Documents\\Coast Meetup Demo\\Sample Data\\Face Detect\\face0.jpg",
    "rb",
)

try:
    conn = http.client.HTTPSConnection(AzureEndPoint)
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

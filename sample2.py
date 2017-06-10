import sys
import requests

url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'b2670446099e461eb1e4ade6da59ac62',
}
params = {
    'returnFaceId': 'true',  # The default value is true.
    'returnFaceLandmarks': 'false', # The default value is false.
    'returnFaceAttributes': 'age,gender', # age, gender, headPose, smile, facialHair, and glasses.
}
if __name__ == '__main__':
    argv = sys.argv
    if len(argv) == 1:
        print('Usage: # python %s [filename]' % argv[0])
        quit()
    r = requests.post(url ,headers = headers,params = params,data = open(argv[1],'rb'))

    print(r.text)
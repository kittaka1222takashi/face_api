import cognitive_face as CF
import sys,json,os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

KEY = os.environ.get("FACE_API_KEY")
CF.Key.set(KEY)

BASE_URL = os.environ.get("BASE_URL")
CF.BaseUrl.set(BASE_URL)

# img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
if __name__ == '__main__':
    argv = sys.argv
    if len(argv) == 1:
        print('Usage: # python %s [filename]' % argv[0])
        quit()
    img_url = open(argv[1],'rb')
    result = CF.face.detect(img_url, face_id=True)

    prsonId = os.environ.get("NONOKA_PERSON_ID")
    prsonGroupId = os.environ.get("PERSON_GROUP_ID")
    result2 = CF.face.verify(result[0]['faceId'],another_face_id=None,person_group_id=prsonGroupId, person_id=prsonId)
    print(result2)
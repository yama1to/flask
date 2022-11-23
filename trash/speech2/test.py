import requests
import os 

cwd = os.getcwd()

class Message:
    def __init__(self):
        # self.accessURL = "http://localhost:8000/speech"
        self.accessURL = "http://3.101.142.253:80/"


    def put_wav(self, user_id, key):
        fileName = cwd + '/app/static/audio/fireball.wav'
        print(fileName)
        files = {'upload-file': open(fileName, 'rb')}
        r = requests.post(self.accessURL,files=files)
        print(r.text)

if __name__ == "__main__":
    message = Message()
    message.put_wav(user_id="user_id", key="key")



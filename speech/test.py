import requests
import os 

# cwd = os.getcwd()

class Message:
    def __init__(self):
        # self.accessURL = "http://localhost:8000/speech"
        self.accessURL = "http://184.72.7.208/"


    def put_wav(self, user_id, key):
        fileName = './app/static/audio/fireball.wav'
        files = {'upload-file': open(fileName, 'rb')}
        r = requests.post(self.accessURL,files=files)
        print(r.text)

if __name__ == "__main__":
    message = Message()
    message.put_wav(user_id="user_id", key="key")



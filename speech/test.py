import requests

class Message:
    def __init__(self):
        self.accessURL = "http://127.0.0.1:5000/speech"


    def put_wav(self, user_id, key):
        fileName = '/Users/sakino/Program/flask/speech/app/static/audio/fireball.wav'
        files = {'upload-file': open(fileName, 'rb')}
        r = requests.post(self.accessURL,files=files)
        print(r.text)

if __name__ == "__main__":
    message = Message()
    message.put_wav(user_id="user_id", key="key")



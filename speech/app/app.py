#Flaskとrender_template（HTMLを表示させるための関数）をインポート
# ssh -i ~/.ssh/speech.pem ec2-user@ec2-54-176-69-188.us-west-1.compute.amazonaws.com
from flask import Flask,render_template,request,jsonify
import wave
from io import BytesIO
import os
import matplotlib.pyplot as plt 
import matplotlib
import numpy as np 
import datetime
matplotlib.use('agg')

def string_now():
    t1=datetime.datetime.now()
    s=t1.strftime('%Y%m%d_%H%M%S')
    return s

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"
@app.route("/sample")
def sample():
    return render_template("sample.html",)

@app.route("/a")
def a():
    return render_template("a.html",)

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/speech")
def index():

    return render_template("index.html",)

#以下を追加
@app.route("/speech",methods=["post"])
def post():
    print("---------------------------------")
    print('request.method', request.method)
    print('request.args', request.args)
    print('request.form', request.form)
    print('request.files', request.files)
    # wavdata = request.files["file"].stream
    # print(request.files.get('file', None))
    # print(request.files.get('form', None))
    if request.files !=None:
        wavdata = request.files.get('upload-file', None)
    else:
        wavdata = uploaded_wav()


    DIR = "./static/images/"
    NOW = string_now()
    fname_wave = NOW + "wave.png"
    fname_cochlear = NOW + "coch.png"

    from wav2coch import wav2coch
    coch,shape_cochlear = wav2coch(wav=wavdata,NOW=NOW)

    from predict import predict
    output = predict(coch,shape_cochlear)


    print("---------------------------------")
    return render_template("index.html", fig_wave=fname_wave,fig_cochlear=fname_cochlear,output=output)

def uploaded_wav():
    fname = "./app/static/audio/" + datetime.now().strftime('%m%d%H%M%S') + ".wav"
    with open(f"{fname}", "wb") as f:
        f.write(request.files['data'].read())
    print(f"posted sound file: {fname}")
    return fname

#おまじない
if __name__ == "__main__":
    app.run(debug=True)



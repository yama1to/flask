#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request
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


    wavdata = request.files.get('upload-file', None)

    DIR = "./app/static/images/"
    NOW = string_now()
    fname_wave = NOW + "wave.png"
    fname_cochlear = NOW + "coch.png"

    from app.wav2coch import wav2coch
    coch,shape_cochlear = wav2coch(wav=wavdata,NOW=NOW)

    from app.predict import predict
    output = predict(coch,shape_cochlear)


    print("---------------------------------")
    return render_template("index.html", fig_wave=fname_wave,fig_cochlear=fname_cochlear,output=output)



#おまじない
if __name__ == "__main__":
    app.run(debug=True)


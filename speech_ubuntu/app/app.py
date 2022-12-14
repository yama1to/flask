#Flaskとrender_template（HTMLを表示させるための関数）をインポート
# ssh -i ~/.ssh/speech.pem ec2-user@ec2-54-176-69-188.us-west-1.compute.amazonaws.com
from flask import Flask,render_template,request,jsonify,flash,redirect
import os
import datetime
import matplotlib
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
matplotlib.use('agg')

import config
from wav2coch import wav2coch
from predict import predict

ALLOWED_EXTENSIONS = {'wav'}
#Flaskオブジェクトの生成
app = Flask(__name__)
app.secret_key = config.Config().SECRET_KEY


def string_now():
    t1=datetime.datetime.now()
    s=t1.strftime('%Y%m%d_%H%M%S')
    return s

def uploaded_wav():
    fname = "/static/audio/" + datetime.now().strftime('%m%d%H%M%S') + ".wav"
    with open(f"{fname}", "wb") as f:
        f.write(request.files['data'].read())
    print(f"posted sound file: {fname}")
    return fname

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return render_template("index.html",)


#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/speech")
def index():

    return render_template("speech.html",)

#以下を追加
@app.route("/speech",methods=["post"])
def post():
    print("---------------------------------")
    print('request.method', request.method)
    print('request.args', request.args)
    print('request.form', request.form)
    print('request.files', request.files)

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if not file.filename:
        flash('No selected file')
        return redirect(request.url)
    
    if not allowed_file(file.filename):
        flash('Fix extension of the file')
        return redirect(request.url)

    if file:
        wavdata = request.files.get('file', None)
    else:
        wavdata = uploaded_wav()

    
    print('------------------')
    print(wavdata)
    print('------------------')

    NOW = string_now()
    fname_wave = NOW + "wave.png"
    fname_cochlear = NOW + "coch.png"

    
    coch,shape_cochlear = wav2coch(wav=wavdata,NOW=NOW)

    
    output = predict(coch,shape_cochlear)


    print("---------------------------------")
    return render_template("speech.html", fig_wave=fname_wave,fig_cochlear=fname_cochlear,output=output)



#おまじない
if __name__ == "__main__":
    app.run(debug=True)



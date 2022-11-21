import argparse
from cProfile import run
from fileinput import filename
import numpy as np
import sys
import os
from copyreg import pickle
import datetime 
import pickle
import os

fname = '20221119_075512_main_speech5_esn.pickle'
# cwd = "/Users/sakino/Program/flask/speech2/app/"
cwd = "/var/www/app/"
def predict(cochlear,shape):
    c=Config()

    model = load_model(fname)
    prediction = run_model(c,model,cochlear)

    return prediction


def load_model(filename):
    # print(filename)

    with open(cwd + 'models/'+filename, mode='rb') as f:
        model = pickle.load(f)
    return model


def run_model(c,model,UP,mode="test"):
    from tqdm import tqdm
    """
    UP: 入力信号の時系列
    DP: ターゲットの時系列
    Ndata:データ（発話）の数
    Nstep:１つのデータ（発話）あたりの時間ステップ数
    mode:{test,train}
    """
  
    collect_state_matrix = np.empty((c.Nh))

    model.run_network(UP,None)
    collect_state_matrix = model.Hp

    Y_pred = collect_state_matrix @ model.Wo.T 

    prediction = np.zeros((c.Ny))
    
    tmp = Y_pred[:]  # 1つのデータに対する出力
    max_index = np.argmax(tmp, axis=1) # 最大出力を与える出力ノード番号
    histogram = np.bincount(max_index) # 出力ノード番号のヒストグラム
    idx = np.argmax(histogram)
    prediction[idx] = 1             # 最頻値

    return np.argmax(prediction)#,dp

class Config():
    def __init__(self):
        # columns, csv, id: データの管理のために必須の変数
        self.columns = None # 結果をCSVに保存する際のコラム
        self.csv = None # 結果を保存するファイル
        self.id  = None
        self.plot = 1 # 図の出力のオンオフ
        self.show = False # 図の表示（plt.show()）のオンオフ、explorerは実行時にこれをオフにする。
        self.savefig = False
        self.fig1 = "fig1.png" ### 画像ファイル名
        

        # config
        self.do_not_use_tqdm = 0
        self.dataset=6
        self.seed:int=1 # 乱数生成のためのシード
        self.MM=50 # サイクル数
        self.MM0 = 0 #

        self.Nu = 77         #size of input
        self.Nh:int = 300   #815 #size of dynamical reservior
        self.Ny = 10        #size of output

        #sigma_np = -5
        self.alpha_i = 0.9
        self.alpha_r = 0.9
        self.alpha_b = 0.

        self.alpha0 = 1#0.1
        self.alpha1 = 1#-5.8

        self.beta_i = 0.9
        self.beta_r = 0.05
        self.beta_b = 0.

        self.lambda0 = 0.

        # ResultsX
        self.trainWSR = None
        self.WSR = None
        self.cnt_overflow=None
import numpy as np
import matplotlib.pyplot as plt
import os
import wave 
import random #リストのshuffleで使用する
from app.lyon.lyon.calc import LyonCalc

config_lyon={"sample_rate":12500, "decimation_factor":200, "ear_q":3, "step_factor":0.091, "tau_factor":3}
DIR = "./app/static/images/"

def wav2coch(wav,NOW):
    coch,shape = generate_cochleagram(wav,config_lyon,NOW)
    return coch,shape


def generate_cochleagram(wave,cl,NOW):
    calc = LyonCalc()
    coch = np.empty((0,0))

    wave = load_wave(wave,NOW)
    # wave = load_wave(wav)
    c = calc.lyon_passive_ear(wave, sample_rate=cl["sample_rate"], decimation_factor=cl["decimation_factor"], ear_q=cl["ear_q"], step_factor=cl["step_factor"], tau_factor=cl["tau_factor"])      
    coch = np.append(coch,c,axis=0) if not coch.shape == (0,0) else c
    #print(coch.shape)
    save_coch(c,NOW=NOW)
    return coch,c.shape # 連結したcochleagramと、データ１つ分のcochleagramのshapeを返す


def load_wave(file,NOW):

    with wave.open(file,mode='r') as W:
        W.rewind()
        buf = W.readframes(-1)  # read allA
        #16bitごとに10進数
        wa = np.frombuffer(buf,dtype='int16').astype(np.float64)
    wa = cut(wa)

    save_wave(wa,NOW)
    return wa

def save_wave(wave,NOW):
    file = DIR + NOW+"wave.png"
    plt.plot(wave)
    plt.savefig(file)
    plt.clf()
    plt.close()

def save_coch(c,NOW):
    file = DIR + NOW+"coch.png"
    plt.imshow(c.T)
    plt.savefig(file)
    plt.clf()
    plt.close()

def cut(wave):
    len_output=10000 # 出力波形の長さ
    count = 0
    start = 0
    for i in range(len(wave)):
        if np.fabs(wave[i]) > 200:
            count += 1
            if count==10:
                start = i
                break 

    start = i-2500
    start = max(start,0)
    end = min(len_output+start,wave.shape[0])
    output = np.zeros(len_output)
    output[:end-start] = wave[start:end]
    return output
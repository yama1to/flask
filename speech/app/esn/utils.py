# Copyright (c) 2022 Katori lab. All Rights Reserved
import numpy as np
import matplotlib.pyplot as plt
from explorer.common import prepare_directory,string_now

from copyreg import pickle
import datetime 
import pickle
import os

prepare_directory('./trashfigure')
prepare_directory('./models')

def save_model(model,fname=__file__):
    with open("./models/"+string_now()+"_"+file_name(fname)+'.pickle', mode='wb') as f:
        pickle.dump(model,f,protocol=2)
    

def load_model(filename):
    with open('./models/'+filename, mode='rb') as f:
        model = pickle.load(f)
    return model

def file_name(fname):
    return os.path.basename(str(os.path.splitext(fname)[0]))


def fy(h):
    return np.tanh(h)

def fyi(h):
    return np.arctanh(h)

def p2s(theta,p):
    return np.heaviside( np.sin(np.pi*(2*theta-p)),1)


def plot1(Up,Hp,Yp,Dp,show = 1,save=1,dir_name = "trashfigure",fig_name="fig1"):
    fig=plt.figure(figsize=(16, 8))
    Nr=6
    ax = fig.add_subplot(Nr,1,1)
    ax.cla()
    ax.set_title("Up")
    ax.plot(Up)

    ax = fig.add_subplot(Nr,1,2)
    ax.cla()
    ax.set_title("Hp")
    ax.plot(Hp)

    ax = fig.add_subplot(Nr,1,3)
    ax.cla()
    ax.set_title("Yp")
    ax.plot(Yp)
    #ax.plot(y)

    ax = fig.add_subplot(Nr,1,4)
    ax.cla()
    ax.set_title("Dp")
    ax.plot(Dp)

    
    if save:plt.savefig("./{}/{}".format(dir_name,fig_name))
    if show:plt.show()

def plot2(Up,Hp,Yp,Dp,show = 1,save=1,dir_name = "trashfigure",fig_name="fig1"):
    fig=plt.figure(figsize=(20, 12))
    Nr=4
    ax = fig.add_subplot(Nr,1,1)
    ax.cla()
    #ax.set_title("input")
    ax.plot(Up)

    ax = fig.add_subplot(Nr,1,2)
    ax.cla()
    #ax.set_title("decoded reservoir states")
    ax.plot(Hp)

    ax = fig.add_subplot(Nr,1,3)
    ax.cla()
    #ax.set_title("predictive output")
    #ax.plot(train_Y)
    ax.plot(Yp)

    ax = fig.add_subplot(Nr,1,4)
    ax.cla()
    #ax.set_title("desired output")
    ax.plot(Dp)
    if show :plt.show()
    if save:plt.savefig("./{}/{}".format(dir_name,fig_name))


def calc_MC(Yp,Dp,delay):
    DC = np.zeros(delay)
    for k in range(delay):
        corr = np.corrcoef(np.vstack((Dp.T[k, k:], Yp.T[k, k:])))   #相関係数
        DC[k] = corr[0, 1] ** 2    #決定係数 = 相関係数 **2
    MC = np.sum(DC)
    return DC,MC

def plot_MC(Yp,Dp,delay=20,show = 1,save=1,dir_name = "trashfigure",fig_name="mc1"):               
    DC,MC = calc_MC(Yp,Dp,delay)
    plt.plot(DC)
    plt.ylabel("determinant coefficient")
    plt.xlabel("Delay k")
    plt.ylim([0,1])
    plt.xlim([0,delay])
    plt.title('MC ~ %3.2lf' % MC, x=0.8, y=0.7)
    if save:plt.savefig("./{}/{}".format(dir_name,fig_name))
    if show :plt.show()
    
def plot_delay(DC,N,pred,target,):
    fig=plt.figure(figsize=(8,8 ))
    Nr=N
    start = 0
    for i in range(Nr):
        ax = fig.add_subplot(Nr,1,i+1)
        ax.cla()
        ax.set_title("DC = %2f,delay = %s" % (DC[i],str(i)))
        ax.plot(pred.T[i,i:])
        ax.plot(target.T[i,i:])
    plt.show()
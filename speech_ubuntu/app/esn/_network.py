# Copyright (c) 2022 Katori lab. All Rights Reserved
import numpy as np
from esn.generate_matrix import *
from tqdm import tqdm


class EchoStateNetwork():
    def __init__(self,columns = None,csv = None,id  = None,
                plot = 1,show = False,savefig = False,fig1 = "fig1.png",
                dataset=6,seed:int=0,
                MM=2200,MM0 = 200,Nu = 1,Nh:int = 100,Ny = 20,
                Temp=1,alpha_i = 0.24,alpha_r = 0.7,alpha_b = 0.,
                alpha0=0,alpha1=1,

                beta_i = 0.9,beta_r = 0.2,beta_b = 0.,lambda0 = 0.,do_not_use_tqdm = 0):
        self.columns = columns # 結果をCSVに保存する際のコラム
        self.csv = csv # 結果を保存するファイル
        self.id  = id
        self.plot = plot # 図の出力のオンオフ
        self.show = show # 図の表示（plt.show()）のオンオフ、explorerは実行時にこれをオフにする。
        self.savefig = savefig
        self.fig1 = fig1 ### 画像ファイル名

        # config
        self.dataset=dataset
        self.seed:int=seed # 乱数生成のためのシード
        self.MM=MM # サイクル数
        self.MM0 = MM0 #

        self.Nu = Nu         #size of input
        self.Nh:int = Nh   #815 #size of dynamical reservior
        self.Ny = Ny        #size of output

        #sigma_np = -5
        self.alpha_i = alpha_i
        self.alpha_r = alpha_r
        self.alpha_b = alpha_b

        self.alpha0 = alpha0#0.1
        self.alpha1 = alpha1#-5.8

        self.beta_i = beta_i
        self.beta_r = beta_r
        self.beta_b = beta_b

        self.lambda0 = lambda0
        self.do_not_use_tqdm = do_not_use_tqdm



    def generate_network(self,):
        np.random.seed(seed=self.seed)
        self.Wr = generate_random_matrix(self.Nh,self.Nh,self.alpha_r,self.beta_r,distribution="one",normalization="sr",diagnal=0)

        #Wr = bm_weight()
        #Wr = ring_weight()
        #Wr = small_world_weight()
        self.Wb = generate_random_matrix(self.Nh,self.Ny,self.alpha_b,self.beta_b,distribution="one",normalization="none")
        self.Wi = generate_random_matrix(self.Nh,self.Nu,self.alpha_i,self.beta_i,distribution="one",normalization="none")
        self.Wo = np.zeros(self.Nh * self.Ny).reshape((self.Ny, self.Nh))

    def fit(self,train_data,target_data):
        self.run_network(train_data,target_data)
        self.regression(self.Hp,target_data)
    
    def regression(self,reservoir_state,target_data):
        M = reservoir_state[self.MM0:, :]
        G = target_data[self.MM0:, :]

        ### Ridge regression
        if self.lambda0 == 0:
            self.Wo = np.dot(G.T,np.linalg.pinv(M).T)
            #print("a")
        else:
            E = np.identity(self.Nh)
            TMP1 = np.linalg.inv(M.T@M + self.lambda0 * E)
            WoT = TMP1@M.T@G
            self.Wo =WoT.T
    
    def validate(self,train_data,target_data):
        self.run_network(train_data,target_data)
    
    def run_network(self,train_data,target_data):
        self.Hp = np.zeros((self.MM, self.Nh))
        self.Yp = np.zeros((self.MM, self.Ny))
        #x = np.random.uniform(-1, 1, Nh)/ 10**4
        x = np.zeros(self.Nh)
        

        for n in range(self.MM):
            
            u = train_data[n, :]

            #Hp[n+1,:] = x + 1.0/tau * (-alpha0 * x + fx(Wi@u + Wr@x))
            next_x = (1 - self.alpha0) * x + self.alpha0*np.tanh(self.Wi@u + self.Wr@x)
            self.Hp[n,:] = next_x
            self.Yp[n] = self.Wo @ next_x
            x= next_x
          
    
    def show_recode(self,):
        return self.Hp[self.MM0:],self.Yp[self.MM0:]




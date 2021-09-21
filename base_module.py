import os
import numpy as np
import matplotlib.pyplot as plt
import abc


class SimulateMLE(metaclass=abc.ABCMeta):
    def __init__(self, theta_0, thetas, n=10, N=10000, Ns=None, seed=9, **kwargs):
        # 固定生成分布的参数值
        self.theta_0 = theta_0
        # 参数值的选择区间
        self.thetas = thetas
        # 最大样本数,默认10000（取不到）
        self.N = N
        # 成长倍率，默认为10
        self.n = n
        # 成长基数，默认[1,2,5]
        self.Ns = Ns if Ns else [1, 2, 5]
        # 固定随机种子
        self.seed = seed
        # 存储生成的随机数
        self.path = './data'
        # 函数中其他的固定数
        self.params = kwargs
        # 分布名称
        self.name=''

    @abc.abstractmethod
    def get_rv_function(self):
        raise TypeError("get_rv_function must be define")

    @abc.abstractmethod
    def get_rv_probability(self):
        raise TypeError("get_rv_probability must be define")

    @abc.abstractmethod
    def get_rv_ppf(self):
        raise TypeError("get_rv_ppf must be define")

    def show_pdf(self):
        ppf=self.get_rv_ppf()
        pdf=self.get_rv_probability()
        x=np.linspace(ppf(0.01,self.theta_0),
                      ppf(0.99,self.theta_0),1000)
        plt.figure()
        plt.plot(x,pdf(x,self.theta_0))
        plt.title(f'{self.name} pdf')
        plt.show()

    def gen_rv_num(self, size):
        rv_function = self.get_rv_function()
        res = rv_function(self.theta_0, size=size,random_state=self.seed)
        np.save(os.path.join(self.path, f'size_{size}.npy'), res)

    def gen_rv_probability(self, size):
        rv_prob_function = self.get_rv_probability()
        points = np.load(os.path.join(self.path, f'size_{size}.npy'))
        res = []
        for theta in self.thetas:
            prob = [rv_prob_function(i, theta) for i in points]
            prob=np.log(prob)
            res.append(sum(prob))
        np.save(os.path.join(self.path, f'res_size_{size}.npy'),res)

    def plot_fig(self, size):
        res = np.load(os.path.join(self.path, f'res_size_{size}.npy'))
        plt.title(f"{self.name}  N={size}")
        plt.xlabel(r'$\theta$')
        plt.ylabel('log likelihood')
        plt.vlines(self.theta_0,ymin=np.min(res),ymax=np.max(res),colors='r',linestyles='--')
        plt.plot(self.thetas,res)
        plt.pause(0.5)
        plt.clf()

    def loop(self,func):
        stop = 1
        while stop < self.N:
            for j in self.Ns:
                size = stop * j
                func(size)
            stop*=self.n


    def main(self):
        print("正在生成样本...")
        self.loop(self.gen_rv_num)
        print("正在计算似然函数...")
        self.loop(self.gen_rv_probability)
        plt.figure()
        for i in range(3):
            plt.ion()
            self.loop(self.plot_fig)
            plt.ioff()
        plt.show()
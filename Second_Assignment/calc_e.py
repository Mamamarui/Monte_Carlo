import os
import sys
import random
import numpy as np
import math
import matplotlib.pyplot as plt

def calc_e(num):
    selected = []
    for i in range(num):
        xi = random.random()
        X = xi//(1/num)
        selected.append(X)
    selected.sort()
    counter = 0
    for index,item in enumerate(selected):
        if index == 0:
            counter += 1
        elif item != selected[index-1]:
            counter += 1
    e = 1/((num-counter)/num)
    return e

def estimate_e(N,num):
    e = np.zeros(N) 
    for i in range(N):
        e[i] = calc_e(num)
    return e

def main():
    num = int(sys.argv[1])
    N = int(sys.argv[2])
    e = estimate_e(N,num)
    draw(num)
    print("The estimate value of e : %10.8f" %e.mean())
    print("The estimate variance : %f" %e.var())

def draw(num):
    test_num = [2,5,10,20,50,100,200,500,1000]
    e_ave = []
    e_var = []
    for i in range(len(test_num)):
        e = estimate_e(test_num[i],num)
        e_ave.append(e.mean())
        e_var.append(e.var())
    x = [0,2000]
    y = [math.exp(1),math.exp(1)]
    plt.semilogx(x,y,"red")
    plt.errorbar(test_num,e_ave,yerr = e_var,color="blue",ecolor="black",fmt="-o",capsize=4)
    plt.xlabel("Number of Sample")
    plt.ylabel("The value of e")
    plt.xlim([-30,1500])
    plt.title("Monte Carlo Estinates of e")
    plt.show()


if __name__ == "__main__":
    main()

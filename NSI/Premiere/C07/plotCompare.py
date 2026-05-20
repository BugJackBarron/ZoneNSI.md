#!/usr/bin/env python 
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pickle
import numpy as np
import time

if __name__ == "__main__" :
    with open("compareGreedyNatural.dat","rb") as file :
        nt,gt,vn,vt = pickle.load(file)
        
        a221 = plt.subplot(231)
        a222 = plt.subplot(232)
        a223 = plt.subplot(233)
        for i in range(1,len(nt)) :
            a221.plot(nt[:i])
            a222.plot(gt[:i])
            a223.plot(nt[:i])
            a223.plot(gt[:i])
            plt.pause(0.5)
        
        plt.show()


# -*- coding: utf-8 -*-
"""
E12系列の抵抗値がどんな仕組みで決まっているのか
https://synapse.kyoto/tips/E_series/page001.html
http://sim.okawa-denshi.jp/keiretu.htm
"""

import numpy as np
import matplotlib.pyplot as plt


def getValue(n, E_series):
    return (10**n)**(1/E_series)

y = np.array([round(getValue(n,12),2) for n in range(30)])
x = np.arange(len(y))

plt.grid()
plt.yscale("log")
plt.scatter(x,y)

print(y[:12])

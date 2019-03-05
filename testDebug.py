import algoDis
import dataCenter
import dataViz
import pandas as pd
import twoGrams
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import multiprocessing
import math
import time

def call_back(event):
    # if event.button=='down':
    #     print('button down')
    print(event.key)

# 这个文件就是用来debug的
if __name__ == "__main__":

    # 测试debug专用
    fig = plt.figure()  # 创建一个没有 axes 的 figure
    fig.suptitle('No axes on this figure')  # 添加标题以便我们辨别

    fig, ax_lst = plt.subplots(2, 2)  # 创建一个以 axes 为单位的 2x2 网格的 figure
    fig.canvas.mpl_connect('button_press_event', call_back)
    plt.show()
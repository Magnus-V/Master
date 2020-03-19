import mglearn as mglearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy as sp

def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value'):
    plt.figure(figsize=(16,5))
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()


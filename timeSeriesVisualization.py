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

def plot_df_2(df):
    plt.figure(figsize=(20, 8))
    plt.plot(df['aargang'], df['saminnt_1'], 'b-', label = 'Samlet inntekt')
    plt.plot(df['aargang'], df['hels1'], 'r-', label = 'Health')
    plt.xlabel('Date'); plt.ylabel('Value'); plt.title('DaFreek')
    plt.legend()

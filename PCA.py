import os

import mglearn as mglearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy as sp
import sklearn
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def runPCAAnalysisOnScaledData(data):
    pca = PCA(n_components=2)
    x_pca = pca.fit_transform(data)
    print("Orignal shape: {}".format(str(data.shape)))
    print("Reduced shape: {}".format(str(x_pca.shape)))
    plt.figure(figsize=(8, 8))
    mglearn.discrete_scatter(x_pca[:, 0], x_pca[:, 1])
    plt.show()
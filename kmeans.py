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

def runKMeansOnScaledData(data):
    kmeans = KMeans(n_clusters=10)
    y_kmeans = kmeans.fit_predict(data)
    plt.scatter(data[:, 0], data[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 1], centers[:, 2], c='black', s=200, alpha=0.5)
    plt.show()
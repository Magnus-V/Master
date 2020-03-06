import columnsToEngineer
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
from sklearn.feature_selection import SelectPercentile
from sklearn.model_selection import train_test_split

def split_train_test(dataFrame):
    return

def selectKBestUsingData(X_train, x_test):
    select = SelectPercentile(percentile=50)
    select.fit()
    X_train_selected = select.transform(X_train)
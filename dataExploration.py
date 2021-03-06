import os
import columnsToEngineer
import mglearn as mglearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy as sp
import sklearn
from pandas import plotting
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import dataExtract
import kmeans
import PCA
import columnsToEngineer
import numpy as np
import seaborn as sns

df2017 = dataExtract.EUSILC2017
df2017 = dataExtract.readCSVSurveyConvertToDataFrame(df2017)
df2017filtered = dataExtract.filterOutDatasetOnListOfConditions(df2017, columnsToEngineer.createArrayOfConditions2017())

plotting.scatter_matrix(df2017filtered, figsize=(15,15), marker='o', hist_kwds={'bins': 14},
                        s=60, alpha=0.8, cmap=mglearn.cm3)


def heatmapCorrelation(dataFrame):
    corrmat = dataFrame.corr()
    top_corr_features = corrmat.index
    plt.figure(figsize=(20,20))
    #plot heat map
    g=sns.heatmap(dataFrame[top_corr_features].corr(),annot=True,cmap="RdYlGn")
    heatmapFigure = g.get_figure()
    heatmapFigure.savefig('heatmap.png', dpi=400)
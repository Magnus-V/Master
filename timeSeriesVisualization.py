import mglearn as mglearn
import pandas as pd
import predictingModel
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


def checkDifferentMethods(df, filter, dropyear):
    print("Linear")
    predictingModel.predictionModelLinearRegression(df, filter, dropyear)
    print("ridge")
    predictingModel.predictionModelRidgeRegression(df, filter, dropyear)
    print("Lasso")
    predictingModel.predictionModelLassoRegression(df, filter, dropyear)
    print("SDG")
    predictingModel.predictionModelSDGRegression(df, filter, dropyear)
    print("RFR")
    predictingModel.predictingRandomForestRegression(df, filter, dropyear)
    print("TR")
    predictingModel.predictingDecisionsTreeRegression(df, filter, dropyear)


def visualizeCoefficients(coefs, names):
    coeff_df = pd.DataFrame(coefs, names, columns=['Coefficient'])
    coeff_df = coeff_df.astype({'Coefficient': int})
    with pd.option_context('display.max_rows', None, 'display.max_columns',
                           None):  # more options can be specified also
        print(coeff_df)


def visualize_coefficients(coefs, names, ax):
    # Make a bar plot for the coefficients, including their names on the x-axis
    ax.bar(coefs, names)
    ax.set(xlabel='Coefficient name', ylabel='Coefficient value')

    # Set formatting so it looks nice
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    return ax
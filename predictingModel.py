import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydot
import sys, os
import scipy as sp
from statsmodels.sandbox.tsa.varma import VAR
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tsa.vector_ar.vecm import coint_johansen
import dataExtract, timeSeriesVisualization
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, SGDRegressor, BayesianRidge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.tree import export_graphviz
from sklearn.metrics import classification_report, confusion_matrix


def predictionModelLinearRegression(dataFrame, label, dropYear):
    X = pd.DataFrame(dataFrame)
    y = pd.DataFrame(dataFrame)
    X = X.drop(columns=label)
    X = X.drop(columns=dropYear)
    #X = dataExtract.insertDataFrameToScale(X)
    #X = dataExtract.insertDataFrameAndNormalize(X)
    y = y[label].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False, random_state=42)
    regressor = LinearRegression(normalize=True)
    regressor.fit(X_train, y_train)
    coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
    coeff_df = coeff_df.astype({'Coefficient':int})
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(coeff_df)
    y_pred = regressor.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(25)

    df1.plot(kind='bar', figsize=(10, 8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


def predictionModelRidgeRegression(dataFrame, label, dropYear):
    X = pd.DataFrame(dataFrame)
    y = pd.DataFrame(dataFrame)
    X = X.drop(columns=label)
    X = X.drop(columns=dropYear)
    #X = dataExtract.insertDataFrameToScale(X)
    #dataExtract.insertDataFrameAndNormalize()
    y = y[label].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False, random_state=42)
    regressor = Ridge()
    regressor.fit(X_train, y_train)
    coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
    coeff_df = coeff_df.astype({'Coefficient':int})
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(coeff_df)
    y_pred = regressor.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(25)

    df1.plot(kind='bar', figsize=(10, 8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

def predictionModelLassoRegression(dataFrame, label, dropYear):
    X = pd.DataFrame(dataFrame)
    y = pd.DataFrame(dataFrame)
    X = X.drop(columns=label)
    X = X.drop(columns=dropYear)
    #X = dataExtract.insertDataFrameToScale(X)
    #X = dataExtract.insertDataFrameAndNormalize(X)
    y = y[label].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False, random_state=42)
    regressor = Lasso()
    regressor.fit(X_train, y_train)
    coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
    coeff_df = coeff_df.astype({'Coefficient':int})
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(coeff_df)
    y_pred = regressor.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(25)

    df1.plot(kind='bar', figsize=(10, 8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

def predictionModelSDGRegression(dataFrame, label, dropYear):
    X = pd.DataFrame(dataFrame)
    y = pd.DataFrame(dataFrame)
    X = X.drop(columns=label)
    X = X.drop(columns=dropYear)
    X = dataExtract.insertDataFrameToScale(X)
    #X = dataExtract.insertDataFrameAndNormalize(X)
    y = y[label].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False, random_state=42)
    regressor = SGDRegressor()
    regressor.fit(X_train, y_train)
    coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
    coeff_df = coeff_df.astype({'Coefficient':int})
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(coeff_df)
    y_pred = regressor.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(25)

    df1.plot(kind='bar', figsize=(10, 8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


def predictingRandomForestRegression(dataFrame, label, dropYear):
    print('\nRandomForestRegression\n')
    X = pd.DataFrame(dataFrame)
    y = pd.DataFrame(dataFrame)
    X = X.drop(columns=label)
    X = X.drop(columns=dropYear)
    feature_list = list(X.columns)
    # X = dataExtract.insertDataFrameToScale(X)
    # X = dataExtract.insertDataFrameAndNormalize(X)
    y = y[label].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False, random_state=42)
    regr1 = RandomForestRegressor()
    regr1.fit(X_train, y_train)
    coeff_df = pd.DataFrame(regr1.feature_importances_, X.columns, columns=['Feature_importance'])
    #coeff_df = coeff_df.astype({'Coefficient': int})
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(coeff_df)
    y_pred1 = regr1.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred1})
    df1 = df.head(25)
    df1.plot(kind='bar', figsize=(10, 8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()

    # Pull out one tree from the forest
    tree = regr1.estimators_[0]  # Export the image to a dot file
    export_graphviz(tree, out_file='tree.dot', feature_names=feature_list, rounded=True,
                    precision=1, )  # Use dot file to create a graph
    #graph,) = pydot.graph_from_dot_file('C:/Users/Magnus L. Vestby/Documents/Universitetsarbeid'
    #                                     '/Master/INFO390/tree.dot')  # Write graph to a png file

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred1))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred1))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred1)))

def predictingDecisionsTreeRegression(dataFrame, label, dropYear):
    print('\nDecisionTreeRegression\n')
    X = pd.DataFrame(dataFrame)
    y = pd.DataFrame(dataFrame)
    X = X.drop(columns=label)
    X = X.drop(columns=dropYear)
    #X = dataExtract.insertDataFrameToScale(X)
    # X = dataExtract.insertDataFrameAndNormalize(X)
    y = y[label].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False, random_state=42)
    regressor1 = DecisionTreeRegressor()
    regressor2 = DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=5, min_samples_split=2,
                                       min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None,
                                       random_state=10, max_leaf_nodes=None, min_impurity_decrease=0.0,
                                       min_impurity_split=None, presort='deprecated', ccp_alpha=0.0)
    regressor1.fit(X_train, y_train)
    regressor2.fit(X_train, y_train)
    coeff_df = pd.DataFrame(regressor1.feature_importances_, X.columns, columns=['Feature_importance'])
    #coeff_df = coeff_df.astype({'Feature_importance': float})
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(coeff_df)
    y_pred1 = regressor1.predict(X_test)
    y_pred2 = regressor2.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred1})
    df1 = df.head(25)

    df1.plot(kind='bar', figsize=(10, 8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()

    print('\nRegr1')
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred1))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred1))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred1)))

    print('\nRegr2')
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred2))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred2))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred2)))


def runRidgePredictionOnYearlyBasis(dataFrame, label, yearFilter, dropYear, dropWorkStatus):
    X = pd.DataFrame(dataFrame)
    X = X[X['aargang'] == yearFilter]
    y = pd.DataFrame(dataFrame)
    y = y[y['aargang'] == yearFilter]
    X = X.drop(columns=[label, dropYear, dropWorkStatus])
    # X = dataExtract.insertDataFrameToScale(X)
    # X = dataExtract.insertDataFrameAndNormalize(X)
    y = y[label].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False, random_state=42)
    regressor = Ridge(alpha=2)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    coeff_df = timeSeriesVisualization.visualize_coefficients(regressor.coef_, X.columns, yearFilter)

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    #print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    #print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    return coeff_df


def runForecastingIntoFuture(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017):
    t1973 = coeff1973.transpose()
    t1983 = coeff1983.transpose()
    t1995 = coeff1995.transpose()
    t2005 = coeff2005.transpose()
    t2013 = coeff2013.transpose()
    t2017 = coeff2017.transpose()
    years = [1973, 1983, 1995, 2005, 2013, 2017]
    dfcombined = pd.concat([t1973, t1983, t1995, t2005, t2013, t2017],
                           ignore_index=False)
    dfcombined.index = years

    # Plot
    fig, axes = plt.subplots(nrows=4, ncols=2, dpi=120, figsize=(10, 6))
    for i, ax in enumerate(axes.flatten()):
        data = dfcombined[dfcombined.columns[i]]
        ax.plot(data, color='red', linewidth=1)
        # Decorations
        ax.set_title(dfcombined.columns[i])
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        ax.spines["top"].set_alpha(0)
        ax.tick_params(labelsize=6)

    plt.tight_layout()

    maxlag = 8
    test = 'ssr_chi2test'

    def grangers_causation_matrix(data, variables, test='ssr_chi2test', verbose=False):
        """Check Granger Causality of all possible combinations of the Time series.
        The rows are the response variable, columns are predictors. The values in the table
        are the P-Values. P-Values lesser than the significance level (0.05), implies
        the Null Hypothesis that the coefficients of the corresponding past values is
        zero, that is, the X does not cause Y can be rejected.

        data      : pandas dataframe containing the time series variables
        variables : list containing names of the time series variables.
        """
        df = pd.DataFrame(np.zeros((len(variables), len(variables))), columns=variables, index=variables)
        for c in df.columns:
            for r in df.index:
                test_result = grangercausalitytests(data[[r, c]], maxlag=maxlag, verbose=False)
                p_values = [round(test_result[i + 1][0][test][1], 4) for i in range(maxlag)]
                if verbose: print(f'Y = {r}, X = {c}, P Values = {p_values}')
                min_p_value = np.min(p_values)
                df.loc[r, c] = min_p_value
        df.columns = [var + '_x' for var in variables]
        df.index = [var + '_y' for var in variables]
        return df

    grangers_causation_matrix(dfcombined, variables=dfcombined.columns)

    def cointegration_test(df, alpha=0.05):
        """Perform Johanson's Cointegration Test and Report Summary"""
        out = coint_johansen(df, -1, 5)
        d = {'0.90': 0, '0.95': 1, '0.99': 2}
        traces = out.lr1
        cvts = out.cvt[:, d[str(1 - alpha)]]

        def adjust(val, length=6): return str(val).ljust(length)

        # Summary
        print('Name   ::  Test Stat > C(95%)    =>   Signif  \n', '--' * 20)
        for col, trace, cvt in zip(df.columns, traces, cvts):
            print(adjust(col), ':: ', adjust(round(trace, 2), 9), ">", adjust(cvt, 8), ' =>  ', trace > cvt)

    cointegration_test(dfcombined)

    X = dfcombined
    model = VAR(X)
    model_fit = model.fit()
    yhat = model_fit.forecast(model_fit.y, steps=1)
    print(yhat)


def runRidgePredictionOnYearlyBasisWithIncomeGroups(dataFrame, label, dropYear, dropWorkStatus, minFactor, maxFactor):
    years = [1973, 1983, 1995, 2005, 2013, 2017]
    coeffArray = []
    for i in range(0, len(years)):
        X = pd.DataFrame(dataFrame)
        X = X[X['aargang'] == years[i]]
        medianIncome = X.saminnt_1.median()
        maxIncome = medianIncome * maxFactor
        minIncome = medianIncome * minFactor
        X = X[(X['saminnt_1'] < maxIncome) & (X['saminnt_1'] > minIncome)]
        print(f'Size of dataset for regression: {X.size}')
        print(f'Max income = {maxIncome}, Min income ={minIncome}, based on a median of '
              f'{medianIncome}')
        medianIncome = X.saminnt_1.median()
        y = X
        X = X.drop(columns=[label, dropYear, dropWorkStatus])
        # X = dataExtract.insertDataFrameToScale(X)
        # X = dataExtract.insertDataFrameAndNormalize(X)
        y = y[label].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=True, random_state=42)
        regressor = Ridge(alpha=2)
        regressor.fit(X_train, y_train)
        y_pred = regressor.predict(X_test)
        coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
        coeff_df = coeff_df.astype({'Coefficient': int})
        coeff_df['MedianIncome'] = medianIncome
        coeffArray.append(coeff_df)
        print(coeff_df)
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))

    timeSeriesVisualization.visualizeTrendsFactoringIncome(coeffArray, dataFrame)
    return coeffArray


def runRidgePredictionOnYearlyBasisAllInOne(dataFrame, label, dropYear, dropWorkStatus):
    years = [1973, 1983, 1995, 2005, 2013, 2017]
    coeffArray = []
    for i in range(0, len(years)):
        X = pd.DataFrame(dataFrame)
        X = X[X['aargang'] == years[i]]
        print(f'Size of dataset for regression: {X.size}')
        y = X
        X = X.drop(columns=[label, dropYear, dropWorkStatus])
        # X = dataExtract.insertDataFrameToScale(X)
        # X = dataExtract.insertDataFrameAndNormalize(X)
        y = y[label].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=True, random_state=42)
        regressor = Ridge(alpha=2)
        regressor.fit(X_train, y_train)
        y_pred = regressor.predict(X_test)
        coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
        coeff_df = coeff_df.astype({'Coefficient': int})
        coeffArray.append(coeff_df)
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))

    # timeSeriesVisualization.visualizeImportanceOfFactor(regressor.coef_, X.columns, dataFrame)
    timeSeriesVisualization.visualizeTrendsFactoringIncome(coeffArray, dataFrame)
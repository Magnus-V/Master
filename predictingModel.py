import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydot
import sys, os
import scipy as sp
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
    regressor = LinearRegression()
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

def predictionModelLassoRegression(dataFrame, label, dropYear, yearToChoose):
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
    #X = dataExtract.insertDataFrameToScale(X)
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

def predictingDecisionsTreeRegression(dataFrame, label, dropYear, dropWorkStatus):
    print('\nDecisionTreeRegression\n')
    X1 = pd.DataFrame(dataFrame)
    X = pd.DataFrame(dataFrame)
    y = pd.DataFrame(dataFrame)
    X = X.drop(columns=label)
    X = X.drop(columns=([dropYear, dropWorkStatus]))
    #X = dataExtract.insertDataFrameToScale(X)
    # X = dataExtract.insertDataFrameAndNormalize(X)
    y = y[label].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False, random_state=42)
    regressor1 = DecisionTreeRegressor(criterion='mse', splitter='best', min_samples_split=2,
                                      min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None,
                                      random_state=10, max_leaf_nodes=None, min_impurity_decrease=0.0,
                                      min_impurity_split=None, presort='deprecated', ccp_alpha=0.0)
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
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(25)

    df1.plot(kind='bar', figsize=(10, 8))
    plt.title(f'Results from year {yearFilter}')
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()

    coeff_df = timeSeriesVisualization.visualize_coefficients(regressor.coef_, X.columns, yearFilter)
    #timeSeriesVisualization.visualizeImportanceOfFactor(regressor.coef_, X.columns, dataFrame)

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    return coeff_df

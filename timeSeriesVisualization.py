import mglearn as mglearn
import pandas as pd
import predictingModel
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import sys
import scipy as sp
from matplotlib import cm


def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value'):
    plt.figure(figsize=(16, 5))
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()


def plot_df_2(df):
    plt.figure(figsize=(20, 8))
    plt.plot(df['aargang'], df['saminnt_1'], 'b-', label='Samlet inntekt')
    plt.plot(df['aargang'], df['hels1'], 'r-', label='Health')
    plt.xlabel('Date');
    plt.ylabel('Value');
    plt.title('DaFreek')
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
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(coeff_df)


def visualize_coefficients(coefs, namesX, year):
    names =['Age', 'Female', 'Male', 'Disability Payment', 'Illness or Injury last 12 months', 'No or pre-school',
            'Primary', 'Lower Secondary', 'Upper Secondary, basic education', 'Upper secondary, final year',
            'Post-secondary non-tertiary', 'First stage of tertiary, undergraduate level',
            'First stage of tertiary, graduate level',
            'Second stage of tertiary (postgraduate)',
            'Unmarried', 'Married/Registered partner', 'Widow/Widower', 'Seperated', 'Divorced']
    posCoefs = coefs.copy()
    negCoefs = coefs.copy()
    posCoefs[posCoefs <= 0] = np.nan
    negCoefs[negCoefs > 0] = np.nan
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_title(f'Coefficient of year {year}')
    rects1 = ax.bar(x=names, height=posCoefs, width=0.8, color="#33ff33")
    rects2 = ax.bar(x=names, height=negCoefs, width=0.8, color="#ff1a1a")
    ax.set_xticklabels(names, rotation=65, ha='right')
    ax.set_ylabel("Coefficient value")
    # Make a bar plot for the coefficients, including their names on the x-axis
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle='-', linewidth='0.5', color='black')


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            height.astype(int)
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    #autolabel(rects1)
    #autolabel(rects2)

    plt.show()
    coeff_df = pd.DataFrame(coefs, namesX, columns=['Coefficient'])
    coeff_df = coeff_df.astype({'Coefficient': int})
    print(coeff_df)
    # coeff_df.plot.bar(rot=0)
    return coeff_df


def visualizeImportanceOfFactor(coef, columns, dataFrame):
    return None



def visualizeTrendsAllInOnePlot(coeffArray, df):
    factorList = ['kjonn_1_1.0', 'kjonn_1_2.0', 'utdnivaa_2.0', 'utdnivaa_5.0', "utdnivaa_6.0"]
    df1973 = df[df['aargang'] == 1973]
    df1983 = df[df['aargang'] == 1983]
    df1995 = df[df['aargang'] == 1995]
    df2005 = df[df['aargang'] == 2005]
    df2013 = df[df['aargang'] == 2013]
    df2017 = df[df['aargang'] == 2017]

    df1973m = int(df1973['saminnt_1'].median())
    df1983m = int(df1983['saminnt_1'].median())
    df1995m = int(df1995['saminnt_1'].median())
    df2005m = int(df2005['saminnt_1'].median())
    df2013m = int(df2013['saminnt_1'].median())
    df2017m = int(df2017['saminnt_1'].median())

    dfs = [df1973, df1983, df1995, df2005, df2013, df2017]
    years = [1973, 1983, 1995, 2005, 2013, 2017]
    means = [df1973m, df1983m, df1995m, df2005m, df2013m, df2017m]


    checkit = pd.DataFrame(columns=['aargang', 'factor', 'percentage'])
    for i in range(0, len(coeffArray)):
        for factor in factorList:
            print(f'\nChanges for {factor} ')
            print(coeffArray[i])
            coeffValue = coeffArray[i][coeffArray[i].index == factor].to_numpy()[0]
            oldValue = means[i]
            newValue = oldValue + coeffValue
            difference = newValue - oldValue
            percentage = int((difference / oldValue) * 100)
            print(f'{years[i]} change in percentage: {percentage}%. N={len(dfs[i])}')
            year = years[i]
            checkit = checkit.append({'aargang': year, 'factor': factor, 'percentage': percentage}, ignore_index=True)
            # Make a bar plot for the coefficients, including their names on the x-axis
            # checkit.plot(x='aargang', y='percentage', kind='line', label="Percentage", title='', style=".-")

    fig, ax = plt.subplots()
    color = ['r', 'b', 'g', 'y', 'c', 'gold', 'teal', 'orchid']
    i = 0
    for factor in factorList:
        tempCheckit = checkit[checkit['factor'] == factor]
        print(tempCheckit)
        print(color[i])
        ax.set_title(f'Difference in of cumulative income based on multiple factors')
        ax.plot(tempCheckit.aargang, tempCheckit.percentage, color=color[i], linestyle="-")
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())
        i = i + 1
    plt.show()

def visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017, df, benchmark, factor):
    df1973 = df[df['aargang'] == 1973]
    df1983 = df[df['aargang'] == 1983]
    df1995 = df[df['aargang'] == 1995]
    df2005 = df[df['aargang'] == 2005]
    df2013 = df[df['aargang'] == 2013]
    df2017 = df[df['aargang'] == 2017]

    df1973m = int(df1973[benchmark].median())
    df1983m = int(df1983[benchmark].median())
    df1995m = int(df1995[benchmark].median())
    df2005m = int(df2005[benchmark].median())
    df2013m = int(df2013[benchmark].median())
    df2017m = int(df2017[benchmark].median())

    dfs = [df1973, df1983, df1995, df2005, df2013, df2017]
    years = [1973, 1983, 1995, 2005, 2013, 2017]
    coeffs = [coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017]
    means = [df1973m, df1983m, df1995m, df2005m, df2013m, df2017m]

    ylim = False
    checkit = pd.DataFrame(columns=['aargang', 'percentage'])
    print(f'\nChanges for {factor} ')
    for i in range(0, len(coeffs)):
        coeffValue = coeffs[i][coeffs[i].index == factor].to_numpy()[0]
        oldValue = means[i]
        newValue = oldValue + coeffValue
        difference = newValue - oldValue
        percentage = int((difference / oldValue) * 100)
        print(f'{years[i]} change in percentage: {percentage}%. N={len(dfs[i])}')
        year = years[i]
        if percentage > 0:
            ylim = True
        checkit = checkit.append({'aargang': year, 'percentage': percentage}, ignore_index=True)

    fig, ax = plt.subplots()
    ax.set_title(f'Difference in of cumulative income based on {factor}')
    ax.plot(checkit.aargang, checkit.percentage, color="#b32400", linestyle="-")

    if not ylim:
        ax.set_ylim(top=0)
    elif ylim:
        ax.set_ylim(auto=True)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    # Make a bar plot for the coefficients, including their names on the x-axis
    # checkit.plot(x='aargang', y='percentage', kind='line', label="Percentage", title='', style=".-")
    plt.show()

def visualizeTrendsFactoringIncome(coeffArray, df):
    factorList = ['kjonn_1_1.0', 'kjonn_1_2.0', 'utdnivaa_2.0', 'utdnivaa_5.0', "utdnivaa_6.0"]
    df1973 = df[df['aargang'] == 1973]
    df1983 = df[df['aargang'] == 1983]
    df1995 = df[df['aargang'] == 1995]
    df2005 = df[df['aargang'] == 2005]
    df2013 = df[df['aargang'] == 2013]
    df2017 = df[df['aargang'] == 2017]

    df1973m = int(df1973['saminnt_1'].median())
    df1983m = int(df1983['saminnt_1'].median())
    df1995m = int(df1995['saminnt_1'].median())
    df2005m = int(df2005['saminnt_1'].median())
    df2013m = int(df2013['saminnt_1'].median())
    df2017m = int(df2017['saminnt_1'].median())

    dfs = [df1973, df1983, df1995, df2005, df2013, df2017]
    years = [1973, 1983, 1995, 2005, 2013, 2017]
    means = [df1973m, df1983m, df1995m, df2005m, df2013m, df2017m]
    checkit = pd.DataFrame(columns=['aargang', 'factor', 'percentage'])

    for i in range(0, len(coeffArray)):
        for factor in factorList:
            print(f'\nChanges for {factor} ')
            coeffValue = coeffArray[i][coeffArray[i].index == factor].to_numpy()[0]
            oldValue = means[i]
            newValue = oldValue + coeffValue
            difference = newValue - oldValue
            percentage = int((difference / oldValue) * 100)
            print(f'{years[i]} change in percentage: {percentage}%.')
            year = years[i]
            checkit = checkit.append({'aargang': year, 'factor': factor, 'percentage': percentage}, ignore_index=True)
            # Make a bar plot for the coefficients, including their names on the x-axis
            # checkit.plot(x='aargang', y='percentage', kind='line', label="Percentage", title='', style=".-")

    fig, ax = plt.subplots(figsize=(10, 10))
    color = ['r', 'b', 'g', 'y', 'c', 'gold', 'teal', 'orchid']
    i = 0
    for factor in factorList:
        tempCheckit = checkit[checkit['factor'] == factor]
        ax.set_title(f'Difference in of cumulative income based on multiple factors')
        ax.plot(tempCheckit.aargang, tempCheckit.percentage, color=color[i], linestyle="-", label=factor)
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())
        i = i + 1
    plt.legend(loc="upper right")
    plt.show()


def visualizeDifferenceForIncomeGroups(lowerClassCoeffArray, middleClassCoeffArray, upperClassCoefArray, df):
    factorList = ['kjonn_1_1.0', 'kjonn_1_2.0', 'utdnivaa_2.0', 'utdnivaa_5.0', "utdnivaa_6.0"]

    for i in range(0, len(lowerClassCoeffArray)):
        print('THIS IS THE ARRAY:')
        print(lowerClassCoeffArray[i].Coefficient)
        print('\n')

    df1973 = df[df['aargang'] == 1973]
    df1983 = df[df['aargang'] == 1983]
    df1995 = df[df['aargang'] == 1995]
    df2005 = df[df['aargang'] == 2005]
    df2013 = df[df['aargang'] == 2013]
    df2017 = df[df['aargang'] == 2017]

    df1973m = int(df1973['saminnt_1'].median())
    df1983m = int(df1983['saminnt_1'].median())
    df1995m = int(df1995['saminnt_1'].median())
    df2005m = int(df2005['saminnt_1'].median())
    df2013m = int(df2013['saminnt_1'].median())
    df2017m = int(df2017['saminnt_1'].median())

    coef = [lowerClassCoeffArray, middleClassCoeffArray, upperClassCoefArray]
    years = [1973, 1983, 1995, 2005, 2013, 2017]
    means = [df1973m, df1983m, df1995m, df2005m, df2013m, df2017m]
    classGroupArray = ['lower', 'middle', 'upper']

    checkit = pd.DataFrame(columns=['aargang', 'factor', 'coeffValue', 'classGroup'])
    for i in range(0, len(coef)):
        for y in range(0, len(coef[i])):
            for factor in factorList:
                print(f'\nChanges for {factor} ')
                coeffValue = coef[i][y][coef[i][y].index == factor].to_numpy()[0]
                coeffValue = coeffValue[0]
                oldValue = means[y]
                newValue = oldValue + coeffValue
                difference = newValue - oldValue
                percentage = int((difference / oldValue) * 100)
                print(f'{years[y]} change in percentage: {percentage}%.')
                year = years[y]
                classGroup = classGroupArray[i]
                checkit = checkit.append({'aargang': year, 'factor': factor, 'coeffValue': coeffValue,
                                          'classGroup' : classGroup}, ignore_index=True)
                # Make a bar plot for the coefficients, including their names on the x-axis
                # checkit.plot(x='aargang', y='percentage', kind='line', label="Percentage", title='', style=".-")


    print(checkit)
    color = ['r', 'b', 'g', 'y', 'c', 'gold', 'teal', 'orchid']
    i = 0
    width = 0.15
    barWidth = 0.1
    indices = range(1, len(factorList) + 1)
    indices2 = range(1, len(factorList) + 1)
    for factor, x in zip(factorList, indices):
        fig, ax = plt.subplots(figsize=(10, 10))
        tempCheckit = checkit[checkit['factor'] == factor]
        for year, y in zip(years, indices2):
            tempYearCheckit = tempCheckit[tempCheckit['aargang'] == year]
            print(year)
            lc = tempYearCheckit[tempCheckit['classGroup'] == 'lower']
            print(lc)
            mc = tempYearCheckit[tempCheckit['classGroup'] == 'middle']
            print(mc)
            uc = tempYearCheckit[tempCheckit['classGroup'] == 'upper']
            print(uc)
            ax.set_title(f'Difference in of cumulative income based on {factor}')
            ax.barh(y - width, lc.coeffValue, barWidth, color='c', label='Lower class')
            ax.barh(y, mc.coeffValue, barWidth, color='gold', label='Middle class')
            ax.barh(y + width, uc.coeffValue, barWidth, color='orchid', label='Upper class')
            ax.invert_yaxis()  # labels read top-to-bottom
            i = i + 1
        plt.legend(loc="upper right")
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        plt.yticks(np.arange(len(years)), years)
        plt.show()

    print(checkit)
    print(checkit.info())
    print(checkit.describe())
    print(checkit.head(100))



import dataExtract
import kmeans
import PCA
import columnsToEngineer
import numpy as np
import pandas as pd
import timeSeriesVisualization
import predictingModel

def main():
    df2012filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2012, columnsToEngineer.createArrayOfConditions2014())
    df2013filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2013, columnsToEngineer.createArrayOfConditions2014())
    df2014filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2014, columnsToEngineer.createArrayOfConditions2014())
    df2015filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2015, columnsToEngineer.createArrayOfConditions2015())
    df2016filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2016, columnsToEngineer.createArrayOfConditions2016())
    df2017filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2017, columnsToEngineer.createArrayOfConditions2017())

    listOfDataFrames = [df2012filtered, df2013filtered, df2014filtered, df2015filtered, df2016filtered, df2017filtered]

    df2012filtered = dataExtract.removeDropEmptyRows(df2012filtered, 'utdnivaa_nus2000_1')
    df2013filtered = dataExtract.removeDropEmptyRows(df2013filtered, 'utdnivaa_nus2000_1')
    df2014filtered = dataExtract.removeDropEmptyRows(df2014filtered, 'utdnivaa_nus2000_1')

    listOfDataFrames = [df2012filtered, df2013filtered, df2014filtered, df2015filtered, df2016filtered, df2017filtered]

    dfTotal = pd.concat(listOfDataFrames, ignore_index=True)

    dfTotal['sivsta_1'] = pd.to_numeric(dfTotal['sivsta_1'], downcast='integer', errors='coerce')
    dfTotal['sivstat_1'] = pd.to_numeric(dfTotal['sivstat_1'], downcast='integer', errors='coerce')
    dfTotal['ts_stor'] = pd.to_numeric(dfTotal['ts_stor'], downcast='integer', errors='coerce')

    dfTotal.aargang.fillna(dfTotal.aar, inplace=True)
    dfTotal.sivstat_1.fillna(dfTotal.sivsta_1, inplace=True)
    listOfValues = []
    for index, value in dfTotal.utdnivaa_nus2000_1.items():
        if value not in listOfValues:
            print(value)
            listOfValues.append(value)
    print(listOfValues)
    dfTotal['utdnivaa1'] = dfTotal['utdnivaa_nus2000_1'].str[:1]
    dfTotal.utdnivaa.fillna(dfTotal.utdnivaa1, inplace=True)
    dfTotal.saminnt_1.fillna(dfTotal.aggi_18_1, inplace=True)
    dfTotal.kode218_1.fillna(dfTotal.bel21_8_1, inplace=True)

    dfTotal = dfTotal.drop(columns='bel21_8_1')
    dfTotal = dfTotal.drop(columns='aggi_18_1')
    dfTotal = dfTotal.drop(columns='sivsta_1')
    dfTotal = dfTotal.drop(columns='aar')
    dfTotal = dfTotal.drop(columns='utdnivaa1')
    dfTotal = dfTotal.drop(columns='utdnivaa_nus2000_1')
    dfTotal = dfTotal.drop(columns='bm2')
    dfTotal = dfTotal.drop(columns='bm1')
    dfTotal = dfTotal.drop(columns='selvsosstat')

    columnsToOneHotEncode = ['utdnivaa', 'sivstat_1', 'ts_stor', 'landsdel', 'hels1',
                             'fam_fase']
    for x in dfTotal.columns:
        print(x)

    dfTotal = dataExtract.insertDataFrameAndGetDummies(dfTotal, columnsToOneHotEncode)

    dfTotalWorkAge = dataExtract.filterWorkingAgeGroups(dfTotal, 'alder_1', 24, 64)

    df2012WorkAge = dataExtract.filterWorkingAgeGroups(df2012filtered, 'alder_1', 24, 64)
    df2013WorkAge = dataExtract.filterWorkingAgeGroups(df2013filtered, 'alder_1', 24, 64)
    df2014WorkAge = dataExtract.filterWorkingAgeGroups(df2014filtered, 'alder_1', 24, 64)
    df2015WorkAge = dataExtract.filterWorkingAgeGroups(df2015filtered, 'alder_1', 24, 64)
    df2016WorkAge = dataExtract.filterWorkingAgeGroups(df2016filtered, 'alder_1', 24, 64)
    df2017WorkAge = dataExtract.filterWorkingAgeGroups(df2017filtered, 'alder_1', 24, 64)

    df2012WorkAge = df2012WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2013WorkAge = df2013WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2014WorkAge = df2014WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2015WorkAge = df2015WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2016WorkAge = df2016WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2017WorkAge = df2017WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    dfTotalWorkAge = dfTotalWorkAge.apply(pd.to_numeric, errors='coerce').dropna()





    dfTotalWorkAgeScaled = dataExtract.insertDataFrameToScale(dfTotalWorkAge)
    dfTotalWorkAgeNormalized = dataExtract.insertDataFrameAndNormalize(dfTotalWorkAge)

    x_scaled = np.asarray(dfTotalWorkAgeScaled)
    #kmeans.runKMeansOnScaledData(x_scaled)
    #PCA.runPCAAnalysisOnScaledData(x_scaled)

    x_scaled = np.asarray(dfTotalWorkAgeNormalized)
    #kmeans.runKMeansOnScaledData(x_scaled)
    #PCA.runPCAAnalysisOnScaledData(x_scaled)

    #timeSeriesVisualization.plot_df(dfTotalWorkAge, x=dfTotalWorkAge.aargang, y=dfTotalWorkAge.saminnt_1, title='Test')
    #timeSeriesVisualization.plot_df_2(dfTotalWorkAge)

    #predictingModel.predictionModelLinearRegression(df2012WorkAge, 'aggi_18_1', 'aargang')
    #predictingModel.predictionModelLinearRegression(df2013WorkAge, 'aggi_18_1', 'aargang')
    #predictingModel.predictionModelLinearRegression(df2014WorkAge, 'aggi_18_1', 'aargang')
    #predictingModel.predictionModelLinearRegression(df2015WorkAge, 'aggi_18_1', 'aar')
    #predictingModel.predictionModelLinearRegression(df2016WorkAge, 'saminnt_1', 'aar')
    #predictingModel.predictionModelLinearRegression(df2017WorkAge, 'saminnt_1', 'aar')

    predictingModel.predictionModelLinearRegression(dfTotalWorkAge, 'saminnt_1', 'aargang')
    predictingModel.predictionModelRidgeRegression(dfTotalWorkAge, 'saminnt_1', 'aargang')
    predictingModel.predictionModelLassoRegression(dfTotalWorkAge, 'saminnt_1', 'aargang')
    predictingModel.predictionModelSDGRegression(dfTotalWorkAge, 'saminnt_1', 'aargang')
    predictingModel.predictingRandomForestRegression(dfTotalWorkAge, 'saminnt_1', 'aargang')
    predictingModel.predictingDecisionsTreeRegression(dfTotalWorkAge, 'saminnt_1', 'aargang')


if __name__ == '__main__':
    main()

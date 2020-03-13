import dataExtract
import kmeans
import PCA
import columnsToEngineer
import numpy as np
import pandas as pd

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

    dfTotal.aargang.fillna(dfTotal.aar, inplace=True)
    dfTotal.sivstat_1.fillna(dfTotal.sivsta_1, inplace=True)
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

    dfTotalWorkAge = dataExtract.filterWorkingAgeGroups(dfTotal, 'alder_1', 24, 64)
    df2012WorkAge = dataExtract.filterWorkingAgeGroups(df2012filtered, 'alder_1', 24, 64)
    df2013WorkAge = dataExtract.filterWorkingAgeGroups(df2013filtered, 'alder_1', 24, 64)
    df2014WorkAge = dataExtract.filterWorkingAgeGroups(df2014filtered, 'alder_1', 24, 64)
    df2015WorkAge = dataExtract.filterWorkingAgeGroups(df2015filtered, 'alder_1', 24, 64)
    df2016WorkAge = dataExtract.filterWorkingAgeGroups(df2016filtered, 'alder_1', 24, 64)
    df2017WorkAge = dataExtract.filterWorkingAgeGroups(df2017filtered, 'alder_1', 24, 64)

    for x in dfTotalWorkAge.columns:
        print (x)


    for index, row in dfTotalWorkAge.iterrows():
        if row == '' or row == np.nan:
            print(row)

    dfTotalWorkAgeScaled = dataExtract.insertDataFrameToScale(dfTotalWorkAge)
    dfTotalWorkAgeNormalized = dataExtract.insertDataFrameAndNormalize(dfTotalWorkAge)

    x_scaled = np.asarray(dfTotalWorkAgeScaled)
    kmeans.runKMeansOnScaledData(x_scaled)
    PCA.runPCAAnalysisOnScaledData(x_scaled)

if __name__ == '__main__':
    main()

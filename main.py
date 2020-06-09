import dataExtract
import kmeans
import PCA
import columnsToEngineer
import numpy as np
import pandas as pd
import timeSeriesVisualization
import predictingModel, dataExploration

def main():
    df1973filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df1973,
                                                                    columnsToEngineer.createArrayOfConditions1973())
    df1983filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df1983,
                                                                    columnsToEngineer.createArrayOfConditions1983())
    df1995filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df1995,
                                                                    columnsToEngineer.createArrayOfConditions1995())
    df2005filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2005,
                                                                    columnsToEngineer.createArrayOfConditions2005())
    df2012filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2012,
                                                                    columnsToEngineer.createArrayOfConditions2014())
    df2013filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2013,
                                                                    columnsToEngineer.createArrayOfConditions2014())
    df2014filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2014,
                                                                    columnsToEngineer.createArrayOfConditions2014())
    df2015filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2015,
                                                                    columnsToEngineer.createArrayOfConditions2015())
    df2016filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2016,
                                                                    columnsToEngineer.createArrayOfConditions2016())
    df2017filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2017,
                                                                    columnsToEngineer.createArrayOfConditions2017())
    df1973filtered = dataExtract.streamlineDataframe1973(df1973filtered)
    df1983filtered = dataExtract.streamlineDataframe1983(df1983filtered)
    df1995filtered = dataExtract.streamlineDataframe1995(df1995filtered)
    df2005filtered = dataExtract.streamlineDataframe2005(df2005filtered)
    df2012filtered = dataExtract.removeDropEmptyRows(df2012filtered, 'utdnivaa_nus2000_1')
    df2013filtered = dataExtract.removeDropEmptyRows(df2013filtered, 'utdnivaa_nus2000_1')
    df2014filtered = dataExtract.removeDropEmptyRows(df2014filtered, 'utdnivaa_nus2000_1')

    listOfDataFrames = [df2012filtered, df2013filtered, df2014filtered, df2015filtered, df2016filtered, df2017filtered]

    dfTotal = pd.concat(listOfDataFrames, axis=0, ignore_index=False, sort=True)
    dfTotal.reset_index(drop=True, inplace=True)

    dfTotal['sivsta_1'] = pd.to_numeric(dfTotal['sivsta_1'], downcast='integer', errors='coerce')
    dfTotal['sivstat_1'] = pd.to_numeric(dfTotal['sivstat_1'], downcast='integer', errors='coerce')
    dfTotal['ts_stor'] = pd.to_numeric(dfTotal['ts_stor'], downcast='integer', errors='coerce')
    dfTotal['kode218_1'] = pd.to_numeric(dfTotal['kode218_1'], downcast='integer', errors='coerce')
    dfTotal['bel21_8_1'] = pd.to_numeric(dfTotal['bel21_8_1'], downcast='integer', errors='coerce')

    dfTotal.aargang.fillna(dfTotal.aar, inplace=True)
    dfTotal.sivstat_1.fillna(dfTotal.sivsta_1, inplace=True)
    dfTotal['utdnivaa_nus2000_1'].replace(np.NaN, 9, inplace=True)
    dfTotal['utdnivaa1'] = dfTotal.utdnivaa_nus2000_1.astype(str).str[:1].astype(int)
    dfTotal.utdnivaa.fillna(dfTotal.utdnivaa1, inplace=True)
    dfTotal.saminnt_1.fillna(dfTotal.aggi_18_1, inplace=True)
    dfTotal.kode218_1.fillna(dfTotal.bel21_8_1, inplace=True)
    dfTotal.landsdel.replace(2,3)
    dfTotal = dataExtract.fixFamilyPhase(dfTotal)
    dfTotal['landsdel'] = dataExtract.fixRegion(dfTotal, 'landsdel', reduction=1)
    dfTotal['ts_stor'] = dataExtract.fixPopDensity(dfTotal, 'ts_stor')
    listOfOlderDataframes = [df1973filtered, df1983filtered, df1995filtered, df2005filtered]
    dfToBeAdded = pd.concat(listOfOlderDataframes, axis=0, sort=True)
    dfTotal = pd.concat([dfToBeAdded, dfTotal], axis=0, sort=True)
    dfTotal['helskomb'] = dataExtract.combineHealth(dfTotal, 'hels2a', 'hels2b', 'helskomb')
    dfTotal['kode218_1'] = dataExtract.fixDisabilityPayment(dfTotal, 'kode218_1')


    #with pd.option_context('display.max_rows', -1, 'display.max_columns', -1):
        #print(df2005filtered.info())


    ##EUSILC
    dfTotal = dfTotal.drop(columns=(['bel21_8_1', 'aggi_18_1', 'sivsta_1', 'aar', 'utdnivaa1', 'utdnivaa_nus2000_1', 'selvsosstat']))

    ##1995&EUSILC
    dfTotal = dfTotal.drop(columns=(['hels1', 'hels2b', 'antbarn']))

    ##1983&1995&EUSILC
    dfTotal = dfTotal.drop(columns=(['landsdel']))

    ##1973&1983&1995&EUSILC
    dfTotal = dfTotal.drop(columns=(['ts_stor', 'hels2a', 'fam_fase']))

    dfTotal['kode218_1'] = pd.to_numeric(dfTotal['kode218_1'], downcast='integer', errors='coerce')
    dfTotal['kode218_1'] = dataExtract.fixDisabilityTotal(dfTotal, 'kode218_1')
    dfTotal['utdnivaa'] = pd.to_numeric(dfTotal['utdnivaa'], downcast='integer', errors='coerce')
    dfTotal['sivstat_1'] = pd.to_numeric(dfTotal['sivstat_1'], downcast='integer', errors='coerce')
    dfTotal['arb1_1'] = pd.to_numeric(dfTotal['arb1_1'], downcast='integer', errors='coerce')
    dfTotal['sivstat_1'].replace([8, 9], np.NaN, inplace=True)
    dfTotal['arb1_1'].replace([8, 9], np.NaN, inplace=True)
    dfTotal['utdnivaa'].replace(9, np.NaN, inplace=True)
    dfTotal['kode218_1'] = dataExtract.inverseDisability(dfTotal, 'kode218_1')
    dfTotal['helskomb'] = dataExtract.inverseHealth(dfTotal, 'helskomb')
    dfTotal.apply(pd.to_numeric, errors='coerce')



    columnsToOneHotEncodeEUSILC = ['utdnivaa', 'sivstat_1', 'ts_stor', 'landsdel', 'hels1',
                             'fam_fase']

    columnsToOneHotEncode1995EU = ['utdnivaa', 'sivstat_1', 'ts_stor', 'landsdel',
                                   'fam_fase']

    columnsToOneHotEncode1983 = ['utdnivaa', 'sivstat_1', 'ts_stor', 'hels1',
                             'fam_fase']

    columnsToOneHotEncodeOverall = ['utdnivaa', 'sivstat_1', 'kjonn_1']

    dfTotal = dfTotal.dropna()
    dfTotal.reset_index(drop=True, inplace=True)

    #dfTotal = dataExtract.insertDataFrameAndGetDummies(dfTotal, columnsToOneHotEncode1995EU)
    #dfTotal = dataExtract.insertDataFrameAndGetDummies(dfTotal, columnsToOneHotEncode1983)
    dfTotal = dataExtract.insertDataFrameAndGetDummies(dfTotal, columnsToOneHotEncodeOverall)

    df2012WorkAge = dataExtract.filterWorkingAgeGroups(df2012filtered, 'alder_1', 24, 64)
    df2013WorkAge = dataExtract.filterWorkingAgeGroups(df2013filtered, 'alder_1', 24, 64)
    df2014WorkAge = dataExtract.filterWorkingAgeGroups(df2014filtered, 'alder_1', 24, 64)
    df2015WorkAge = dataExtract.filterWorkingAgeGroups(df2015filtered, 'alder_1', 24, 64)
    df2016WorkAge = dataExtract.filterWorkingAgeGroups(df2016filtered, 'alder_1', 24, 64)
    df2017WorkAge = dataExtract.filterWorkingAgeGroups(df2017filtered, 'alder_1', 24, 64)
    dfTotalWorkAge = dataExtract.filterWorkingAgeGroups(dfTotal, 'alder_1', 24, 64)
    #dfTotalWorkAge = dataExtract.filterWorkedLastWeek(dfTotalWorkAge, 'arb1_1', 1)


    df2012WorkAge = df2012WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2013WorkAge = df2013WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2014WorkAge = df2014WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2015WorkAge = df2015WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2016WorkAge = df2016WorkAge.apply(pd.to_numeric, errors='coerce').dropna()
    df2017WorkAge = df2017WorkAge.apply(pd.to_numeric, errors='coerce').dropna()


    dfTotalWorkAgeScaled = dataExtract.insertDataFrameToScale(dfTotalWorkAge)
    dfTotalWorkAgeNormalized = dataExtract.insertDataFrameAndNormalize(dfTotalWorkAge)

    #x_scaled = np.asarray(dfTotalWorkAgeScaled)
    #kmeans.runKMeansOnScaledData(x_scaled)
    #PCA.runPCAAnalysisOnScaledData(x_scaled)

    #x_scaled = np.asarray(dfTotalWorkAgeNormalized)
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


    #timeSeriesVisualization.checkDifferentMethods(dfTotalWorkAge, 'saminnt_1', 'aargang')

    #with pd.option_context('display.max_rows', -1, 'display.max_columns', -1):

    for x in dfTotalWorkAge.columns:
        print(x)


    dfTotalWorkAge = dfTotalWorkAge.rename(columns={"alder_1":"alder","kode218_1":"Uføretrygdet","saminnt_1":"SamletInntekt",
                                   "utdnivaa_0.0":"IngenUtdanning","utdnivaa_1.0":"Barneskole","utdnivaa_2.0":
                                    "Ungdomsskole","utdnivaa_3.0":"VideregåendeGrunn","utdnivaa_4.0":"VideregåendeAvslut",
                                   "utdnivaa_5.0":"Påbygg","utdnivaa_6.0":"UniversitetBachelor","utdnivaa_7.0":"UniversitetMaster",
                                   "utdnivaa_8.0":"Forskernivå","sivstat_1_1.0":"Ugift","sivstat_1_2.0":"Gift/partnerskap",
                                   "sivstat_1_3.0":"Enke/enkemann","sivstat_1_4.0":"Separert","sivstat_1_5.0":"Skilt"
                                    ,"kjonn_1_1":"Mann","kjonn_1_2":"Kvinne"}, errors="raise")

    print(dfTotalWorkAge.cov())

    dataExploration.heatmapCorrelation(dfTotalWorkAge)

    coeffArrayLC = predictingModel.runRidgePredictionOnYearlyBasisWithIncomeGroups(dataFrame=dfTotalWorkAge,
                                                                                   label='SamletInntekt',
                                                                                    dropWorkStatus='arb1_1',
                                                                                   dropYear='aargang', minFactor=0.1,
                                                                                   maxFactor=0.59,
                                                                                   wagegroup="low-income class")

    coeffArrayMC = predictingModel.runRidgePredictionOnYearlyBasisWithIncomeGroups(dataFrame=dfTotalWorkAge,
                                                                                   label='SamletInntekt',
                                                                                    dropWorkStatus='arb1_1',
                                                                                   dropYear='aargang',
                                                                                    minFactor=0.6, maxFactor=1.39,
                                                                                   wagegroup="middle-income class")

    coeffArrayUC = predictingModel.runRidgePredictionOnYearlyBasisWithIncomeGroups(dataFrame=dfTotalWorkAge,
                                                                                   label='SamletInntekt',
                                                                                    dropWorkStatus='arb1_1',
                                                                                   dropYear='aargang',
                                                                                    minFactor=1.4, maxFactor=2.2,
                                                                                   wagegroup="high-income class")

    timeSeriesVisualization.visualizeDifferenceForIncomeGroups(coeffArrayLC, coeffArrayMC, coeffArrayUC, df=dfTotalWorkAge)

    predictingModel.runRidgePredictionOnYearlyBasisAllInOne(dataFrame=dfTotalWorkAge, label='SamletInntekt',
                                                            dropWorkStatus='arb1_1', dropYear='aargang', )

    coeff1973 = predictingModel.runRidgePredictionOnYearlyBasis(dataFrame=dfTotalWorkAge, dropYear='aargang',
                                                                yearFilter=1973, label='SamletInntekt',
                                                                dropWorkStatus='arb1_1')
    coeff1983 = predictingModel.runRidgePredictionOnYearlyBasis(dataFrame=dfTotalWorkAge, dropYear='aargang',
                                                                yearFilter=1983, label='SamletInntekt',
                                                                dropWorkStatus='arb1_1')
    coeff1995 = predictingModel.runRidgePredictionOnYearlyBasis(dataFrame=dfTotalWorkAge, dropYear='aargang',
                                                                yearFilter=1995, label='SamletInntekt',
                                                                dropWorkStatus='arb1_1')
    coeff2005 = predictingModel.runRidgePredictionOnYearlyBasis(dataFrame=dfTotalWorkAge, dropYear='aargang',
                                                                yearFilter=2005, label='SamletInntekt',
                                                                dropWorkStatus='arb1_1')
    coeff2013 = predictingModel.runRidgePredictionOnYearlyBasis(dataFrame=dfTotalWorkAge, dropYear='aargang', yearFilter=2013,
                                               label='SamletInntekt', dropWorkStatus='arb1_1')
    coeff2017 = predictingModel.runRidgePredictionOnYearlyBasis(dataFrame=dfTotalWorkAge, dropYear='aargang', yearFilter=2017,
                                               label='SamletInntekt', dropWorkStatus='arb1_1')

    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="Mann")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="Kvinne")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="Uføretrygdet")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="Ungdomsskole")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="VideregåendeGrunn")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="VideregåendeAvslut")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="Påbygg")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="UniversitetBachelor")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="UniversitetMaster")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="Forskernivå")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="helskomb")
    timeSeriesVisualization.visualizeTrends(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017,
                                            dfTotalWorkAge, benchmark='SamletInntekt', factor="Ugift")

    #predictingModel.runForecastingIntoFuture(coeff1973, coeff1983, coeff1995, coeff2005, coeff2013, coeff2017)


if __name__ == '__main__':
    main()
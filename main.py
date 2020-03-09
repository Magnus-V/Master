import dataExtract
import kmeans
import PCA
import columnsToEngineer
import numpy as np

def main():

    #WorkAgeDf1973 = dataExtract.filterWorkingAgeGroups(dataExtract.df1973, 'v002', 24, 64)
    #WorkAgeDf1983 = dataExtract.filterWorkingAgeGroups(dataExtract.df1983, 'V10', 59, 19)
    #WorkAgeDf1987 = dataExtract.filterWorkingAgeGroups(dataExtract.df1987, 'V6', 1963, 1923)

    df2011 = dataExtract.df2011
    df2012 = dataExtract.df2012
    df2013 = dataExtract.df2013
    df2014 = dataExtract.df2014
    df2015 = dataExtract.df2015
    df2016 = dataExtract.df2016
    df2017 = dataExtract.df2017
    df2018 = dataExtract.df2018




    #df2011filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2011, columnsToEngineer.createArrayOfConditions2017())
    #df2012filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2012, columnsToEngineer.createArrayOfConditions2017())
    #df2013filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2013, columnsToEngineer.createArrayOfConditions2017())
    df2014filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2014, columnsToEngineer.createArrayOfConditions2014())
    df2015filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2015, columnsToEngineer.createArrayOfConditions2015())
    df2016filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2016, columnsToEngineer.createArrayOfConditions2016())
    df2017filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2017, columnsToEngineer.createArrayOfConditions2017())
    #df2018filtered = dataExtract.filterOutDatasetOnListOfConditions(dataExtract.df2018, columnsToEngineer.createArrayOfConditions2017())

    #listOfDataFramesLower = dataExtract.writeHeadersToLowerCaseOnly(dataExtract.listOfDataFrames)
    #arrayWithDataframesWithWorkingAgeGroups = dataExtract.filterListWorkingAgeGroups(listOfDataFramesLower, 'alder_1', 'v315', 24, 64)
    columnsToEngineer2017 = columnsToEngineer.createArrayOfConditions2017()


    #dfarray = dataExtract.filterOutArrayOfDatasetsOnArrayOfConditions(arrayWithDataframesWithWorkingAgeGroups, columnsToEngineer2017)


    columnsToEngineer1973 = columnsToEngineer.createArrayOfConditions1973()

    #df1973WorkAgeChosenColumnsStandardized = dataExtract.insertDataFrameAndColumnsToStandardScaler(WorkAgeDf1973, columnsToEngineer1973)
    #df1973WorkAgeChosenColumnsNormalized = dataExtract.insertDataFrameAndColumnsToMinMaxNormalize(WorkAgeDf1973, columnsToEngineer1973)

    #df1973AllStandard = dataExtract.insertDataFrameToScale(WorkAgeDf1973)
    #df1973AllNormalized = dataExtract.insertDataFrameAndNormalize(WorkAgeDf1973)
    #x_scaled = np.asarray()
    #kmeans.runKMeansOnScaledData(x_scaled)
    #PCA.runPCAAnalysisOnScaledData(x_scaled)

if __name__ == '__main__':
    main()

import dataExtract
import kmeans
import PCA
import columnsToEngineer
import numpy as np

def main():

    #WorkAgeDf1973 = dataExtract.filterWorkingAgeGroups(dataExtract.df1973, 'v002', 24, 64)
    #WorkAgeDf1983 = dataExtract.filterWorkingAgeGroups(dataExtract.df1983, 'V10', 59, 19)
    #WorkAgeDf1987 = dataExtract.filterWorkingAgeGroups(dataExtract.df1987, 'V6', 1963, 1923)

    listOfDataFramesLower = dataExtract.writeHeadersToLowerCaseOnly(dataExtract.listOfDataFrames)
    arrayWithDataframesWithWorkingAgeGroups = dataExtract.filterListWorkingAgeGroups(listOfDataFramesLower, 'alder_1', 'v315', 24, 64)



    print(arrayWithDataframesWithWorkingAgeGroups)
    columnsToEngineer1973 = columnsToEngineer.createArrayOfConditions1973()

    df1973WorkAgeChosenColumnsStandardized = dataExtract.insertDataFrameAndColumnsToStandardScaler(WorkAgeDf1973, columnsToEngineer1973)
    df1973WorkAgeChosenColumnsNormalized = dataExtract.insertDataFrameAndColumnsToMinMaxNormalize(WorkAgeDf1973, columnsToEngineer1973)

    #df1973AllStandard = dataExtract.insertDataFrameToScale(WorkAgeDf1973)
    #df1973AllNormalized = dataExtract.insertDataFrameAndNormalize(WorkAgeDf1973)
    x_scaled = np.asarray(df1973WorkAgeChosenColumnsStandardized)
    kmeans.runKMeansOnScaledData(x_scaled)
    PCA.runPCAAnalysisOnScaledData(x_scaled)

if __name__ == '__main__':
    main()

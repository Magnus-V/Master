import dataExtract
import kmeans
import PCA
import numpy as np


def main():
    df1973 = dataExtract.readCSVSurveyConvertToDataFrame(dataExtract.LivingConditionsSurvey1973)
    df2017 = dataExtract.readCSVSurveyConvertToDataFrame(dataExtract.EUSILC2017)
    WorkAgeDf1973 = dataExtract.filterWorkingAgeGroups(df1973, 'v002', 24, 64)
    WorkAgeDf2017 = dataExtract.filterWorkingAgeGroups(df2017, 'alder_1', 24, 64)

    columnsToEngineer1973 = dataExtract.createArrayOfConditions1973()

    df1973WorkAgeChosenColumnsStandardized = dataExtract.insertDataFrameAndColumnsToStandardScaler(WorkAgeDf1973, columnsToEngineer1973)
    df1973WorkAgeChosenColumnsNormalized = dataExtract.insertDataFrameAndColumnsToMinMaxNormalize(WorkAgeDf1973, columnsToEngineer1973)

    #df1973AllStandard = dataExtract.insertDataFrameToScale(WorkAgeDf1973)
    #df1973AllNormalized = dataExtract.insertDataFrameAndNormalize(WorkAgeDf1973)
    x_scaled = np.asarray(df1973WorkAgeChosenColumnsStandardized)
    kmeans.runKMeansOnScaledData(x_scaled)
    PCA.runPCAAnalysisOnScaledData(x_scaled)

if __name__ == '__main__':
    main()

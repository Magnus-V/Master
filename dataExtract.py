import os
import columnsToEngineer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy as sp
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder




# Bærbare
my_data_folder = os.path.dirname(r'C:\Users\Magnus\Documents\MasterProg\AmazonWebServices\survey_on_income_and_living_conditions\\')
# Stasjonære
#my_data_folder = os.path.dirname(r'C:\Users\Magnus L. Vestby\Documents\Universitetsarbeid\Master\INFO390\survey_on_income_and_living_conditions\\')


# Surveys predating 1996
HealthSurvey1968 = os.path.join(my_data_folder, r'HealthSurvey1968.csv')
HealthSurvey1975 = os.path.join(my_data_folder, r'HealthSurvey1975.csv')
HealthSurvey1985 = os.path.join(my_data_folder, r'HealthSurvey1985.csv')
HealthSurvey1995 = os.path.join(my_data_folder, r'HealthSurvey1995.csv')
LivingConditionsSurvey1973 = os.path.join(my_data_folder, r'LivingConditionsSurvey1973.csv')
LivingConditionsSurvey1980 = os.path.join(my_data_folder, r'LivingConditionsSurvey1980.csv')
LivingConditionsSurvey1981Housing = os.path.join(my_data_folder, r'LivingConditionsSurvey1981.csv')
LivingConditionsSurvey1983 = os.path.join(my_data_folder, r'LivingConditionsSurvey1983.csv')
LivingConditionsSurvey1987 = os.path.join(my_data_folder, r'LivingConditionsSurvey1987.csv')
LivingConditionsSurvey1988Housing = os.path.join(my_data_folder, r'LivingConditionsSurvey1988.csv')
LivingConditionsSurvey1991 = os.path.join(my_data_folder, r'LivingConditionsSurvey1991.csv')
LivingConditionsSurvey1995 = os.path.join(my_data_folder, r'LivingConditionsSurvey1995.csv')
LivingConditionsSurvey1995Housing = os.path.join(my_data_folder, r'LivingConditionsSurvey1995Housing.csv')

# Coordinated surveys
CoordinatedSurvey2016Work = os.path.join(my_data_folder, r'LivingConditionsSurvey2016Work.csv')
CoordinatedSurvey2015SocialRegion = os.path.join(my_data_folder, r'LivingConditionsSurvey2015SocialCounty.csv')
CoordinatedSurvey2013Work = os.path.join(my_data_folder, r'LivingConditionsSurvey2013Work.csv')
CoordinatedSurvey2012Social = os.path.join(my_data_folder, r'LivingConditionsSurvey2012Social.csv')
CoordinatedSurvey2009Work = os.path.join(my_data_folder, r'LivingConditionsSurvey2009Work.csv')
CoordinatedSurvey2008Health = os.path.join(my_data_folder, r'LivingConditionsSurvey2008Health.csv')
CoordinatedSurvey2007Housing = os.path.join(my_data_folder, r'LivingConditionsSurvey2007Housing.csv')
CoordinatedSurvey2006Work = os.path.join(my_data_folder, r'LivingConditionsSurvey2006Work.csv')
CoordinatedSurvey2005Health = os.path.join(my_data_folder, r'LivingConditionsSurvey2005Health.csv')
CoordinatedSurvey2004Housing = os.path.join(my_data_folder, r'LivingConditionsSurvey2004Housing.csv')
CoordinatedSurvey2003Work = os.path.join(my_data_folder, r'LivingConditionsSurvey2003Work.csv')
CoordinatedSurvey2002Health = os.path.join(my_data_folder, r'LivingConditionsSurvey2002Health.csv')
CoordinatedSurvey2001Housing = os.path.join(my_data_folder, r'LivingConditionsSurvey2001Housing.csv')
CoordinatedSurvey2000Work = os.path.join(my_data_folder, r'LivingConditionsSurvey2000Work.csv')
CoordinatedSurvey1998Health = os.path.join(my_data_folder, r'LivingConditionsSurvey1998Health.csv')
CoordinatedSurvey1997Housing = os.path.join(my_data_folder, r'LivingConditionsSurvey1997Housing.csv')
CoordinatedSurvey1996Work = os.path.join(my_data_folder, r'LivingConditionsSurvey1996Work.csv')

# EUSILC
EUSILC2011 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2011.csv')
EUSILC2012 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2012.csv')
EUSILC2013 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2013.csv')
EUSILC2014 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2014.csv')
EUSILC2015 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2015.csv')
EUSILC2016 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2016.csv')
EUSILC2017 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2017.csv')
EUSILC2018 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2018.csv')


def readCSVSurvey(csvfile):
    readCSV = pd.read_csv(csvfile, low_memory=False)
    return readCSV


def readCSVSurveyConvertToDataFrame(csvfile):
    readCSV = pd.read_csv(csvfile, low_memory=False)
    df_readCSV = pd.DataFrame(readCSV)
    return df_readCSV


def readDfAndReturnSeries(dataFrame, Seriesname):
    tempDataSeries = dataFrame[Seriesname]
    return tempDataSeries


df1973 = readCSVSurveyConvertToDataFrame(LivingConditionsSurvey1973)
df1983 = readCSVSurveyConvertToDataFrame(LivingConditionsSurvey1983)
df1987 = readCSVSurveyConvertToDataFrame(LivingConditionsSurvey1987)
df1995 = readCSVSurveyConvertToDataFrame(LivingConditionsSurvey1995)
df2005 = readCSVSurveyConvertToDataFrame(CoordinatedSurvey2005Health)

df2011 = readCSVSurveyConvertToDataFrame(EUSILC2011)
df2012 = readCSVSurveyConvertToDataFrame(EUSILC2012)
df2013 = readCSVSurveyConvertToDataFrame(EUSILC2013)
df2014 = readCSVSurveyConvertToDataFrame(EUSILC2014)
df2015 = readCSVSurveyConvertToDataFrame(EUSILC2015)
df2016 = readCSVSurveyConvertToDataFrame(EUSILC2016)
df2017 = readCSVSurveyConvertToDataFrame(EUSILC2017)
df2018 = readCSVSurveyConvertToDataFrame(EUSILC2018)

listOfDataFrames = [df2012, df2013, df2014, df2015, df2016, df2017, df2018]

def writeHeadersToLowerCaseOnly(dataFrame):
    dataFrame.columns = dataFrame.columns.str.lower()
    return dataFrame


def writeArrayOfDataFramesHeadersToLowerCaseOnly(arrayOfDataFrames):
    returnList = []
    for dataFrame in arrayOfDataFrames:
        dataFrame.columns = dataFrame.columns.str.lower()
        returnList.append(dataFrame)
    return returnList

listOfDataFramesLower = writeArrayOfDataFramesHeadersToLowerCaseOnly(listOfDataFrames)

def filterWorkingAgeGroups(dataFrame, filter, minAge, maxAge):
    filteredDataFrame = dataFrame[(dataFrame[filter] >= minAge) & (dataFrame[filter] <= maxAge)]
    filteredDataFrame.reset_index(inplace=True, drop=True)
    return filteredDataFrame

def filterWorkedLastWeek(dataFrame, filter, validValue):
    filteredDataFrame = dataFrame[(dataFrame[filter] == validValue)]
    filteredDataFrame.reset_index()
    return filteredDataFrame

def filterListWorkingAgeGroups(listOfDataFrames, filter, excfilter, minAge, maxAge):
    returnArray = []
    for dataFrame in listOfDataFrames:
        try:
            tempDataFrame = dataFrame[(dataFrame[filter] > minAge) & (dataFrame[filter] < maxAge)]
        except:
            tempDataFrame = dataFrame[(dataFrame[excfilter] > minAge) & (dataFrame[excfilter] < maxAge)]
        returnArray.append(tempDataFrame)
    return returnArray


def findIncomeAndEducation(dataFrame, firstCondition, secondCondition):
    returnArray = []
    for index, row in dataFrame.iterrows():
        tempCond = row[firstCondition]
        tempCond2 = row[secondCondition]
        tempArray = [tempCond, tempCond2]
        returnArray.append(tempArray)
    return returnArray


def filterOutDatasetsOnFourConditions(dataFrame, firstCondition, secondCondition, thirdCondition, fourthCondition):
    returnArray = []
    for index, row in dataFrame.iterrows():
        tempCond = row[firstCondition]
        tempCond2 = row[secondCondition]
        tempCond3 = row[thirdCondition]
        tempCond4 = row[fourthCondition]
        tempArray = [tempCond, tempCond2, tempCond3, tempCond4]
        returnArray.append(tempArray)
    return returnArray


def filterOutDatasetOnListOfConditions(dataFrame, arrayOfConditions):
    dataFrame = dataFrame.filter(arrayOfConditions)
    dataFrame = dataFrame.apply(pd.to_numeric, downcast='integer', errors='coerce')
    return dataFrame


def filterOutArrayOfDatasetsOnArrayOfConditions(arrayOfDataFrames, arrayOfConditions):
    returnArrayOfDataframes = []
    for dataFrame in arrayOfDataFrames:
        returnArray = []
        for index, row in dataFrame.iterrows():
            tempArray = []
            tempArraySingleRow = []
            length = len(arrayOfConditions)
            for i in range(0, length):
                tempArraySingleRow = []
                tempCond = row[arrayOfConditions[i]]
                tempArraySingleRow.append(tempCond)
            tempArray.append(tempArraySingleRow)
        returnArray.append(tempArray)
    returnArrayOfDataframes.append(returnArray)
    return returnArrayOfDataframes


def removeDropEmptyRows(dataFrame, filter):
    indexList = []
    for index, row in dataFrame[filter].iteritems():
        if row == ' ':
            indexList.append(index)
    dataFrame = dataFrame.drop(indexList)
    return dataFrame


def insertDataFrameAndColumnsToMinMaxNormalize(dataFrame, columnsToNormalize):
    minMaxScaler = MinMaxScaler()
    x = dataFrame[columnsToNormalize].values
    x_scaled = minMaxScaler.fit_transform(x)
    df_temp = pd.DataFrame(x_scaled, columns=columnsToNormalize, index=dataFrame.index)
    dataFrame[columnsToNormalize] = df_temp
    return dataFrame


def insertDataFrameAndColumnsToStandardScaler(dataFrame, columnsToNormalize):
    standardScaler = StandardScaler()
    x = dataFrame[columnsToNormalize].values
    x_scaled = standardScaler.fit_transform(x)
    df_temp = pd.DataFrame(x_scaled, columns=columnsToNormalize, index=dataFrame.index)
    dataFrame[columnsToNormalize] = df_temp
    return dataFrame


def insertDataFrameToScale(dataFrame):
    standardScaler = StandardScaler()
    x = dataFrame.values
    x_scaled = standardScaler.fit_transform(x)
    df_temp = pd.DataFrame(x_scaled, index=dataFrame.index, columns=dataFrame.columns)
    return df_temp


def insertDataFrameAndNormalize(dataFrame):
    minMaxScaler = MinMaxScaler()
    x = dataFrame.values
    x_normalized = minMaxScaler.fit_transform(x)
    df_temp = pd.DataFrame(x_normalized, index=dataFrame.index, columns=dataFrame.columns)
    return df_temp

# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy


def insertDataFrameAndOneHotEncode(dataFrame, columsToOneHotEncode):
    return


def insertDataFrameAndGetDummies(dataFrame, columnsToOneHotEncode):
    encodedDf = pd.get_dummies(dataFrame, columns=columnsToOneHotEncode)
    return encodedDf


def fixAge(df, labelOfBirth, yearOfSurvey):
    ageSeries = df[labelOfBirth]
    for index, row in ageSeries.items():
        if row <= yearOfSurvey:
            age = yearOfSurvey - row
            df.at[index, labelOfBirth] = age
        if row > yearOfSurvey:
            age = yearOfSurvey + (row-yearOfSurvey)
            df.at[index, labelOfBirth] = age
    return ageSeries


def fixRegion(df, labelOfRegion, reduction):
    regionSeries = df[labelOfRegion]
    for index, row in regionSeries.items():
        region = row - reduction
        df.at[index, labelOfRegion] = region
    return regionSeries


def fixFamilyPhase(df):
    df.fam_fase.replace(10, 9, inplace=True)
    df.fam_fase.replace(11,10, inplace=True)
    df.fam_fase.replace(12, 11, inplace=True)
    df.fam_fase.replace(13, 11, inplace=True)
    df.fam_fase.replace(14, np.NaN, inplace=True)
    return df


def fixDisabilityPayment(df, labelOfDisability):
    disabilitySeries = df[labelOfDisability]
    df[labelOfDisability] = 2
    for index, row in disabilitySeries.items():
        if row > 0:
            df.at[index, labelOfDisability] = 1
    return df[labelOfDisability]


def fixDisabilityTotal(df, label):
    disabilitySeries = df[label]
    for index, row in disabilitySeries.items():
        if row == (-4) or row == 9 or row == 0:
            df.at[index, label] = 2
        if row > 9:
            df.at[index, label] = 1
    return df[label]


def fixSSHEduCoding(df, labelOfEduCode):
    educationSeries = df[labelOfEduCode].astype(str)
    educationSeries = educationSeries.str[:1]
    educationSeries.replace(5, 6, inplace=True)
    return educationSeries


def fix1995edu(df, labelOfEducation):
    educationSeries = df[labelOfEducation].astype(str)
    educationSeries = educationSeries.replace(np.nan, 9)
    df.replace(r'\s+', np.nan, regex=True)
    educationSeries = educationSeries.str[:1]
    return educationSeries


def fixOldEncoding(df, labelOfEducation):
    educationSeries = df[labelOfEducation].astype(str)
    educationSeries = educationSeries.str[:1]
    educationSeries.replace(3, 2, inplace=True)
    educationSeries.replace(4, 2, inplace=True)
    educationSeries.replace(5, 3, inplace=True)
    educationSeries.replace(6, 2, inplace=True)
    educationSeries.replace(7, 3, inplace=True)
    educationSeries.replace(8, 4, inplace=True)
    return educationSeries


def fixPopDensity(df, labelOfPopDensity):
    popDensitySeries = df[labelOfPopDensity]
    popDensitySeries.replace(11, 1, inplace=True)
    popDensitySeries.replace(12, 2, inplace=True)
    popDensitySeries.replace(13, 2, inplace=True)
    popDensitySeries.replace(14, 2, inplace=True)
    popDensitySeries.replace(15, 3, inplace=True)
    popDensitySeries.replace(16, 4, inplace=True)
    popDensitySeries.replace(17, 5, inplace=True)
    return popDensitySeries


def combineHealth(df, sickness, injury, combineHealthLabel):
    df[combineHealthLabel] = 2
    sicknessSeries = df[sickness]
    injurySeries = df[injury]
    for index, row in sicknessSeries.items():
        if row == 1:
            df.at[index, combineHealthLabel] = 1
    for index, row in injurySeries.items():
        if row == 1:
            df.at[index, combineHealthLabel] = 1
    return df[combineHealthLabel]


def fixNoChild(df, combine, firstSet, secondSet):
    df[combine] = 0
    first = df[firstSet]
    second = df[secondSet]
    for index, row in first.items():
        if row > 0:
            df.at[index, combine] += row
    for index, row in second.items():
        if row > 1:
            df.at[index, combine] += row
    return df[combine]


def fixMaritalStatus(df, labelOfMaritalStatus):
    maritalStatusSeries = df[labelOfMaritalStatus]
    maritalStatusSeries.replace(2, 't', inplace=True)
    maritalStatusSeries.replace(1, 2, inplace=True)
    maritalStatusSeries.replace('t', 1, inplace=True)
    return maritalStatusSeries


def inverseDisability(df, labelOfDisability):
    disabilitySeries = df[labelOfDisability]
    disabilitySeries.replace(2, 't', inplace=True)
    disabilitySeries.replace(1, 2, inplace=True)
    disabilitySeries.replace('t', 1, inplace=True)
    return disabilitySeries


def inverseHealth(df, labelOfHealth):
    healthSeries = df[labelOfHealth]
    healthSeries.replace(2, 't', inplace=True)
    healthSeries.replace(1, 2, inplace=True)
    healthSeries.replace('t', 1, inplace=True)
    return healthSeries


def fix1983Income(df, incomeLabel):
    incomeSeries = df[incomeLabel]
    incomeSeries = pd.to_numeric(incomeSeries, downcast='integer', errors='coerce')
    for index, row in incomeSeries.items():
        if row == 99999999:
            df.at[index, incomeLabel] = np.NaN
    return df[incomeLabel]


def streamlineDataframe1973(df):
    df['aargang'] = 1973
    df['alder_1'] = fixAge(df, 'v002', 73)
    df['utdnivaa'] = fixOldEncoding(df, 'v228')
    df['arb1_1'] = df['v003']
    df['sivstat_1'] = df['v146']
    df['saminnt_1'] = df['v406']
    df['hels2a'] = df['v220']
    df['hels2b'] = df['v243']
    df['antbarn'] = df['v149']
    df['ts_stor'] = df['v205']
    df['kjonn_1'] = df['v372']
    df['kode218_1'] = fixDisabilityPayment(df, 'v008')
    df = df.drop(columns=(['v002', 'v003', 'v228', 'v146', 'v406', 'v220', 'v243', 'v149', 'v205', 'v372', 'v008']))
    return df


def streamlineDataframe1983(df):
    df['aargang'] = 1983
    df['alder_1'] = fixAge(df, 'V10', 83)
    df['utdnivaa'] = fixSSHEduCoding(df, 'V1151')
    df['arb1_1'] = df['V457']
    #df['landsdel'] = df['v547']
    df['sivstat_1'] = df['V42']
    df['saminnt_1'] = fix1983Income(df, 'V1081')
    df['hels2a'] = df['V676']
    df['fam_fase'] = df['V1037']
    df['antbarn'] = df['V50']
    df['ts_stor'] = df['V41']
    df['kjonn_1'] = df['V12']
    df['kode218_1'] = df['V430']
    df = df.drop(columns=(['V10', 'V457', 'V1151', 'V42', 'V1081', 'V676', 'V1037', 'V50', 'V41', 'V12', 'V430']))
    return df


def streamlineDataframe1995(df):
    df['aargang'] = 1995
    df['alder_1'] = fixAge(df, 'v004', 95)
    df['utdnivaa'] = fix1995edu(df, 'v609')
    df['arb1_1'] = df['v312']
    df['landsdel'] = df['v547']
    df['sivstat_1'] = fixMaritalStatus(df, 'v107')
    df['saminnt_1'] = df['v613']
    df['hels2a'] = df['v424']
    df['fam_fase'] = df['v550']
    #df['antbarn0to10'] = df['v213']
    df['ts_stor'] = df['v006']
    df['kjonn_1'] = df['v005']
    df['kode218_1'] = df['v307']
    df = df.drop(columns=(['v613', 'v609', 'v312', 'v004', 'v107', 'v547', 'v424', 'v550', 'v006', 'v005', 'v307']))
    return df


def streamlineDataframe2005(df):
    df['aargang'] = 2005
    df['alder_1'] = df['v0002']
    df['utdnivaa'] = df['v1276']
    df['arb1_1'] = df['v0081']
    df['sivstat_1'] = df['v0011']
    df['fam_fase'] = df['v0012']
    df['saminnt_1'] = df['v2040']
    df['hels1'] = df['v0093']
    df['hels2a'] = df['v0095']
    df['hels2b'] = df['v0181']
    df['antbarn'] = fixNoChild(df, 'antbarn', 'v0020', 'v0013')
    df['landsdel'] = df['v0006']
    df['ts_stor'] = df['v0009']
    df['kjonn_1'] = df['v0004']
    df['kode218_1'] = df['v2300']
    df = df.drop(columns=(['v0002', 'v0081', 'v1276', 'v0011', 'v0012', 'v2040', 'v0093', 'v0095', 'v0006', 'v0181', 'v0020',
                           'v0013', 'v0009', 'v0004', 'v2300']))
    return df

#test1 = streamlineDataframe1973(df1973)
#test2 = streamlineDataframe1983(df1983)
#test3 = streamlineDataframe1995(df1995)
#test4 = streamlineDataframe2005(df2005)



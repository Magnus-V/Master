import os
import pandas as pd
import numpy as np



# Bærbare
my_data_folder = os.path.dirname(r'C:\Users\Magnus\Documents\Master\AmazonWebServices\survey_on_income_and_living_conditions\\')
# Stasjonære
#my_data_folder = os.path.dirname(r'C:\Users\Magnus L. Vestby\Documents\Universitetsarbeid\Master\INFO390\LivingConditionsSurvey\\')


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

df1973 = readCSVSurveyConvertToDataFrame(LivingConditionsSurvey1973)
df2017 = readCSVSurveyConvertToDataFrame(EUSILC2017)

def readDfAndReturnSeries(dataFrame, Seriesname):
    tempDataSeries = dataFrame[Seriesname]
    return tempDataSeries


df1973income = readDfAndReturnSeries(df1973, 'v406')
df2017income = readDfAndReturnSeries(df2017, 'wies_su')

def filterOutTheNonWorkingAgeGroups(dataFrame, SeriesName):
    tempDataSeries = dataFrame[dataFrame[AGEVARIABEL] > 24 && dataFrame[AGEVARIABLE] < 62]]
print(df1973income.mean)
print(df2017income.mean)
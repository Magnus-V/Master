import os
import pandas as pd
import numpy as np
import IPython


# my_data_folder = os.path.dirname(r'C:\Users\Magnus\Documents\Master\AmazonWebServices\survey_on_income_and_living_conditions\\')
# healthSurvey1968 = os.path.join(my_data_folder, r'HealthSurvey1968.csv')
# healthSurvey1975 = os.path.join(my_data_folder, r'HealthSurvey1975.csv')
# healthSurvey1985 = os.path.join(my_data_folder, r'HealthSurvey1985.csv')
# healthSurvey1995 = os.path.join(my_data_folder, r'HealthSurvey1995.csv')

my_data_folder_home = os.path.dirname(r'C:\Users\Magnus L. Vestby\Documents\Universitetsarbeid\Master\INFO390\LivingConditionsSurvey\\')
livingConditionsSurvey2018 = os.path.join(my_data_folder_home, r'LivingConditionsSurveyEUSILC2018.csv')
livingConditionsSurvey2017 = os.path.join(my_data_folder_home, r'LivingConditionsSurveyEUSILC2017.csv')

# healthSurvey1968csv = pd.read_csv(healthSurvey1968)
# healthSurvey1975csv = pd.read_csv(healthSurvey1975, low_memory=False)


def readCSVSurvey(csvfile):
    readCSV = pd.read_csv(csvfile, low_memory=False)
    return readCSV


def readCSVSurveyConvertToDataFrame(csvfile):
    readCSV = pd.read_csv(csvfile, low_memory=False)
    df_readCSV = pd.DataFrame(readCSV)
    return df_readCSV


csv1 = readCSVSurvey(livingConditionsSurvey2018)

# df1 = readCSVSurveyConvertToDataFrame(livingConditionsSurvey2018)
df2 = readCSVSurveyConvertToDataFrame(livingConditionsSurvey2017)
# print(list(df1.columns))

print(list(df2.columns))
avgInntekt = df2['saminnt_su'].mean()
avgLonnSu = df2['lonn_su'].mean()
avgLonnEtterSkatt = df2['wies_1'].mean()
print(avgInntekt)
print(avgLonnSu)
print(avgLonnEtterSkatt)

#print(df2.describe())
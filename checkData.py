import os
import pandas as pd
import numpy as np
import pyodbc


my_data_folder = os.path.dirname(r'C:\Users\Magnus\Documents\Master\AmazonWebServices\survey_on_income_and_living_conditions\\')
healthSurvey1968 = os.path.join(my_data_folder, r'HealthSurvey1968.csv')
healthSurvey1975 = os.path.join(my_data_folder, r'HealthSurvey1975.csv')
healthSurvey1985 = os.path.join(my_data_folder, r'HealthSurvey1985.csv')
healthSurvey1995 = os.path.join(my_data_folder, r'HealthSurvey1995.csv')

healthSurvey1968csv = pd.read_csv(healthSurvey1968)
healthSurvey1975csv = pd.read_csv(healthSurvey1975, low_memory=False)

def readCSVSurvey(csvfile):
    readCSV = pd.read_csv(csvfile)
    return readCSV

def readCSVSurveyConvertToDataFrame(csvfile):
    readCSV = pd.read_csv(csvfile)
    df_readCSV = pd.DataFrame(readCSV)
    return df_readCSV

csv1 = readCSVSurvey(healthSurvey1968)

df1 = readCSVSurveyConvertToDataFrame(healthSurvey1968)

print(df1)
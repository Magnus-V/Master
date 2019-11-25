import os
import pandas as pd
import numpy as np


# Bærbare
my_data_folder = os.path.dirname(r'C:\Users\Magnus\Documents\Master\AmazonWebServices\survey_on_income_and_living_conditions\\')
# Stasjonære
#my_data_folder = os.path.dirname(r'C:\Users\Magnus L. Vestby\Documents\Universitetsarbeid\Master\INFO390\LivingConditionsSurvey\\')

# healthSurvey1968 = os.path.join(my_data_folder, r'HealthSurvey1968.csv')
# healthSurvey1975 = os.path.join(my_data_folder, r'HealthSurvey1975.csv')
# healthSurvey1985 = os.path.join(my_data_folder, r'HealthSurvey1985.csv')
# healthSurvey1995 = os.path.join(my_data_folder, r'HealthSurvey1995.csv')
livingConditionsSurvey2017 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2017.csv')
livingConditionsSurvey2018 = os.path.join(my_data_folder, r'LivingConditionsSurveyEUSILC2018.csv')


def readCSVSurvey(csvfile):
    readCSV = pd.read_csv(csvfile, low_memory=False)
    return readCSV


def readCSVSurveyConvertToDataFrame(csvfile):
    readCSV = pd.read_csv(csvfile, low_memory=False)
    df_readCSV = pd.DataFrame(readCSV)
    return df_readCSV


df2017 = readCSVSurveyConvertToDataFrame(livingConditionsSurvey2017)


#print(list(df2017.columns))
#avgInntekt = df2['saminnt_su'].mean()
#avgLonnSu = df2['lonn_su'].mean()
#avgLonnEtterSkatt = df2017['wies_3'].mean()


def findCorrelation(x, y):
    corrArray = np.corrcoef(x, y)
    print(corrArray)
    return corrArray

def functionThatFindsCorrelationBetweenHigherThanAveragePay():
    # ha et array med gjennomsnittsverdier som gjenspeiler de verdier som gjenspeiler et gjennomsnittsperson i Norge i hver aldersgruppe
    # Bruker skriver inn sin inntekt og alder

    """"
    OKAY.

    Funksjon med array for gjennomsnittet, de under gj.snitt og de over gj.snitt. Finn de variablene som avviker mest.

    """

def createArrayWithAverageValues(dataFrame):
    addition = 0
    noRow = 0
    for row in dataFrame:
        addition =+ dataFrame['wies_3'].values(row)
        noRow =+ 1
    return addition/noRow

createArrayWithAverageValues(df2017)

def createArrayForThoseWithHigherPayAndTheirAverageValues():
    return

def createArrayForThoseWithLowerPayAndTheirAverageValues():
    return


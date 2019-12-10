import os
import pandas as pd
import numpy as np


# Bærbare
#my_data_folder = os.path.dirname(r'C:\Users\Magnus\Documents\Master\AmazonWebServices\survey_on_income_and_living_conditions\\')
# Stasjonære
my_data_folder = os.path.dirname(r'C:\Users\Magnus L. Vestby\Documents\Universitetsarbeid\Master\INFO390\LivingConditionsSurvey\\')

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

def listOfColumnsToBeUsedInProject():
    #Background variabels
    Sex = 'kjonn_1'
    Region = 'landsdel'
    IOs_familyPhase = 'fam_fase'
    sizeOfUrbanArea = 'ts_stor'
    ageGroup = 'aldgrupp'
    heightCm = 'bm1'
    weightKg = 'bm2'
    SelfdefinedSocioeconomicStatus = 'selvsosstat'
    HighestLevelOfEducation = 'utdnivaa'
    disabilityBenefits = 'bel21_8_su'
    TotalIncome = 'saminnt_su'
    IncomeAfterTax = 'wies_su'

    #Work variables
    currentMainActivity = 'naa_1'
    incomeFromWorkLastWeek = 'arb1_1'

    #Household variables
    IsIOMarriedCohabitant = 'siv_1'
    MaritalStatus = 'sivstat_1'
    ImmigrationCategory = 'invkat_1'
    NumberOfChildrenUnder17 = 'antbarn'
    ProblemsWithRot = 'bol6a'
    ProblemsWithMoisture = 'bol6b'
    ProblemsWithNoise = 'bol6d'
    ProblemsWithDustSmellOrPollution = 'bol6e'
    ProblemsWithCrime = 'bol6f'
    TypeOfHouse = 'hus'

    #Expenses and Economic Variables
    ProblemsPayingRent = 'prob1'
    ProblemsPayingMortgage = 'prob2'
    ProblemsPayingElectricityAndTaxes = 'prob3'
    ProblemsPayingOtherLoans = 'prob4'
    AffordOneWeekVacation = 'raad1'
    AffordMeatChickenOrFishEveryOtherDay = 'raad2'
    AffordToKeepHouseWarm = 'raad4'
    AffordToReplaceOutwornFurniture = 'raad5'
    SalesValueOfHouse = 'salg1'
    HandleUnforseenExpensesOfTenThousandNorwegianKroner = 'end3b'

    #Helse
    SelfAssesmentOfHealth = 'hels1'
    CronicPainOrHealthIssues = 'hels2a'
    DisabilitiesOrPainsCausedByInjury = 'hels2b'
    ConstraintsDailyActivity = 'hels3a1'
    LevelOfConstraints = 'hels3b'
    NeedForDentalCheckWithoutDoingIt = 'hels5a'
    ReasonForNotCheckDentalStatus = 'hels5b'
    DegreeOfFinancialBurdenOfHealthExpenses = 'hs200'
    DegreeOfFinancialBurdenOfDentalExpenses = 'hs210a'
    DegreeOfFinancialBurdenOfMedicinalExpenses = 'hs220'

    #SocialCapitalAndHappiness
    RatingOfHappiness = 'pw010'
    RatingOfMeaningfullness = 'pw020'
    RateYesterdaysFeelingOfHappiness = 'affekt1'
    RateYesterdaysFeelingOfWorry = 'affekt2'
    RateYesterdaysFeelingOfSadness = 'affekt3'
    HaveSomeoneCloseIfPersonalProblems = 'sk7a'
    TrustInPeople = 'soskap1'
    DoPeopleTreatOthersWell = 'soskap2'

    #Political participation and organizational work
    DidVoluntaryWork = 'org10a'
    BelongToAReligion = 'rel1a'



df2017 = readCSVSurveyConvertToDataFrame(livingConditionsSurvey2017)
print(df2017.head())


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


def removeEmptyStringsInDataFrameSeries(dataFrame, seriesName):
    dataFrame(str(seriesName)).replace('', np.nan, inplace=True)
    print(dataFrame(str(seriesName)))


#removeEmptyStringsInDataFrameSeries(df2017, 'wies_3')


def checkType(dataFrame):
    dataFrame['wies_3'].astype(bool)
    print(dataFrame[dataFrame['wies_3'].astype(bool)])

#checkType(df2017)

def createDictWithIndexValuesAndAverageValues(dataFrame, seriesName):
    chosenColumn = dataFrame[seriesName]
    dictWithValidInformation = dict()
    addition = 0
    noRow = 0
    filter = ' '
    for item in chosenColumn.iteritems():
        if item[1] != filter and int(item[1]) > 0:
            addition += int(item[1])
            noRow += 1
            dictWithValidInformation[item[0]] = item[1]
    dictWithValidInformation['avgValue'] = addition/noRow
    return dictWithValidInformation


def storeInDictionary(dataFrame, seriesName):
    tempDict = (createDictWithIndexValuesAndAverageValues(dataFrame, seriesName))
    print(tempDict.keys())


#storeInDictionary(df2017, 'wies_3')


#print(createArrayWithAverageValues(df2017, 'wies_3'))

def createArrayForThoseWithHigherPayAndTheirAverageValues():
    return


def createArrayForThoseWithLowerPayAndTheirAverageValues():
    return


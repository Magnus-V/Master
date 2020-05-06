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

def listOfColumnsToBeUsedInProject():
    #Background variabels
    BSex = 'kjonn_1'
    BRegion = 'landsdel'
    BIOsFamilyPhase = 'fam_fase'
    BSizeOfUrbanArea = 'ts_stor'
    BAgeGroup = 'aldgrupp'
    BHeightCm = 'bm1'
    BWeightKg = 'bm2'
    BSelfdefinedSocioeconomicStatus = 'selvsosstat'
    BHighestLevelOfEducation = 'utdnivaa'
    BDisabilityBenefits = 'bel21_8_su'
    BTotalIncome = 'saminnt_su'
    BIncomeAfterTax = 'wies_su'

    #Work variables
    WCurrentMainActivity = 'naa_1'
    WIncomeFromWorkLastWeek = 'arb1_1'

    #Household variables
    HIsIOMarriedCohabitant = 'siv_1'
    HMaritalStatus = 'sivstat_1'
    HImmigrationCategory = 'invkat_1'
    HNumberOfChildrenUnder17 = 'antbarn'
    HProblemsWithRot = 'bol6a'
    HProblemsWithMoisture = 'bol6b'
    HProblemsWithNoise = 'bol6d'
    HProblemsWithDustSmellOrPollution = 'bol6e'
    HProblemsWithCrime = 'bol6f'
    HTypeOfHouse = 'hus'

    #Expenses and Economic Variables
    EProblemsPayingRent = 'prob1'
    EProblemsPayingMortgage = 'prob2'
    EProblemsPayingElectricityAndTaxes = 'prob3'
    EProblemsPayingOtherLoans = 'prob4'
    EAffordOneWeekVacation = 'raad1'
    EAffordMeatChickenOrFishEveryOtherDay = 'raad2'
    EAffordToKeepHouseWarm = 'raad4'
    EAffordToReplaceOutwornFurniture = 'raad5'
    ESalesValueOfHouse = 'salg1'
    EHandleUnforseenExpensesOfTenThousandNorwegianKroner = 'end3b'

    #Health
    HeSelfAssesmentOfHealth = 'hels1'
    HeCronicPainOrHealthIssues = 'hels2a'
    HeDisabilitiesOrPainsCausedByInjury = 'hels2b'
    HeConstraintsDailyActivity = 'hels3a1'
    HeLevelOfConstraints = 'hels3b'
    HeNeedForDentalCheckWithoutDoingIt = 'hels5a'
    HeReasonForNotCheckDentalStatus = 'hels5b'
    HeDegreeOfFinancialBurdenOfHealthExpenses = 'hs200'
    HeDegreeOfFinancialBurdenOfDentalExpenses = 'hs210a'
    HeDegreeOfFinancialBurdenOfMedicinalExpenses = 'hs220'

    #SocialCapitalAndHappiness
    SRatingOfHappiness = 'pw010'
    SRatingOfMeaningfullness = 'pw020'
    SRateYesterdaysFeelingOfHappiness = 'affekt1'
    SRateYesterdaysFeelingOfWorry = 'affekt2'
    SRateYesterdaysFeelingOfSadness = 'affekt3'
    SHaveSomeoneCloseIfPersonalProblems = 'sk7a'
    STrustInPeople = 'soskap1'
    SDoPeopleTreatOthersWell = 'soskap2'

    #Political participation and organizational work
    PDidVoluntaryWork = 'org10a'
    PBelongToAReligion = 'rel1a'


    backgroundVariabelsList = [BSex, BRegion, BIOsFamilyPhase, BSizeOfUrbanArea, BAgeGroup, BHeightCm, BWeightKg,
                                   BSelfdefinedSocioeconomicStatus, BHighestLevelOfEducation, BDisabilityBenefits, BTotalIncome,
                                   BIncomeAfterTax]
    workVariabelsList = [WCurrentMainActivity, WIncomeFromWorkLastWeek]
    householdVariabelsList = [HIsIOMarriedCohabitant, HMaritalStatus, HImmigrationCategory, HNumberOfChildrenUnder17,
                                  HProblemsWithRot, HProblemsWithMoisture, HProblemsWithNoise, HProblemsWithDustSmellOrPollution,
                                  HProblemsWithCrime, HTypeOfHouse]
    economicVariabelsList = [EProblemsPayingRent, EProblemsPayingMortgage, EProblemsPayingElectricityAndTaxes,
                                 EProblemsPayingOtherLoans, EAffordOneWeekVacation, EAffordMeatChickenOrFishEveryOtherDay,
                                 EAffordToKeepHouseWarm, EAffordToReplaceOutwornFurniture, ESalesValueOfHouse,
                                 EHandleUnforseenExpensesOfTenThousandNorwegianKroner]
    healthVariabelsList = [HeSelfAssesmentOfHealth, HeCronicPainOrHealthIssues, HeDisabilitiesOrPainsCausedByInjury,
                               HeConstraintsDailyActivity, HeLevelOfConstraints, HeNeedForDentalCheckWithoutDoingIt,
                               HeReasonForNotCheckDentalStatus, HeDegreeOfFinancialBurdenOfHealthExpenses,
                               HeDegreeOfFinancialBurdenOfDentalExpenses, HeDegreeOfFinancialBurdenOfMedicinalExpenses]
    socialVariabelsList = [SRatingOfHappiness, SRatingOfMeaningfullness, SRateYesterdaysFeelingOfHappiness,
                           SRateYesterdaysFeelingOfWorry, SRateYesterdaysFeelingOfSadness, SHaveSomeoneCloseIfPersonalProblems,
                           STrustInPeople, SDoPeopleTreatOthersWell]
    politicalVariabelsList = [PDidVoluntaryWork, PBelongToAReligion]

    variabelList = [backgroundVariabelsList, workVariabelsList, householdVariabelsList, economicVariabelsList,
                    healthVariabelsList, socialVariabelsList,  politicalVariabelsList]

    return variabelList


df2017 = readCSVSurveyConvertToDataFrame(livingConditionsSurvey2017)

#print(df2017.head())

#print(listOfColumnsToBeUsedInProject())


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
    cleanDataframe = dataFrame(str(seriesName)).replace('', np.nan, inplace=True)
    print(dataFrame(str(seriesName)))
    return cleanDataframe


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


def createWageGroups(dataFrame):
    chosenColumns = dataFrame.filter(['wies_su', 'aldgrupp'])
    dictWithValidInformation = dict()
    addition = 0
    noRow = 0
    filter = ' '
    for item in chosenColumns.iteritems():
        if item[1] != filter and int(item[1]) > 0:
            addition += int(item[1])
            noRow += 1
            dictWithValidInformation[item[0]] = item[1]
    dictWithValidInformation['avgValue'] = addition / noRow
    return dictWithValidInformation


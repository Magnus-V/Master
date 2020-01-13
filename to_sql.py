# import the module
from sqlalchemy import create_engine
import os
import pandas as pd
import numpy as np
import pymysql
import cryptography


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


# create sqlalchemy engine
engine = create_engine("mysql+pymysql://admin:Jule@Nissen94@localhost/master_thesis"
                       .format(user="root",
                               pw="Jule@Nissen94",
                               db="master_thesis"))

def readCSVSurveyConvertToDataFrame(csvfile):
    readCSV = pd.read_csv(csvfile, low_memory=False)
    df_readCSV = pd.DataFrame(readCSV)
    return df_readCSV

df2017 = readCSVSurveyConvertToDataFrame(livingConditionsSurvey2017)


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

    variabelListAll = [BSex, BRegion, BIOsFamilyPhase, BSizeOfUrbanArea, BAgeGroup, BHeightCm, BWeightKg,
                        BSelfdefinedSocioeconomicStatus, BHighestLevelOfEducation, BDisabilityBenefits, BTotalIncome,
                        BIncomeAfterTax, WCurrentMainActivity, WIncomeFromWorkLastWeek,
                        HIsIOMarriedCohabitant, HMaritalStatus, HImmigrationCategory, HNumberOfChildrenUnder17,
                        HProblemsWithRot, HProblemsWithMoisture, HProblemsWithNoise, HProblemsWithDustSmellOrPollution,
                        HProblemsWithCrime, HTypeOfHouse, EProblemsPayingRent, EProblemsPayingMortgage, EProblemsPayingElectricityAndTaxes,
                        EProblemsPayingOtherLoans, EAffordOneWeekVacation, EAffordMeatChickenOrFishEveryOtherDay,
                        EAffordToKeepHouseWarm, EAffordToReplaceOutwornFurniture, ESalesValueOfHouse,
                        EHandleUnforseenExpensesOfTenThousandNorwegianKroner, HeSelfAssesmentOfHealth, HeCronicPainOrHealthIssues,
                        HeDisabilitiesOrPainsCausedByInjury,
                        HeConstraintsDailyActivity, HeLevelOfConstraints, HeNeedForDentalCheckWithoutDoingIt,
                        HeReasonForNotCheckDentalStatus, HeDegreeOfFinancialBurdenOfHealthExpenses,
                        HeDegreeOfFinancialBurdenOfDentalExpenses, HeDegreeOfFinancialBurdenOfMedicinalExpenses,
                        SRatingOfHappiness, SRatingOfMeaningfullness, SRateYesterdaysFeelingOfHappiness,
                        SRateYesterdaysFeelingOfWorry, SRateYesterdaysFeelingOfSadness,
                        SHaveSomeoneCloseIfPersonalProblems, STrustInPeople, SDoPeopleTreatOthersWell,PDidVoluntaryWork,
                        PBelongToAReligion]

    return variabelListAll

df2017filter = df2017.filter(items= listOfColumnsToBeUsedInProject())

df2017filter.to_sql('atbl_living_conditions_survey2017', con = engine, if_exists = 'append', chunksize = 1000)
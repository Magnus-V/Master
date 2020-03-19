
def createArrayOfConditions1973():
    income = 'v406'
    educationLevel = 'v228'
    sickness = 'v243'
    injury = 'v237'
    maritalStatus = 'v146'
    numberOfChildren = 'v149'
    housingPopDensity = 'v205'
    workType = 'v005'
    vacationFromHousework = 'v142'
    vacationOverFourWeeks = 'v073'
    sex = 'v372'
    recievesDisabilityPay = 'v008'

    array = [income, educationLevel, sickness, injury, maritalStatus, numberOfChildren, housingPopDensity, workType,
             vacationFromHousework, vacationOverFourWeeks, sex, recievesDisabilityPay,]
    return array

def createArrayOfConditions1983():
    income = 'V1081'
    educationLevel = 'V1147'
    #sickness =
    consultationWithDoctor = 'V668'
    #injury = 'v237'
    maritalStatus = 'V42'
    numberOfChildren = 'V50'
    housingPopDensity = 'v205'
    housingType = 'V196'
    workType = 'V459'
    #vacationFromHousework = ''
    #vacationOverFourWeeks = ''
    sex = 'V12'
    recievesDisabilityPay = 'V430'

    array = [income, educationLevel, consultationWithDoctor, maritalStatus, numberOfChildren, housingPopDensity, housingType,
             workType, sex, recievesDisabilityPay,]
    return array

def createArrayOfConditions1995():
    income = 'v613'
    educationLevelSSBCoded = 'v609'
    sicknessLongTerm = 'v424'
    injuryCausedByViolence = 'v468'
    maritalStatus = 'v107'
    numberOfChildren0to10 = 'v213'
    housingPopDensity = 'v006'
    housingType = 'v007'
    workTypeAlphaNumericalCoded = 'v386'
    sex = 'v005'
    recievesDisabilityPay = 'v307'


    array = [income, educationLevelSSBCoded, sicknessLongTerm, injuryCausedByViolence, maritalStatus, numberOfChildren0to10,
             housingPopDensity, housingType, workTypeAlphaNumericalCoded, sex, recievesDisabilityPay]
    return array

def createArrayOfConditions2005():
    #age = NEEDTOFIX
    income = 'v2040'
    educationLevel = 'v1276'
    sicknessLongTerm = 'v0095'
    injuryLast12Months = 'v1455'
    county = 'v0006'
    familyPhase = 'v0012'
    maritalStatus = 'v0011'
    numberOfChildren6to15 = 'v0013'
    numberOfChildren0to5 = 'v0020'
    housingPopDensity = 'v0009'
    typeOfHousehold = 'v1288'
    workType = 'v1398'
    sex = 'v0004'
    degreeOfDisability = 'v2300'
    weightKg = 'v0376'
    heightCm = 'v0375'

    array = [income, educationLevel, sicknessLongTerm, injuryLast12Months, maritalStatus, familyPhase, county,
             numberOfChildren6to15, numberOfChildren0to5, housingPopDensity, typeOfHousehold, workType,
             sex, degreeOfDisability, weightKg, heightCm]
    return array


def createArrayOfConditions2014():
    surveyYear = 'aargang'
    age = 'alder_1'
    income = 'aggi_18_1'
    educationLevel = 'utdnivaa_nus2000_1'
    selfRatingOfHealth = 'hels1'
    sicknessLongTerm = 'hels2a'
    injuryLast12Months = 'hels2b'
    familyPhase = 'fam_fase'
    maritalStatus = 'sivsta_1'
    numberOfChildren0to16 = 'antbarn'
    housingPopDensity = 'ts_stor'
    county = 'landsdel'
    socioEconomicStatus = 'selvsosstat'
    sex = 'kjonn_1'
    DisabilityPayment = 'kode218_1'

    array = [surveyYear, age, income, educationLevel, selfRatingOfHealth, sicknessLongTerm, injuryLast12Months,
             maritalStatus, familyPhase, numberOfChildren0to16, housingPopDensity, county, socioEconomicStatus,
             sex, DisabilityPayment]
    return array


def createArrayOfConditions2015():
    surveyYear = 'aar'
    age = 'alder_1'
    income = 'aggi_18_1'
    educationLevel = 'utdnivaa'
    selfRatingOfHealth = 'hels1'
    sicknessLongTerm = 'hels2a'
    injuryLast12Months = 'hels2b'
    familyPhase = 'fam_fase'
    maritalStatus = 'sivstat_1'
    numberOfChildren0to16 = 'antbarn'
    housingPopDensity = 'ts_stor'
    county = 'landsdel'
    socioEconomicStatus = 'selvsosstat'
    sex = 'kjonn_1'
    DisabilityPayment = 'kode218_1'

    array = [surveyYear, age, income, educationLevel, selfRatingOfHealth, sicknessLongTerm, injuryLast12Months,
             maritalStatus, familyPhase, numberOfChildren0to16, housingPopDensity, county, socioEconomicStatus,
             sex, DisabilityPayment]
    return array

def createArrayOfConditions2016():
    surveyYear = 'aar'
    age = 'alder_1'
    income = 'saminnt_1'
    educationLevel = 'utdnivaa'
    selfRatingOfHealth = 'hels1'
    sicknessLongTerm = 'hels2a'
    injuryLast12Months = 'hels2b'
    familyPhase = 'fam_fase'
    maritalStatus = 'sivstat_1'
    numberOfChildren0to16 = 'antbarn'
    housingPopDensity = 'ts_stor'
    county = 'landsdel'
    socioEconomicStatus = 'selvsosstat'
    sex = 'kjonn_1'
    DisabilityPayment = 'bel21_8_1'

    array = [surveyYear, age, income, educationLevel, selfRatingOfHealth, sicknessLongTerm, injuryLast12Months,
             maritalStatus, familyPhase, numberOfChildren0to16, housingPopDensity, county, socioEconomicStatus,
             sex, DisabilityPayment]
    return array

def createArrayOfConditions2017():
    surveyYear = 'aar'
    age = 'alder_1'
    income = 'saminnt_1'
    educationLevel = 'utdnivaa'
    selfRatingOfHealth = 'hels1'
    sicknessLongTerm = 'hels2a'
    injuryLast12Months = 'hels2b'
    familyPhase = 'fam_fase'
    maritalStatus = 'sivstat_1'
    numberOfChildren0to16 = 'antbarn'
    housingPopDensity = 'ts_stor'
    county = 'landsdel'
    socioEconomicStatus = 'selvsosstat'
    sex = 'kjonn_1'
    DisabilityPayment = 'bel21_8_1'
    weightKg = 'bm2'
    heightCm = 'bm1'

    array = [surveyYear, age, income, educationLevel, selfRatingOfHealth, sicknessLongTerm, injuryLast12Months, maritalStatus, familyPhase,
             numberOfChildren0to16, housingPopDensity, county, socioEconomicStatus,
             sex, DisabilityPayment, weightKg, heightCm]
    return array

def createArrayOfConditions2018():
    surveyYear = 'aar'
    age = 'alder_1'
    income = 'saminnt_1'
    educationLevel = 'utdnivaa'
    selfRatingOfHealth = 'hels1'
    sicknessLongTerm = 'hels2a'
    injuryLast12Months = 'hels2b'
    familyPhase = 'fam_fase'
    maritalStatus = 'sivstat_1'
    numberOfChildren0to16 = 'antbarn'
    housingPopDensity = 'ts_stor'
    county = 'landsdel'
    socioEconomicStatus = 'selvsosstat'
    sex = 'kjonn_1'
    DisabilityPayment = 'bel21_8_1'
    weightKg = 'bm2'
    heightCm = 'bm1'

    array = [surveyYear, age, income, educationLevel, selfRatingOfHealth, sicknessLongTerm, injuryLast12Months, maritalStatus, familyPhase,
             numberOfChildren0to16, housingPopDensity, county, socioEconomicStatus,
             sex, DisabilityPayment, weightKg, heightCm]
    return array
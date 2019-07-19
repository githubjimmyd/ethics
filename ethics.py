# Jim Davies
# jim@jimdavies.org
# ethics.py
# Version 2019-07-19
# Started July 18, 2019



## This variable is the humber of kilograms of CO2e estimated by the WHO to produce 1 DALY of suffering.
oneDALY2carbonConversion = 5000000.00 ## five million kg oc CO2e causes 1 DALY of suffering

## This variable is the number of kilograms of CO2e emitted into the atmosphere caused by raising 1kg of chicken meat.
chickenmeat2carbonConversion = 5.0

## This variable is the number of kilograms of CO2e emitted into the atmosphere caused by raising 1kg of beef from cattle.
beef2carbonConversion = 35.0

## This variable is the number of kilograms in an average broiler chicken.
kgMeatPerChicken = 1.5

## This variable is the age at which a broiler chicken is slaughtered for meat.
yearsChickenLife = (1.0/6.0) # two months is one sixth of a year.

## This variable is the age at which a head of cattle is slaughtered for meat.
yearsCowLife = 1.5 # eighteen months is a year and a half

## This variable is the number of kilograms of meat in an average head of cattle at slaughter time.
## If we assume 1 head of cattle weighs an average of 1200 pounds (544.3kg), we can expect to get 750 pounds of meat from it (340.2kg).
## citation: Holland, R., Loveday, D. & Ferguson, K. (N.D.). How  Much Meat to Expect From a Beef Carcass. University of Tennessee Institute of Agriculture Technical Report PB1822.
kgMeatPerCow = 340.2

## This variable is the estimated mass of meat eaten in a typical meal, in kilograms.
kgMealSize = .028 # 10 ounces = 0.28kg

## A reduction in demand at the store causes a reduction in prices, which increases sales. So reducing chicken consumption from,
##   say, 10 birds to 0 causes a demand reduction of less than 10. How much less is called the cumulative elasticity factor.
##   Estimates for this vary widely for meat, especially fish, but for chickens it’s about 0.6.
##   This means that eating 10 fewer chickens can be expected to result in 6 fewer chickens being farmed.
## citation: https://animalcharityevaluators.org/research/dietary-impacts/effects-of-diet-choices/
chickenElasticityFactor = 0.6

secondsPerYear = 31540000
minutesPerYear = 525600

## These variables are estimates of how much suffering animals experience relative to humans. If a human experiences a suffering of 1,
##    for example, a chicken will suffer 0.0038, based on estimates of number of neurons in the chicken cortex.
## These estimates come from: Scherer, L., Tomasik, B., Rueda, O., & Pfister, S. (2018). Framework for integrating animal welfare into life cycle sustainability assessment. The international journal of life cycle assessment, 23(7), 1476-1490.
cattleSentienceDiscount =	0.035
pigSentienceDiscount =		0.027
chickenSentienceDiscount =	0.0038
salmonSentienceDiscount =	0.0012
shrimpSentienceDiscount =	0.0000012
cricketSentienceDiscount =	0.0000029
mealwormSentienceDiscount = 	0.00000029
cowSentienceDiscount =	        cattleSentienceDiscount
# we assume that mealworms represent sentience of bugs: insects, spiders, moths, aphids, and other small invertebrates.
bugSentienceDiscount =	        mealwormSentienceDiscount

def dalys2carbon(DALYs=1):
    '''Takes in a number of DALYs (default 1) and outputs the kg of CO2e to be released into the atmosphere to cause that much suffering.'''
    ## to do this, we muliply the number of DALYs times how many kg of CO2e it takes to cause 1 DALY.
    return DALYs * oneDALY2carbonConversion

def carbon2dalys(kgCarbon=1):
    '''Takes in some number of kg of carbon dioxide (CO2e) and ouputs what the WHO estimates to be suffering, measured in DALYs'''
    ## to do this, we divide the kg of CO2e emitted (default 1), and divide it by the number of kg it takes to create 1 DALY.
    DALYs = kgCarbon / oneDALY2carbonConversion
    return DALYs
## testing function. Should print 5 million
print "1 DALY of suffering is caused by an estimated", dalys2carbon(1), "kilograms of CO2e emitted into the atmosphere."


def chickenmeat2carbon(kgChickenmeat):
    '''Takes in some number of kg of chicken meat raised and outputs the estimated kg of carbon emitted into the atmosphere.'''
    carbonReleased = kgChickenmeat * chickenmeat2carbonConversion
    return carbonReleased

def beef2carbon(kgBeef):
    ''' Takes in some number of kg of beef raised and outputs the estimated kg of carbon emitted into the atmosphere.'''
    carbonReleased = kgBeef * beef2carbonConversion
    return carbonReleased

def daly2chickenmeat(DALYs=1):
    '''For some number of input DALYs, how many kilograms of chicken meat would need to be raised to cause them?'''
    ## to figure this out, we look at how many kilograms of CO2e cause 1 DALY of suffering.
    kg_of_carbon_for_one_DALY = dalys2carbon(1)
    ## and we divide that by the number of kilgrams of CO2e caused by raising 1kg of chicken meat.
    kg_of_carbon_for_one_kg_chickenmeat = chickenmeat2carbon(1)
    ## This gives us a number of kilograms of chicken meat needed to cause 1 DALY.
    chickenmeat_for_one_DALY = kg_of_carbon_for_one_DALY / kg_of_carbon_for_one_kg_chickenmeat
    ## But the input number might not be 1 DALY, so we multiply this result by the input number.
    kgChickenmeat = DALYs * chickenmeat_for_one_DALY
    ## This value is the kg of chicken meat that would be raised to produce the input number of DALYs.
    return kgChickenmeat
## Testing function. Shoud print 1 million
print "1 DALY of human suffering due to climate change is caused by", daly2chickenmeat(1),"kg of chicken meat raised."

def chickenmeat2chickens(kgChickenmeat):
    '''Takes some number of kilograms of chicken meat, and returns how many chickens would be needed to produce it.'''
    numberOfChickens = kgChickenmeat / kgMeatPerChicken
    return numberOfChickens
## Testing function. Should return 666666.666667 chickens
print "It takes the raising of", chickenmeat2chickens(daly2chickenmeat(1)) ,"chickens to create", daly2chickenmeat(1), "kg of chicken meat,"\
      "which causes 1 human DALY of climate change damage, becaue there is", kgMeatPerChicken,"kg of meat on a chicken."

def chickens2yearsOfChickenLife(chickens):
    '''takes in a number of chickens and returns how many years of life that number of chickens would live, given their lifespan in a farm.'''
    yearsOfChickenLife = chickens * yearsChickenLife
    return yearsOfChickenLife
## Testing function. Should print 111,111.11
print "Raising", chickenmeat2chickens(daly2chickenmeat(1)), "chickens requires", \
      chickens2yearsOfChickenLife(chickenmeat2chickens(daly2chickenmeat(1))),"years of chicken life in farms, because chickens live", yearsChickenLife, \
      "years (about two months) before slaughter."

print "A year of chicken suffering is estimated to be", chickenSentienceDiscount, "as bad as a human's."
## this variable is the years of chicken suffering involved with creating CO2e emissions that would result in 1 DALY for humans
yearsOfChickenSufferingForOneDALY = chickens2yearsOfChickenLife(chickenmeat2chickens(daly2chickenmeat(1)))

def Species_YearsOfAnimalSuffering2DALYs(theSpecies, years):
    '''Takes in a species (theSpecies) and some number of years and returns equivalent DALYs of suffering, according to that animal's sentience.'''
    if theSpecies == "chicken":
        return years * chickenSentienceDiscount
    if (theSpecies == "cattle") or (theSpecies == "cow") or (theSpecies =="steer") or (theSpecies == "beef"):
        return years * cattleSentienceDiscount
    else:
        print "ERROR: that animal is not defined in function Species_YearsOfAnimalSuffer2DALYs."
## testing function. Should result in 422.22
DALYsForChickens = yearsOfChickenSufferingForOneDALY
print yearsOfChickenSufferingForOneDALY, "years of suffering for a chicken, at a discount rate of", cattleSentienceDiscount, \
      "means the equivalent of", Species_YearsOfAnimalSuffering2DALYs("chicken", DALYsForChickens), "of DALYs directly suffered by chickens."

print "Therefore, every time humanity raises enough chicken to cause 1 DALY to humans from climate change damage, they cause the equivalent of", \
    Species_YearsOfAnimalSuffering2DALYs("chicken", DALYsForChickens), "DALYs of chicken suffering to make the meat."

print daly2chickenmeat(1), "kg of chicken causes 1 human DALY +", Species_YearsOfAnimalSuffering2DALYs("chicken", DALYsForChickens), \
      "chicken DALYs =", (1 + Species_YearsOfAnimalSuffering2DALYs("chicken", DALYsForChickens)), "total DALYs caused by eating", \
      daly2chickenmeat(1),"kg of chicken meat."

## This adds the human DALY (1) due to climate change to animal suffering equivalent DALYS, and divides by the kg of meat needed to create 1
##    climate-change human DALY to find the DALYs caused by that much chicken. Divide that to get total DALYs per kg of chicken meat.
DALYsPerKgOfChicken = (1 + Species_YearsOfAnimalSuffering2DALYs("chicken", DALYsForChickens)) / daly2chickenmeat(1)
print "If we divide", (1 + Species_YearsOfAnimalSuffering2DALYs("chicken", DALYsForChickens)), "by",  daly2chickenmeat(1), \
    "we get the DALYs caused by raising one kilogram of chicken meat, which is", DALYsPerKgOfChicken, "DALYs."

DALYsPerKgOfChickenEaten = chickenElasticityFactor * DALYsPerKgOfChicken
print "Eating chicken does not directly cause more chicken to be raised. There is an elasticity factor of", chickenElasticityFactor, \
      ", which must be multiplied."
print "This results in", DALYsPerKgOfChickenEaten, "DALYs caused by *eating* 1 kilogram of chicken."

print " " ## this is just a line break.
print "What is the moral cost of eating chicken for dinner, assuming a portion size of", kgMealSize, "kg? (this is 10 ounces)"
chickenMealImpact = kgMealSize * DALYsPerKgOfChickenEaten
print kgMealSize, "kg *", DALYsPerKgOfChickenEaten, "DALYs =", chickenMealImpact, "DALYs caused per chicken dinner."
print "This number is small, so we'll think in terms of seconds. There are", secondsPerYear, "seconds in a year."
print "One year is", secondsPerYear, "seconds."
print "So one DALY is", secondsPerYear, "DALSs, or disability-adjusted life seconds."
print "If we multiply DALYs caused per chicken dinner by the number of seconds in a year,"
disabilityAdjustedLifeSecondsPerChickenMeal = chickenMealImpact * secondsPerYear
disabilityAdjustedLifeMinutesPerChickenMeal = chickenMealImpact * minutesPerYear
print "that's", chickenMealImpact, "*", secondsPerYear, "=", disabilityAdjustedLifeSecondsPerChickenMeal
print "This means that eating a meal of chicken is expected to cause suffering in a human expected to last", disabilityAdjustedLifeSecondsPerChickenMeal, \
      "seconds."
print "In minutes, it's", disabilityAdjustedLifeMinutesPerChickenMeal, "disability-adjusted life minutes."
print "In other words, having chicken for dinner causes an estimated", disabilityAdjustedLifeMinutesPerChickenMeal, "minutes of equivalent human suffering,"
print "due to climate change, but mostly because of direct chicken suffering."


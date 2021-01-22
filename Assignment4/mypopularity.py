# CMPT 120
# Poplularity Contest
# Author: Henry Yin
# Section: D200

# DATA
# Lists that will be used in dialog
lst_season=["Spring","Summer","Fall","Winter"]
season_accum=[0]*4

lst_day=["sun-cold","clou-warm"]
day_accum=[0]*2

rate_accum=0

lst_month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
month_accum=[0]*12





# Ask Seasons
def season_preference():
    print("\nWhich seasons do you prefer?")
    print("\nCoding used for seasons")
    print("0 - Spring")
    print("1 - Summer")
    print("2 - Fall")
    print("3 - Winter")
    season_code=int(input("\nPlease Provide a season code-->"))
    return season_code

# Ask Type of day if winter
def type_of_day_preference():
    print("\nSince you prefer Winter...")
    print("\nWhat type of day do you prefer in Winter?")
    print("Coding used for type of day")
    print("sun-cold: Sunny and cold")
    print("clou-warm: Cloudy and warm")
    day_code=input("\nPlease provide a type day code-->")
    return day_code

# Ask Chocolate rating
def chocolate_rating():
    print("\nPlease rate how much you like chocolate")
    print("from 1 to 5, 1 - not at all, 5 - you love it!")
    rate_code=int(input("\nPlease provide your chocolate rateing-->"))
    return rate_code

# Ask Month 
def month_preference():
    print("\nWhich month do you prefer?")
    for i in range (1,13):
        print(i,"-",lst_month[i-1])
    month_code=int(input("\nPlease provide your preferred month-->"))
    return month_code
    
#############
# TOP LEVEL

# Greeting
print("Hi dear user!!")

# Ask number of people
n=int(input("\nHow many people shall we interview?-->"))

# Collect data using for loop
for i in range(n):
    print("\nPerson...",i+1)

    rec_season = season_preference()
    season_accum[rec_season] += 1

    if(rec_season == 3):
        rec_day = type_of_day_preference()
        day_accum[lst_day.index(rec_day)] += 1

    rec_rate = chocolate_rating()
    rate_accum += rec_rate

    rec_month = month_preference()
    month_accum[rec_month - 1] += 1

    print("\n** All data of person",i+1,"collected **")

# Concolusion
print("\nTOTALS")

print("\n======")

print("\nTRACE...list seasons accumulators:",season_accum)

print("\n----Seasons preferred----")

print("\nSeason \t total people \t % wrt.all respondents")
print("Spring \t   ", season_accum[0], "\t          ", season_accum[0]/n*100,"%")
print("Spring \t   ", season_accum[1], "\t          ", season_accum[1]/n*100,"%")
print("Spring \t   ", season_accum[2], "\t          ", season_accum[2]/n*100,"%")
print("Spring \t   ", season_accum[3], "\t          ", season_accum[3]/n*100,"%")


print("\nTRACE...number of people who voted winter:",season_accum[3])

print("\n----Type of day in Winter----")

print("\nType of day \t total people \t % wrt. Winter respondents")
print("Sunny,cold \t     ",day_accum[0], "\t          ", day_accum[0]/season_accum[3]*100,"%")
print("Cloudy,warm \t     ",day_accum[1], "\t          ", day_accum[1]/season_accum[3]*100,"%")

print("\nTRACE...total accumulating rates choco:",rate_accum)

print("\n----Average rate chocolate----",rate_accum/n)

print("\nTRACE...number of people each month:",month_accum)
import math
print("TRACE...maximum in month list:",max(month_accum))
print("TRACE...first index with maximum:",month_accum.index(max(month_accum)))

print("\n----Most preferred month----",lst_month[month_accum.index(max(month_accum))])

print("\nBye!!!")

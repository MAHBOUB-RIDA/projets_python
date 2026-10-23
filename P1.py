print("---Age in Days calculatar ")

ageYears = input("Enter yours age in years : ") # 10
ageYears = int(ageYears)

# Age en mois
ageMonths = ageYears*12

# Age en jour
ageDays = ageYears*365

# Age en houres
ageHours = ageDays*24

# Age en secondes
ageScends = ageDays*24*60*60

print(f"You have lived for {ageYears} years, and {ageMonths} month, and {ageDays} days, and {ageHours} hour, and {ageScends} second.")
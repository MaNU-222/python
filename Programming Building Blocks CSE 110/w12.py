import math
with open("life-expectancy.csv") as life_data:
    next(life_data)

    country_min = " "
    maximum_year = -math.inf
    minimum_year = math.inf

    country_max = " "
    maximum_age = -math.inf
    minimum_age = math.inf
    
    average = []

    country_ma = " "
    country_mi = " "

    age_max = -math.inf
    age_min = math.inf

    year_max = -math.inf
    year_min = math.inf


    interest = int(input("Enter the year of interest: "))
    #countty_of_interest = input("Enter Country of interest: ")

    for line  in life_data:
        parts = line.split(",")

        country_name = parts[0]
        abraviation = parts[1]
        year = int(parts[2])
        ages = float(parts[3])


        if ages > maximum_age:
            maximum_age = ages
            country_max = country_name
            maximum_year = year

        if ages < minimum_age:
            minimum_age = ages
            country_min = country_name
            minimum_year = year
        
        if year == interest:
            average.append(float(parts[3]))
            average_answer = sum(average) / len(average)

        if year == interest:
            year_max = float(ages)
            country_ma = country_name

        if year == interest:
            year_min = float(ages)
            country_mi = country_name


    print()
    print(f"The overall max life expectancy is: {maximum_age} from {country_max} in {maximum_year}")
    print(f"The overall min life expectancy is: {minimum_age} from {country_min} in {minimum_year}")
    print()

    print(f"For the year {interest}")
    print(f"The average life expectancy across all countries was {average_answer:.2f}")
    print(f"The max life expectancy was in {country_ma} with {interest}")
    print(f"The min life expectancy was in {country_min} with {year_min}")
    print()
    

    
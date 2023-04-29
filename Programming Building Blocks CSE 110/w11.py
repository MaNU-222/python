import math
with open("life-expectancy.csv") as life_data:
    next(life_data)
    
    maximum_count = -math.inf
    minimum_count = math.inf

    for line  in life_data:
        parts = line.split(",")

        country_name = parts[0]
        abraviation = parts[1]
        year = int(parts[2])
        ages = float(parts[3])

        if float(ages) > maximum_count:
            maximum_count = ages
        if float(ages) < minimum_count:
            minimum_count = ages

    print(f"The maximum life expetancy is: {maximum_count}")
    print(f"The minimum life expentancy is: {minimum_count}")
    print()
       
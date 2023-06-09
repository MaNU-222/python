def main():
    #get an odometervalue in U.S miles from the user.
    start_miles = float(input("Enter the first odometer reading (miles): "))
    
    #get another odometer value in U.S miles from the user.
    end_miles = float(input("Enter the second odometer reading (miles): "))
    
    #get the fuel amount in U.S gallons from user.
    amount_gallons = float(input("Enter amount fuel used (gallons): "))

    # call the miles per gallon function per and store
    # the result in a variable named mpg
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # call the lp100k from mpg function to convert the 
    # miles per gallon to liters per 100 kilometers and 
    # store the result in a variableb lp100k
    lp100k = lp100k_from_mpg(mpg)


# Display the result for the user to see
print(f"{mpg:.1f} miles per gallon")
print(f"{lp100k:.2f} liters per 100 kilometers") 


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute mand return the average number of miles that a vehicle travelled 
    per gallon of fuel 
    parameters
        start_miles: An odometer value in miles
        end_miles: another odometer value in miles.
        amount_gallon: A fuel amount in U.S gallons
    Return: fuel efficiency in miles per gallon.
    """
    mpg = abs(end_miles - start_miles) / amount_gallons
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    parameters mpg: A value in miles per gallon 
    Return: The converted value in liters per 100km.
     """
    lp100k = 235.215 / mpg
    return lp100k


# call the main function so that
# this program will start executing 
main()

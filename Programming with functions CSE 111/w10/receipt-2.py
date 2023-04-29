import csv
from datetime import datetime

def main():
    try:
    
        # index of some of the colums in the product.cvs
        PRODUCT_NUMBER = 0
        PRICE_INDEX = 2

        # read the content of product.cvs into a compound dictionary named product_dict
        products_dict = read_dict("products.csv", PRODUCT_NUMBER)

        # Print the compound product dictionary
        #print("ALL PRODUCTS")
        #print(products_dict)

        PRODUCT_NUMBER = 0
        PRODUCT_QUANTITY = 1

        current_date_time = datetime.now()

        # THIS OPEN THE FILE FOR REWADING 

        with open("request.csv", "rt") as request:
        
            reader = csv.reader(request)

            next(reader)

            #create empty list
            total = []
            total_price = []

            print("=" * 21)
            print("M AND E SHOPPING MALL")
            print("=" * 21)
            print()

            for line in reader:
                key = line[0]
                number_of_items = float(line[1])
                product_info = products_dict[key]
                name = product_info[1]
                product_cost = float(product_info[2])

                total.append(number_of_items)
                total_price.append(product_cost)

                print(f"{name}: {number_of_items} @ {product_cost} ")

        
            total_price = sum(total_price)
            total = sum(total)

            tax = 0.06 * total_price
            total_tax = tax + total_price
        
            print()
            print(f"Number of items: {total}")
            print(f"Subtotal: ${total_price:.2f}")
            print(f"Sales Tax: {tax:.2f}")
            print(f"Total: {total_tax:.2f}")
            print("." * 60)

            print("Please visit our website and complete the following survey")
            print("To help us know how we will serve you well")
            print(">>>>> www.mandeshopping.com")
            print()
            print("Thank you for shopping at the M and E Shopping Mall.")
            print("." * 60)
            print(f"{current_date_time: %A %I:%M%p %Y - %m} " )
            print("." * 26)




    except PermissionError as permerr:
            print(permerr)

    except FileNotFoundError as filenot:
            print(filenot)

    except KeyError as key:
        print(key)


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    #craete an empty dictionay that will store the data from cvs file
    dictionary = {}


    #open the cvs file for reading
    with open(filename, "rt") as csv_file:

        #this will create a reader object that will read fron the opened file
        reader = csv.reader(csv_file)

        # this skips the first line in the file
        next(reader)

        # Read the rows in the cvs file, one row at a time 
        # the reader object returns each row as a list
        for row_list in reader:
        
            #if the current row is not blank, add the data from the current to the dictionary. 
            if len(row_list) != 0:
        
                # from the current row, retrieve the data 
                # from the column that contains the key
                key = row_list[key_column_index]

            # store the data from thr current row into dictionary 
            dictionary[key] = row_list

        return dictionary
    
#call the main
if __name__== "__main__":
    main()


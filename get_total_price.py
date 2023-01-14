import csv
def get_total_price(fname:str)->float:
    """
    This function returns the total price of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    file = open('fruits.csv')
    reader = list(csv.reader(file))[1:]
    sum = 0
    for row in reader:
        sum+=float(row[1])
    
    return sum
print(get_total_price('fruits.csv'))

    
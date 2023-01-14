import csv
def get_frutis_name(fname:str)->list:
    """
    This function returns the name of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits names
    """
    file = open('fruits.csv')
    reader = csv.reader(file)
    lst = []
    for row in reader:
        if row[0] != 'name':
            lst.append(row[0])
            
    return lst
print(get_frutis_name('fruits.csv'))

    
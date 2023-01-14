import csv
def get_cheapest_fruit_id(fname:str)->id:
    """
    This function returns the index of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    file = open('fruits.csv')
    reader = csv.reader(file)
    lst1 = []
    lst2 = []
    for row in reader:
        if row[1] != 'price':
            lst1.append(row[0])
            lst2.append(row[1])
    s = ''
    min = lst2[0]
    for i in range(1,len(lst2)):
        if float(lst2[i]) < float(min):
            min = lst2[i]
            s = lst1[i]
    return lst1.index(s)
print(get_cheapest_fruit_id('fruits.csv'))
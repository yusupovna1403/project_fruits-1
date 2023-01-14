import csv
def get_expensive_fruit(fname:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
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
    max = lst2[0]
    for i in range(1,len(lst2)):
        if float(lst2[i]) > float(max):
            max = lst2[i]
            s = lst1[i]
    return s
print(get_expensive_fruit('fruits.csv'))
     



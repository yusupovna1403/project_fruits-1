def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    # your code here
    rows = data.split()[1:]
    price = []
    name = []

    for row in rows:
        price.append(float(row.split(',')[1]))
        name.append(row.split(',')[0])


    idx = 0
    mprice = price[idx]

    for i in range(len(price)):
        if price[i]>mprice:
            mprice=price[i]
            idx = i  

    return name[idx]    

data = open('fruits.csv').read()

print(get_expensive_fruit(data))


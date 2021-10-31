def appleCost():
    """ Function for total Cost of apples """
    # The cost of each apple is 20
    appleFunc = int(input('Enter the amount of apples that you want to buy: '))*20
    return appleFunc

def orangeCost():
    """ Function for total Cost of oranges """
     # The cost of each apple is 25
    orangeFunc = int(input('Enter the amount of oranges that you want to buy: '))*25
    return orangeFunc

def displayOutput(appleF, orangeF):
    print(f'The total amount is Php {appleF+orangeF:.2f}.')

apple = appleCost()
orange = orangeCost()
displayOutput(apple, orange)
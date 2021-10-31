def moneyAmount():
    """ Function for money input """
    moneyFunc = float(input('Enter the amount of your money: '))
    return moneyFunc

def appleCost():
    """ Function for the price input """
    costFunc = float(input('Enter the price of an apple: '))
    return costFunc

def amountApple():
    """ Compute and return the amount of apples that you can buy """
    appleFunc = int(money/cost)
    return appleFunc

def amountChange():
    """ Compute and return the amount of change that you will have """
    changeFunc = float(money%cost)
    return changeFunc

def displayOutput(applesF, changeF):
    print(f'You can buy {applesF} apples and your change is {change:.2f} pesos.')

money = moneyAmount()
cost = appleCost()
apples = amountApple()
change = amountChange()
displayOutput(apples, change)

def getName():
    """ Function for name input """
    nameFunc = input('Enter your Full Name: ')
    return nameFunc

def getAge():
    """ Function for age input """
    ageFunc = input('Enter your Age: ')
    return ageFunc

def getAddress():
    """ Function for address input """
    addressFunc = input('Enter yout Address: ')
    return addressFunc

def displayOutput(nameF, ageF, addressF):
    print(f'Hi, my name is {nameF}. I am {ageF} years old and I live in {addressF}.')

# Steps
# 1. Ask for name and save to a variable
name = getName()
# 2. Ask for age and save to a variable
age = getAge()
# 3. Ask for address and save to a variable
address = getAddress()
# 4. Display name, age, and address
displayOutput(name, age, address)
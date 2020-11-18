import random
from math import *
#Goods (No services) Company Management Game
'''
Run in IDLE

Manage a company

Company Aspects:
    product

    

Product Aspects:
    price
    demand
    num sold since last qtr
    qtrs since prodict change

market:
    fluctuates and regulates demand
    inflate at 2% per yr during normal years
    inflate at 5-10% during years of high infalation
    deflate by 5-30% during recession (crash demand accordingly)

options:
    advertise
    develop
    retire product
    liquidate(end game)
    next qtr
    sim n qtrs
'''


'''
Interface Mockup:

|--------------------------------|
|         Company Name           |
|         ------------           |
| Market:                        | 
|                                |
| Product 1:                     |
|   Price: $XX.XX                |
|   Demand: XX%                  |
|   Num Sold Last QTR: XXXXXX    |
|   QTRs since product change: X |
| ...                            |
|                                |
|--------------------------------|

"Mr CEO, what would you like to do?":
'''


'''
Needed user input to begin game:
    company name
    product name
    product price
'''

###Number Manipulation Functions###
def calculateDemand(price):
    global market, demandMarker
    raw = str((market * demandMarker / (price * 5))/10000)
    raw2 = raw[0:12]
    return float(raw2)        
            

###GUI Functions###
def renderGUI():
    global companyName, spaces40, products, reachStr
    #NEED TO CLEAR SCREEN
    #GUI Screen is 40 char w/o border
    print("|----------------------------------------|")
    numSpaces = (40 - len(companyName))/2
    extra = ''
    if int(numSpaces) < numSpaces:
        extra = ' '
    numSpaces = int(numSpaces)
    spaces = ''
    for i in range(numSpaces):
        spaces += ' '
    print("|" + spaces + companyName + spaces + extra + "|")
    xChars = ''
    for i in range(len(companyName)):
        xChars += '-'
    print('|' + spaces + xChars + spaces + extra + '|')
    print('|' + spaces40 + '|')
    spaces = ''
    for i in range(24-len(reachStr)):
        spaces += ' '
    print('| Company Reach: ' + reachStr + spaces + '|')
    print('|' + spaces40 + '|')
    printProducts()
    numSpaces = 28 - len(productName)
    print
    
def printProducts():
    global products
    counter = 0
    for product in products:
        counter += 1
        spaces = getSpacesByNum( 28 - len(product[4]))
        print("| Product " + str(counter) + ": " + product[4] + spaces + '|')
        itemInfoLen = len(product[0])
        spaces =  getSpacesByNum(29 - itemInfoLen)
        print("|   Price: $" + product[0] + spaces + '|')
        itemInfoLen = len(product[1][:5])
        spaces = getSpacesByNum(28 - itemInfoLen)
        print("|   Demand: " + product[1][:5] + "%" + spaces + '|')
        spaces = getSpacesByNum(18 - len(product[2]))
        print("|   Num Sold Last QTR: " + product[2] + spaces + "|")
        spaces = getSpacesByNum(10 - len(product[3]))
        print("|   QTRs since product change: " + product[3] + spaces + '|\n|' + spaces40 + "|")
    print('|----------------------------------------|')
        

def getSpacesByNum(num):
    spaces = ''
    for i in range(num):
        spaces += ' '
    return spaces


#Game Movement Functions
'''
options:
    advertise
    develop
    retire product
    liquidate(end game)
    next qtr
    sim n qtrs
'''
def advertise(productName):
    global products
    product = ''
    for product_ in products:
        if product_[4] == productName:
            product = product_
            break
    if product == '':
        return False
    manipulationNum = float(random.randint(-2,10))
    product[2] = float(product[2])
    if product[2] < 50: #Current Demand < 50%
        newDemand = product[2] + product[2] * (manipulationNum / 10) #demand + demand * (-20% to 100%)
    else:
        newDemand = product[2] + ((100 - product[2]) * (manipulationNum /10)) #demand + (%ofPopLeft * (-20% to 100%))
    product[2] = str(newDemand)
    for product_ in products:
        if product_[4] == productName:
            product_ = product
            break
    return(manipulationNum)

def develop(productName):
    global products
    success = random.randInt(0,10)
    if success < 7:
        return False
    for product_ in products:
        if product_[4] == productName:
            product_[3] = 0
            return True
    
def retireProduct(productName):
    global products
    for product_ in products:
        if product_[4] == productName:
            products.remove(product_)
            return True
    return False

def liquidate():
    'End Game'

def nextQtr():
    global moneyMade, reach
    numSold = 0
    for product in products:
        numSold = int((float(product[1])/100) * reach)
        moneyMade += numSold * float(product[0])
        p3 = float(product[3])
        product[1] = str(float(product[1]) - abs(((p3 + 1) * (p3 + 1) * (p3 + 1) * (float(product[1]) - 0.001012)/1000)))
        product[2] = str(numSold)
        product[3] = str(float(product[3]) + 1)
        
def simQtrs(n):
    for i in range(n):
        nextQtr()

def changeProductPrice(productName, newPrice):
    global products
    for product_ in products:
        if product_[4] == productName:
            product_[0] = newPrice
            return True
    return False

###Company Setup###
print("Welcome to COMPANY MANAGER, the worlds lowest quality\nASCII buisness-management game.\nTo begin, we need to know a few things about your company...\nWhat is your company's:")
companyName = input("Name: ")
productName = input("First product's name: ")
productPrice = input("First product's price(): $")
try:
    productPrice = float(productPrice)
except:
    aFloat = False
    while not(aFloat):
        print('schlup')
        try:
            productPrice = float(productPrice)
            aFloat = True
        except:
            productPrice = input("Please enter a number: ")


    
###Initial Values###
reach = 3500
reachStr = 'Local'
moneyMade = 0
market = 1
demandMarker = 15
productDemand = calculateDemand(productPrice)
products = [[str(productPrice), str(productDemand),'0','0', productName]]
spaces40 = '                                        '
renderGUI()
while True:
    choice = input("CEO, what would you like to do?:")
    if choice == 'advertise':

        advertise(input("Which product would you like to advertise?"))
    if choice == 'develop':
        develop()
    if choice == 'retire product':
        retireProduct()
    if choice == 'next qtr':
        nextQtr()
    if choice == 'sim qtrs':
        simQtrs(int(input(':')))
    renderGUI()
    print(moneyMade)

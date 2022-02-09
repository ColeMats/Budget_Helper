
category_list = []
class Category:
    def __init__(self, cName = 'None', cPercentage = 0, cTotal = 0): #initiator for a category
        self.cName = cName
        self.cPercentage = cPercentage
        self.cTotal = cTotal

def make_Category(cName = 'None', cPercentage = 0, cTotal = 0): # makes the category
    category = Category(cName, cPercentage, cTotal)
    category_list.append(category)

def add_to_category(category, amount): #adds money to a categroy
    category.cTotal += amount

def withdraw_from_category(category, amount): #subtracts money from a category
    category.cTotal -= amount

def divide_total(total):
    for i in category_list:
        amount = i.cPercentage * total
        add_to_category(i, amount)

def display_category():
    total_balance = 0
    for i in category_list:
        print("Name: " + i.cName)
        print("Percentage: " + str(i.cPercentage))
        print("Total: " + str(i.cTotal) + '\n')
        total_balance += i.cTotal
    print("Total Money: " + str(total_balance))

def design_category(index): #designs the category by asking the user for name, % amount
    cName = input(f"What is the Name of the Category {index + 1}?\n")
    percentage = input(f"What Percentage for Category {cName}?\n")
    make_Category(cName, float(float(percentage)/100))

def start(): #start of app
    print("Welcome to Budget Helper")
    num_cat = input("How many categories would you like?\n")
    for i in range(0, int(num_cat)):
        design_category(i)
    budget_total = input("How much money are you budgetting?\n")
    divide_total(float(budget_total))
    u = input("Would you like to view all categories?")
    if (u == 'y'):
        display_category()
    else:
        print("Goodbye")




start()

def greeter(x = "User"):
    return (f"Hello, {x}! Welcome")

def dollarToRupee(x):
    return (f"Your {x} Dollars are {x*94.25} in Rupees")

def userFullName(first, last):
    first = first.strip().capitalize()
    last = last.strip().capitalize()
    return (f"User's full name is {first} {last}")

def secondCounter(hrs, mins, secs):
    hrstoSec = 3600*hrs
    minstosec = 60*mins
    secs = 1*secs
    totalseconds = hrstoSec+minstosec+secs
    return (f"for the given {hrs},{mins},{secs} total seconds are {totalseconds} ")


def type_inspector():
        user_input = input("Enter something: ")

        try:
            value = int(user_input)
            print("Type: int")
            print("Value:", value)
        except:
            try:
                value = float(user_input)
                print("Type: float")
                print("Value:", value)
            except:
                value = user_input
                print("Type: str")
                print("Value:", value)

def get_tip(bill, percent):
    tip = (percent/100) * bill
    return tip 
def get_total(bill, tip):
    total = bill + tip
    return total 

def getInitials(fullName):
    fullName = fullName.strip().title()
    initials = ".".join(word[0] for word in fullName.split() if word)+ "."
    return initials

def celsiusToFahrenheit(c):
    return (c * 9/5) + 32
def fahrenheitToCelsius(f):
    return (f - 32) * 5/9

def rectangle_stats(length, width):
    Area = length * width
    Perimeter = 2*(length+width)
    diagonal = (length**2 + width**2) ** 0.5
    return (f"""
    Area of the given rectangle with {length} {width} is {Area}sqft, 
    Perimeter of the given rectangle is {Perimeter}ft,
    Diagonal of the given rectangle is {diagonal}ft
    """)

def check_password(pw):

    has_digit = False
    has_upper = False
    for ch in pw:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True

    length = len(pw)

    if length < 6:
        return "At least 6 characters required"
    elif not has_digit or not has_upper:
        return "Weak Password"
    elif length < 10:
        return "Medium Password"
    else:
        return "Strong Password"


def buy(item, money_given):
        menu = {
    "chips": 20,
    "water": 15,
    "chocolate": 30,
    "juice": 25,
    "biscuits": 10
}
        item = item.lower()
        if item not in menu:
            return "Item not available"
        price = menu[item]
        if money_given < price:
            return "insufficient funds"
        else:
            change = money_given - price
            return f"Item purchased {item}! Change: {change}"
        
def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

def class_report():
    n = int(input("Number of Students in class: "))
    scores = []

    for i in range (n):
        s = int(input(f"Enter score of student {i+1}: "))
        scores.append(s)

    print ("\nClass Report")
    for i in range(len(scores)):
        grade = get_grade(scores[i])
        print (f"Student {i+1}: Score = {scores[i]}, Grades = {grade}")  
    class_avg = sum(scores)/len(scores)
    print(f'\nClass average: {class_avg:.2f}')

def main():
    # name = input("Enter user's name ? ")
    # print(greeter(name))

    # dollars = float(input("enter the amount in Dollars: "))
    # print(dollarToRupee(dollars))

    # first = input("Enter your first name: ")
    # last = input("Enter your last name ")
    # print(userFullName(first, last))

    # hr = int(input("Enter number of hrs: "))
    # min = int(input("Enter number of mins: "))
    # sec = int(input("Enter number of secs: "))
    # print (secondCounter(hr,min,sec))

    # type_inspector()

    # bill = int(input("Enter bill amount: "))
    # percent = int(input("Enter tip percentage: "))
    # tips = (get_tip(bill, percent))
    # print("Tips: $", tips)
    # total =  get_total(bill,tips)
    # print("Total: $", total)

    # fullname= input("Enter Your fullname: ")
    # print(getInitials(fullname))
    
    # while(True):
    #     Question = input("What do you want to convert? c/f: ")
    #     if (Question.lower()=="c"):
    #         c= float(input("Enter the temp in Celsius to convert: "))
    #         f = celsiusToFahrenheit(c)
    #         print(f"{f:,.1f}")
    #         break
    #     elif(Question.lower()=="f"):
    #         f= float(input("Enter the temp in Fahrenheit to convert: "))
    #         c = fahrenheitToCelsius(f)
    #         print(f"{c:,.1f}")
    #         break
    #     else:
    #         print("Wrong choice choose again")

    # length = int (input("Enter length of the rectangle? "))
    # width = int (input("Enter width of the rectangle? "))
    # print(rectangle_stats(length, width))

    # pw = input("Enter the Password: ")
    # print(check_password(pw))

    # item = input("Enter item name: ")
    # money_given = int(input("Enter given money: "))
    # print(buy(item,money_given))

    # class_report()

if __name__ == "__main__":
    main()

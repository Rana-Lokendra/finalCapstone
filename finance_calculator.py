import math

print("investment - to calculate the amount of the interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
cal = str(input("Enter either 'investment' or 'bond' from the menu above to proceed : ")).lower()

# conditional statement

if cal == "investment":

    print(("choose below : \n Simple \n Compound"))
    choose_investment = input("Choose : ").lower()
    if choose_investment == "simple":
        print("1 . The amount of money you are depositing : ")
        P = (int(input("P = ")))
        print("Enter the interest rate : ")
        R = (int(input("r = ")))
        R = R / 100
        print("number of years that the money is being invested.")
        T = (int(input("T = ")))
        print("The total amount once the interest has been applies.")
        A = P * (1 + R * T)  # calculating the overall input
        print("Your interest rate is : ", A)

    elif choose_investment == "compound":
        print("1 . The amount of money you are depositing : ")
        P = (int(input("P = ")))
        print("Enter the interest rate : ")
        R = (int(input("r = ")))
        R = R / 100
        print("number of years that the money is being invested.")
        T = (int(input("T = ")))
        print("The total amount once the interest has been applies.")
        A = P * math.pow((1 + R), T)
        print("Your compound interest is : ", A)

    else:
        print("Try again")









# Bond conditional statements
print("Enter the amount to get the bond")
if (cal == "bond"):
    print("1.The present value of the house")
    P = int(input("P - "))
    print("The interest rate : ")
    I = int(input("I = "))/100/12
    print("The number of months they plan to take to repay the bond")
    N = int(input("N : "))

    repayment = (I * P) / (1 - (1 + I) ** (-N))
    print("This is the total amount", repayment)


else:
    print("Incorrect, redo again")











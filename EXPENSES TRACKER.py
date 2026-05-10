#expenses tracker
expenseslist=[ ]    #list of all expenses in form of dictionary
print("Welcome to Expenses Tracker:")

while True:
    print("====MENU====")
    print("1. Add Expenses")
    print("2. View all Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice=int(input("Please enter your choice:-"))

    #Add expenses
    if(choice==1):
        date=input("enter the date of expenses?: ")
        category=input("enter what type of spending habe you done?(food,transport,makeup,books,dress,others)")
        description=input("enter the details of expenses?:")
        amount=float(input("enter the amount of expenses?:"))

        expenses={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenseslist.append(expenses)
        print("\n DONE!...Expenses added sucessfully")

    #view all expenses
    elif(choice==2):
        if(len(expenses)==0):
            print("\n No Expenses added our recorded!")
        else:
            print("\n See your all Expenses:")
            count=1
            for each_expenses in expenses:
                print(f"expenses no.{count}-->")   
                print(f" Date: {each_expenses['date']}")
                print(f" Category: {each_expenses['category']}")
                print(f" Description: {each_expenses['description']}")
                print(f" Amount: {each_expenses['amount']}")
                count=count+1
    #view total expense
    elif(choice==3):
        total=0
        for each_expenses in expenses:  
            total=total+each_expenses["amount"]
        print(f"Total Expenses = {total}")

    #exit
    elif(choice==4):
        print("THANK YOU FOR USING ALL EXPENSES TRACKER!")
        break
    else:
        print("INVALID CHOICE.  Try again!!")


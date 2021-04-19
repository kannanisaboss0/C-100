                        #---------------------------------------------------ATMCard.py-----------------------------------------------------------#
#Importing two modules:Random and Datetime
import random
import datetime
import requests


#Declaring inputs and variables
ATMCardNumber=int(input("Enter ATM Card Number:"))
ATMCardPin=int(input("Enter ATM Card Pin:"))
TotalMoney=random.randint(0,10000000)
print("Current total amount is "+str(TotalMoney)+".")
date=datetime.datetime.now()


#Defining A Class ATM
class ATM (object):
    def __init__(self,ATMNumber,ATMPin,TotalMoney):
        self.self=self
        self.ATMNumber=ATMNumber
        self.ATMPin=ATMPin
        self.TotalMoney=TotalMoney

        #Function 1
    def WithdrawMoney(self):
        print("Current total amount is "+str(TotalMoney)+".")
        withdrawAmount=int(input("Enter the amount to withdraw:"))
        if(withdrawAmount<self.TotalMoney):      
            print(str(withdrawAmount)+" withdrawn from the total amount of "+str(TotalMoney)+" at "+str(date)+".")
            print("The account now has "+str(self.TotalMoney-withdrawAmount)+" left.")
            print("Thank you for using ATMCard.py.")
            print("Have A Nice Day.")
        elif(withdrawAmount==TotalMoney):
            choice=input("By withdrawing the specified amount, the total money in the account  would amount to 0. Continue to withdraw? ")
            if(choice=="Yes" or choice=="yes"):
                self.TotalMoney=self.TotalMoney-withdrawAmount
                print("Amount withdrawn. The account's present value is now 0.")
                print("Thank you for using ATMCard.py.")
                print("Have A Nice Day.")
            else:
                print("Withdraw request terminated.")  
                print("Thank you for using ATMCard.py.")
                print("Have A Nice Day.")
        elif(withdrawAmount>TotalMoney):
            print("Withdraw request terminated.")
            print("Amount requested for withdrawal exceeds the total amount held by the current account")  
            print("Thank you for using ATMCard.py.")  
            print("Have A Nice Day.")

        #Function 2
    def DepositMoney(self):
        print("Current total amount is "+str(TotalMoney)+".")
        depositAmount=int(input("Enter the amount to deposit:"))
        if(depositAmount<=0):
            print("Deposit request terminated.")
            print("The value specified is invalid.")
            print("The specified value should be a natural number (Eg. 1,2,3,4....n)")
        else:
            print(str(depositAmount)+" deposited to the total amount of "+str(TotalMoney)+"at "+str(date)+".")
            print("The account now has  "+str(self.TotalMoney+depositAmount)+" credited to it.")
            print("Thank you for using ATMCard.py.")
            print("Have A Nice Day.")

        #Function 3
    def CreateUniqueOneTimeIDWithCardNumberAndPin(self):
        id_string=random.randint(10000000,100000000000)
        random_id=bin(id_string*self.ATMNumber*self.ATMPin)
        print("The unique ID is "+str(random_id))

        #Function 4
    def ConvertCurrency(self):
        url='http://data.fixer.io/api/latest?access_key=8a18e12c1f4eb92f062ceb0e00fa121f'
        data=requests.get(url).json()
        print("Please type the following in UPPERCASE.")
        initial_currency=input("Enter the initial currency:")
        final_currency=input("Enter the final Currency")
        amount=int(input("Enter the amount to be converted:"))
        rate=data["rates"]
        initial_amount=amount
        if (initial_currency!='EUR'):
            amount=amount/rate[initial_currency]
        final_amount=round(amount*rate[final_currency],2)
        print(str(initial_amount)+" in "+str(initial_currency)+" = "+str(final_amount)+" in "+final_currency)
        print("Thank you for using ATMCard.py.")
        print("Have A Nice Day.")


                
     
#Verifying the credibility of the ATMCardNubmer and ATMCardPin             
if(1000<ATMCardNumber<100000000 and 1000<ATMCardPin<10000000000 ):

    #Declaring object User with class as ATM
    User=ATM(ATMCardNumber,ATMCardPin,TotalMoney)

    #Listing the various functions available
    print("Welcome to ATMCard.py")
    print("Given below are list of actions possible to do here:")
    print("1. Withdrawal From Account")
    print("2. Deposition To Account")
    print("3. Create Unique One-Time-Use Card ID Based On Account")
    print("4. Currency Conversion")

    #Providing functions to user's discretion
    action_index=int(input("Type the index of the desired action here:"))

#Listing all cases. Is there a switch function in Python?
    #Case 1 
    if(action_index==1):
        print("Withdrawing Money")
        User.WithdrawMoney()

    #Case 2    
    elif(action_index==2):
        print("Depositing Money")
        User.DepositMoney()

    #Case 3    
    elif(action_index==3):
        print("Calculating Unique ID")
        User.CreateUniqueOneTimeIDWithCardNumberAndPin()    

    #Case 4     
    elif(action_index==4):
        print("Coverting Currency")
        User.ConvertCurrency()   

    #Case 5
    else:
        print("Please enter a valid index.")         
#End of cases

else:
    print("Access request terminated.")
    print("A credential is invalid. Please check")
                        #---------------------------------------------------ATMCard.py-----------------------------------------------------------#




     



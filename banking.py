# =============================================================================
# 1) Write documentation for class
# 2) Create a menu driven netbanking application where user can 
# 
#     a) Register/Create account
# 
#     b) Check balance 
# 
#     c) Transfer balance
# 
# =============================================================================
import datetime as dt
class NetBanking:
    """
    This Program is Created For Following:
    a) Register/Create account
    b) Check balance 
    c) Transfer balance
      
    """
        
    def __init__(self):
        print('''
        * OPTIONS AVAILABLE * 
            1. Register/Create account
            2. Check Balance 
            3. Transfer balance
            4. Read Documentation
            5. EXIT
            ''')
        choice=int(input("Enter choice="))
        
        if(choice==1):
            NetBanking.account_new(self)
        elif(choice==2):
            NetBanking.show_balance(self)            
        elif(choice==3):
            NetBanking.Withdraw_amount(self)
        elif(choice==4):
            NetBanking.Documentation(self)
        elif(choice==5):
            pass
        else:
            print("Invalid choice, Try Again !!")
            NetBanking.__init__(self)
        
        
    def min_balnce(self):
        if self.__accType == "S":
            print("Minimum Saving Account Balance Should Be Rs. 1000")
        else:
            print("Minimum Current Account Balance Should Be Rs. 5000")
                           
           
    def account_new(self):
        self.__custName = input("Enter Name=")
        self.__acc_no = int(input("Enter Account No="))
        self.__dob = input("Enter Date Of Birth=")
        accType_flag=False
        while(accType_flag==False):
            self.__accType = str(input("Enter Account Type(S/C): "))
            if self.__accType == "S" or self.__accType =="C":
                accType_flag=True
            else:
                print("Enter account type as S=Savings / C=Current")
                accType_flag=False

        accType_min_balnce_flag=False
        while(accType_min_balnce_flag==False):
            if self.__accType == "S":
                self.__savingBal = int(input("Savings Account Opening Balance="))
                self.__currentBal=0
            else:
                self.__currentBal = int(input("Current Account Opening Balance="))
                self.__savingBal=0
        
            if((self.__accType == "S" and self.__savingBal<1000) or (self.__accType == "C" and self.__currentBal<5000)):
                NetBanking.min_balnce(self)
            else:
                accType_min_balnce_flag=True
                
        print("Account Created !!!")
        NetBanking.__init__(self)
    
                    
  
    def show_balance(self):
        if self.__accType == "S":
            print("Savings Account Balance: ",self.__savingBal)
        else:
            print("Current Account Balance: ",self.__currentBal)    
       

    def Withdraw_amount(self):
        withdraw_amt=int(input("Enter withdraw amount="))
        if((withdraw_amt>self.__savingBal and self.__accType == "S") or (withdraw_amt>self.__currentBal and self.__accType == "C")):
            print("Insufficient Fund, Try Again !!!")
            NetBanking.show_balance(self)
            try_withdraw=input("Do You Want To Try Again (Y/N):").upper()
            if try_withdraw=="Y":
                NetBanking.Withdraw_amount(self)
            else:
                pass
        elif(self.__accType == "S" and withdraw_amt<=self.__savingBal):
            self.__savingBal = self.__savingBal - withdraw_amt
            NetBanking.show_balance(self)
        elif(self.__accType == "C" and withdraw_amt<=self.__currentBal):
            self.__currentBal = self.__currentBal - withdraw_amt
            NetBanking.show_balance(self)
        else:
            print("Invalid Input, Try Again !!")
            NetBanking.Withdraw_amount(self)
    

    def Documentation(self):
        print("\t\t\t  == DOCUMENTATION  == ")
        print(NetBanking.__doc__)
        NetBanking.__init__(self)
        

nb=NetBanking()


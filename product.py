class purchase:
    
    def __init__(self):

        self.com_name = " "
        self.product_name = " "
        #customer_name = " "
    
    def input_company(self):
        
        print('')
        print('''MENU:-PLEASE SELECT THE COMPANY 
        1)AGAPPE
        2)BIOMEURIEX
        3)ARKRAY
        4)NIHON KOHDEN
        5)BIOLAB''')
        self.com_name=input()
        #print(self.com_name)

    def input_product(self):
        
        if(self.com_name == "1"):
            print('')
            print('''MENU:-
            1)BIO-CHEMISTRY
            2)CELL-COUNTER
            3)MISPA NANO
            4)MISPA NEO
            ''')
        
        elif(self.com_name == "2"):
            print('')
            print('''MENU:-
            1)MINI VIDAS
            2)VIDAS
            ''')

        elif(self.com_name == "3"):
            print('')
            print('''MENU:-
            1)PPD 10TU
            2)PPD 2TU
            3)PPD 5TU
            ''')     

        elif(self.com_name == "4"):
            print('')
            print('''MENU:-
            1)CELL COUNTER 3
            2)CELL COUNTER 5
            3)REAGENTS
            ''')      
        else:
            print('')
            print('''MENU:-
            1)GIMSA STAIN
            2)RAPID PAP
            3)LIQUID SOLUTION
            ''')  
        self.product_name=input()        

class sales:
    
    def __init__(self):
        self.com_name = " "
        self.product_name = " "
        self.customer_name = " "
    
    def input_company(self):
        
        print('''MENU:-PLEASE SELECT THE COMPANY 
        1)AGAPPE
        2)BIOMEURIEX
        3)ARKRAY
        4)NIHON KOHDEN
        5)BIOLAB''')
        self.com_name = input()
        #print(self.com_name)

    def input_product(self):
        
        if(self.com_name == "1"):
            print('')
            print('''MENU:-
            1)BIO-CHEMISTRY
            2)CELL-COUNTER
            3)MISPA NANO
            4)MISPA NEO
            ''')
        
        elif(self.com_name == "2"):
            print('')
            print('''MENU:-
            1)MINI VIDAS
            2)VIDAS
            ''')

        elif(self.com_name == "3"):
            print('')
            print('''MENU:-
            1)PPD 10TU
            2)PPD 2TU
            3)PPD 5TU
            ''')     

        elif(self.com_name == "4"):
            print('')
            print('''MENU:-
            1)CELL COUNTER 3
            2)CELL COUNTER 5
            3)REAGENTS
            ''')      
        
        else:
            print('')
            print('''MENU:-
            1)GIMSA STAIN
            2)RAPID PAP
            3)LIQUID SOLUTION
            ''')  
        self.product_name = input()        
        
    def input_customer(self):
        print("\nPLEASE ENTER THE CUSTOMER NAME")
        self.customer_name = input()

           
#if"name"=="main":
print('\n**********Displaying the Company and their Products**********')
print('->>>Enter Number of Company<<<-')
purchase().input_company()
print('->>>Enter Number of Product<<<-')
purchase().input_product()
#comobj.input_customer()
print('\nWhat you want to buy ?')

sales().input_company()
sales().input_product()
sales().input_customer()
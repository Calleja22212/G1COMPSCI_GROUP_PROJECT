TOTAL_PRICE=0
CAMPUS=["CBZRC", "IRC", "WVC","CLC",
          "CVC", "CMC", "MC","ZRC",
          "EVC", "CVISC", "DRC", "MRC",
          "BRC", "ZPRC", "NMC", "SRC", "CARC"]#Campus abbreviations
RICEPRICE={"Whole": 50, "Half":25, "None":0}#Rice prices
MAINSPRICE={"Seafood":40, "Beef":35,
             "Vegetables":35, "Pork":25, "Chicken":30}#Main prices
SHAKE_FLAVORS=["Banana","Straberry","Blueberry","Muscat grape",
            "Red grapes","Dragon fruit","Mango","Watermelon"
            "Buko", "Guyabano","Apple", "Lychee",
            "Pineapple"]#Shake flavors
DAIRY=["Milo", "Milk", "Yakult"]
JUICE_FLAVORS=['Pink lemonade', 'Blue lemonade', 'Iced tea', 'Cucumber', 'C2', 'Mogu mogu', 'Pineapple'
            'Apple', 'Buko', 'Lemonade', 'Orange', 'Blueberry', 'Strawberry', 'Lemon', ]#Juice options
MAIN=[]
RICE=[]
DRINK=[]

counter = 2

def address(email_name, abr):
        return f"{email_name}@{abr.lower()}.pshs.edu.ph"





print("""
===FOODIFYE | E-COMMERCE CANTEEN===""")

pick = str(input("""
                 
Welcome, dear user!

Sign-in? (Yes/No): """)).title()
while pick not in ["Yes", "No"]:                
    print("""
---Invalid choice, kindly try again---""")                
    pick = str(input("""
                     
Welcome, dear user!

Sign-in? (Yes/No): """)).title() # Corrected method
if pick == "Yes":
    print("""
---Proceed with the following instructions---
""")




   #SIGNING IN SEGMENT#
    while True:
        try:
            name=str(input("Enter your email name (Ex. jcdeguzman): "))
            campus=str(input(f"Enter your campus abbreviation (Ex. CBZRC): ")).upper()
            while campus not in CAMPUS:
                print("""
---Campus address not found, kindly try again---
""")
                campus=str(input(f"Enter your campus abbreviation: ")).upper()#Error handling no.1 for campus address
            psswrd=str(input("""
Enter your password: """))
            print("""
---Password integrated to log-in---
""")
            email=address(name, campus)
            print(f"""Welcome, {email}!

---        
""")
            break
            #END OF SEGMENT#
        except ValueError:
            print(f"""
---Error in values entered, kindly try again---
""")




    #HANDLING AND MODE OF RECEIVE SEGMENT#
    while True:
         try:
            choice=input("Order OR Pre-Order? (If 'Pre-Order, please enter 'preorder'): ").title()
            while choice not in ["Order","Pre order", "Preorder"]:#Error handling no.2 for order handling
                print("""
---Invalid option, kindly try again---
""")
                choice=input("Order OR PreOrder?: ").title()

            mode=input("Takeout OR Dine-in? (If 'Dine-in', please enter 'dinein'): ").title()
            while mode not in ["Take-out", "Takeout", "Take out", "Dinein"]:
                print("""
---Invalid option, kindly try again---
""")
                mode=input("Takeout OR Dinein?: ").title()
            break

    #END OF SEGMENT#
         except ValueError:
             print(f"""---Error in values entered
, kindly try again---""")
             




    #ORDERING SEGMENT#
    while True:
        try:
            if mode=="Dinein":#Plate section for dining-in
                print("""                   
---You have a limit of three plates---
""")
                plate_counter=int(input("How many plates?: "))
                while plate_counter>3 or plate_counter<0:
                    if plate_counter>3:
                        print("""
---Maximum of 3 plates, kindly insert another input---
""")
                        plate_counter=int(input("How many plates?: "))
                    else:
                        print("""
---Invalid input, kindly try again---
""")
                        plate_counter=int(input("How many plates?: "))
                break
            else:#Takout section for boxes
                print("""
---You have a limit of three boxes---
""")
                box_counter=int(input("How many boxes? (Do not input negative integers): "))
                match box_counter:
                    case _ if box_counter>3:
                        while box_counter>3:
                            print("""
---Maximum of 3 boxes, kindly insert another input---
""")
                            box_counter=int(input("How many boxes? (Do not input negative integers): "))
                    case _ if box_counter<0:
                        while box_counter<0:
                            print("""
    ---Invalid input, kindly try again---
""")
                            box_counter=int(input("How many boxes?: "))
                break
        except ValueError:
            print(f"""
---Error in values entered, kindly try again---""")



while True:
        try:
            print("""
---
""")
            rice_response=str(input("Would you like some rice? (Yes/No): ")).title()
            while rice_response!="Yes" and rice_response!="No":#Error handling
                      print("""
---Kindly try again---
""")
                      rice_response=str(input("Would you like some rice? (Yes/No): ")).title()

            if rice_response=="Yes":
                 r=counter
                 for i in range(0, r):
                          rice_pick=str(input("Choose either Whole, Half, or None for rice (Enter twice): ")).title()
                          while rice_pick not in ["Whole", "Half", "None"]:
                                print("""
---Choice does not exist, kindly try again---
""")
                                rice_pick=str(input("Choose either Whole, Half, or None for rice: ")).title()
                                continue
                          TOTAL_PRICE = RICEPRICE[rice_pick]+TOTAL_PRICE
            c=2*counter#Display choices remaining, dependant on no. of plates ordered

            for i in range(0,c):
                 print(f"""
---Enter your main dishes. You have {c} options left. Enter 0 to for none---
( Seafood = 40 / Beef = 35 / Vegetables = 35 / Pork = 25 / Chicken = 30 )
""")
                 main_dish=str(input("Enter a Main dish or dishes to go: ")).title()

                 if main_dish=='0':
                           break
                 
                 while main_dish not in ["Chicken","Pork","Beef","Vegetables","Seafood"]:
                           print("""
---Choice does not exist, kindly try again---
""")
                           main_dish=str(input("Enter a Main dish to go: ")).title()
                           
                 TOTAL_PRICE=TOTAL_PRICE+MAINSPRICE[main_dish]
                 MAIN.append(main_dish) 
                 c-=1

            break
#END OF SEGMENT#
        except ValueError:
            print(f"""
---Error in values entered, kindly try again---
""")
            


while True:
     try:
            print("""
---
""")
            drink_response=input("Would you like drinks (Yes/No)?: ").title()
            while drink_response not in ["Yes", "No"]:
                 print("""
---Choice does not exist, kindly try again---
""")
                 drink_response = input("Would you like drinks (Yes/No)?: ").title()
                    
            if drink_response=="Yes":
                      print("""
---Limit of 10 drinks---
""")
                      drink_counter = int(input("How many drinks do you want?: "))
                      while drink_counter < 0 or drink_counter > 10:
                                print("Kindly try again")
                                print("""
---Maximum of 10 drinks, minimum of 0---""")
                                drink_counter=int(input("How many do you want?: ")).title()
                      
                                
                      print(f"""
---DRINKS---

AVAILBLE JUICES:
{JUICE_FLAVORS}
""")
                      print(f"""AVAILBLE SHAKES:
{SHAKE_FLAVORS}
""")
                      print(f"""AVAILABLE DAIRY:
{DAIRY}""")
                      e = drink_counter
                      for i in range(0,e):
                           print(f"""
---Enter some drinks to go. You have {e} choice/s left. Enter 0 to exit---
""")
                           drink=str(input("Would you like a Shake, Juice, or Dairy?: ")).title()
                           while drink not in ["Shake","Juice","Dairy", "0"]:
                                     print("""
---Kindly try again
""")
                                     drink=str(input("Would you like a Shake, Juice, or Dairy?: ")).title()
                         
                           if drink=="0":
                                     break
                           
                           elif drink=="Shake":
                                     TOTAL_PRICE=TOTAL_PRICE+20
                                     drink_pick=input(f"""
---Look at the choices above---
                                                          
Chosen shake type: """).title()
                                     while drink_pick not in SHAKE_FLAVORS: 
                                        ("""
---Option not found, kindly try again---
""")
                                        drink_pick=input(f"""
---Look at the choices above---
                                                          
Chosen shake type: """).title()

                           elif drink=="Juice":
                                      TOTAL_PRICE=TOTAL_PRICE+25
                                      drink_pick=str(input(f"""
---Look at the choices above---
                                                          
Chosen juice type: """)).title()
                                      while drink_pick not in JUICE_FLAVORS:
                                                print("""
---Option not found, kindly try again---
""")
                                                drink_pick=str(input(f"""
---Look at the choices above---
                                                          
Chosen juice type: """)).title()
                           else:
                                      TOTAL_PRICE=TOTAL_PRICE+27
                                      drink_pick=str(input(f"""
---Look at the choices above---
                                                          
Chosen dairy type: """)).title()
                                      while drink_pick not in DAIRY:
                                                print("""
---Option not found, kindly try again---
""")
                                                drink_pick=str(input(f"""
---Look at the choices above---
                                                          
Chosen dairy type: """)).title()                        
                           DRINK.append(drink_pick)
                           e = 1                        

            break
     except ValueError:
             print(f"""
---Invalid input. Try again---
""")
                             
#END OF SEGMENT#



#OUTPUT SEGMENT#
print("""---

      
===FINAL RECEIPT===
""")
print(f"""EMAIL: {email}
CHOICE: {choice}
PLATES/BOXES ORDERED: {counter}""")
if rice_response == "No":
      print(f"RICE: NONE")
else:
     print(f"RICE: {rice_pick} rice")
print(f"MAIN: {MAIN}")
print(f"NO. OF DRINKS ORDERED: {drink_counter}")

if drink_response == "No":
       print(f"DRINK/S: NONE")
else:
     print(f"DRINK/S: {drink_pick}")
     
print(f"TOTAL PRICE: ₱{TOTAL_PRICE}")


print("""
      
===THANK YOU FOR USING FOODIFYE FOR YOUR PURCHASES====
      
===GOODBYE FELLOW CUSROMER!!===

""")

input("Press anything to exit...")
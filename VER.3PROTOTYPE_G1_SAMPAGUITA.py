TOTAL_PRICE=0
CAMPUS=["CBZRC", "IRC", "WVC","CLC",
          "CVC", "CMC", "MC","ZRC",
          "EVC", "CVISC", "DRC", "MRC",
          "BRC", "ZPRC", "NMC", "SRC", "CARC"]#Campus abbreviations
RICECEPRICE={"Whole":50, "Half":25, "None":0}#Rice prices
MAINSPRICE={"Seafood":40, "Beef":35,
             "Vegetables":35, "Pork":25, "Chicken":30}#Main prices
SHAKE_FLAVORS=["Banana","Straberry","Blueberry","Muscat grape",
            "Red grapes","Dragon fruit","Mango","Watermelon"
            "Buko", "Guyabano","Apple", "Lychee",
            "Pineapple"]#Shake flavors
JUICE_FLAVORS=['Pink lemonade', 'Blue lemonade', 'Iced tea', 'Cucumber lemonade', 'C2', 'Mogu mogu', 'Pineapple'
            'Apple', 'Buko juice', 'Lemonade', 'Orange']#Juice options
MAIN=[]
SIDE=[]
def address(email_name, abr):
        return f"{email_name}@{abr.lower()}.pshs.edu.ph"

pick=str(input("Welcome, dear user. Would you sign in for ordering at the canteen (Yes/No)?")).title()
while pick not in ["Yes", "No"]:
    print("Invalid choice, kindly try again")
    pick=str(input("Dear user, would you sign in for ordering at the canteen?")).upper()
if pick=="Yes":
    print("Proceed with the following instructions")



   #SIGNING IN SEGMENT#
    while True:
        try:
            name=str(input("Enter your email name (Ex. jcdeguzman):"))
            campus=str(input(f"""Enter your campus abbreviation (Ex. CBZRC):""")).upper()
            while campus not in CAMPUS:
                print("Campus address not found, kindly try again")
                campus=str(input(f"""Enter your campus abbreviation:"""))#Error handling no.1 for campus address
            psswrd=str(input("Enter your password:"))
            print("Password integrated to log-in")
            email=address(name, campus)
            print(f"Welcome,{email}")
            break
            #END OF SEGMENT#
        except ValueError:
            print(f"""Error in values entered
, kindly try again""")




    #HANDLING AND MODE OF RECEIVE SEGMENT#
    while True:
         try:
            choice=str(input("Order or Pre-order:")).title()
            while choice not in ["Order","Pre order", "Pre-order", "Preorder"]:#Error handling no.2 for order handling
                print("Invalid option, kindly try again.")
                choice=str(input("Order or Pre-order:")).title()
            mode=str(input("Takeout or Dine-in?")).title()
            while mode not in ["Take-out", "Takeout", "Take out", "Dine-in"]:
                print("Invalid option, kindly try again.")
                mode=str(input("Takeout or Dine-in?")).title()
            break
    #END OF SEGMENT#
         except ValueError:
             print(f"""Error in values entered
, kindly try again""")




    #ORDERING SEGMENT#
    while True:
        try:
            if mode=="Dine-in":#Plate section for dining-in
                print("You have a limit of three plates.")
                counter=int(input("How many plates?"))
                while counter>3 or plate_counter<0:
                    if counter>3:
                        print("Over limit, kindly try again.")
                        counter=int(input("How many plates?"))
                    else:
                        print("Invalid input, kindly try again.")
                        counter=int(input("How many plates?"))
                break
            else:#Takout section for boxes
                print("You have a limit of three boxes.")
                box_counter=int(input("How many boxes?"))
                match box_counter:
                    case _ if counter>3:
                        while counter>3:
                            print("Over limit, kindly try again.")
                            counter=int(input("How many boxes?"))
                    case _ if box_counter<0:
                        while box_counter<0:
                            print("Invalid input, kindly try again.")
                            box_counter=int(input("How many boxes?"))
#END OF SEGMENT#
                break
        except ValueError:
            print(f"""Error in values entered, kindly try again""")
 #RICE AND MAINS SEGMENT#
 while True:
     try:
          rice_pick=str(input("Whole, Half, or None for rice")).title()
          while rice_pick not in ["Whole", "Half", "None"]:
                 print("Choice does not exist, kindly try again.")
                 rice_pick=str(input("Whole, Half, or None for rice")).title()
          TOTAL_PRICE=RICEPRICE[rice_pick]*counter   
          c=2*counter#Display choices remaining
          for i in range(0,c):
                 print(f"You have {c} options left, enter 0 to exit")
                 main_dish=str(input("Enter a main dish to go with your rice:")).title()
                 print(MAINSPRICE)
                 if main_dish=='0':
                           break
                 while main_dish not in ["Chicken","Pork","Beef","Vegetables","Seafood"]:
                           print("Choice does not exist, kindly try again")
                           main_dish=str(input("Enter a main dish to go with your rice:")).title()
                 TOTAL_PRICE=TOTAL_PRICE+MAINSPRICE[main_dish]
                 MAIN.append()
                 c-=1
          break
#END OF SEGMENT#
     except ValueError:
            print(f"""Error in values entered, kindly try again""")
print("===THANK YOU FOR YOUR COOPERATION====")

          

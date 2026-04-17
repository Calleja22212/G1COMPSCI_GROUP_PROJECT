camp_abb={"cbzrc", "irc", "wvc","clc",
          "cvc", "cmc", "mc","zrc",
          "evc", "cvisc", "drc", "mrc",
          "brc", "zprc", "nmc", "src", "carc"}#Campus abbreviations
price_rice={"Whole":50, "Half":25, "None":0}#Rice prices
price_mains={"Seafood":40, "Beef":30,
             "Vegetables":35, "Pork":37, "Chicken":29}#Main prices
mains={"Seafood", "Beef", "Vegetables", "Pork", "Chicken"}#SIde choices
shake_flav={"Banana","Straberry","Blueberry","Muscat grape",
            "Red grapes","Dragon fruit","Mango","Watermelon"
            "Buko", "Guyabano","Apple", "Lychee",
            "Pineapple"}#Shake flavors
juice_flav={'Pink lemonade', 'Blue lemonade', 'Iced tea', 'Cucumber lemonade', 'C2', 'Mogu mogu', 'Pineapple'
            'Apple', 'Buko juice'}#Juice options
side=[]
while True:
    try:#Error return and handling
        name=str(input(f"""Enter the first half
of your email address (Ex.jcdeguzman):"""))
        print(camp_abb)
        campus=str(input(f"""Enter your campus abbreviation:""")).lower()
        while campus not in camp_abb:#Error handle #1 campus value
            campus=str(input(f"""Try again for this does not exist:""")).lower()
        passwrd=str(input("Enter your password:"))
        email=name+"@"+campus+".pshs.edu.ph"
        print(f"Welcome, user {email}")
        print("Enter a choice")
        action=str(input("Order or Leave:")).title()#Action choice and input
        while  action !="Order" and action!="Leave":#Error handle #2 opt value
            print("Try again")
            action=str(input("Order or Leave:")).title()
        print(f"You chose to {action}")
        break
    except ValueError:
        print("Error in values")
while True:
    try:#Error return and handling
        if action=="Order":
            choice=str(input("Would you order or pre-order:")).lower()#pre-order or order choice and input
            while choice not in ["order","pre order", "pre-order", "preorder"]:
                print("Try again")
                choice=str(input("Would you order or pre-order:")).lower()#order or pre-order choice input
            direct=str(input("Takeout or Dine-In:"))
            while direct not in ["take-out", "takeout","Take-out", "Takeout", "Take out", "Dine In", "Dine-In"]:#Error handle#3 direct value
                print("Try again")
                direct=str(input("Takeout or Dine-In:"))
            print("Whole, Half, or None?")
            ricepick=str(input("Enter rice order:")).title()
            while ricepick not in ["Whole", "Half" ,"None"]:#Error handle#4 ricepic value
                print("Try again. Whole, Half, or None?")
                ricepick=str(input("Enter rice order:")).title()
            total_price=price_rice[ricepick]
            c=2
            for i in range(0,2):
                print(f"You have {c} options left")
                print("Enter 0 to exit")
                print(mains)
                dish=str(input("Enter a main dish to go with your rice:")).title()
                if dish=="0":
                    break
                while dish not in mains:#Error handle#5 dish c=value
                    dish=str(input("Doesn't exist in the menu, try again")).title()
                total_price=price_mains[dish]+total_price
                side.append(dish)#Add to list of items in side
                c-=1
            break
        else:
            print(f"Thank you for your cooperation, {email}")
            break
    except ValueError:
        print("Error in values")
        break
while True:
    try: #Error return and handling
        response=str(input("Would you like a drink (Y/N):")).title()#Drink options evaluation
        while response!="Y" and response!="N":
                response=str(input("Try again? Y/N:")).title()
        if response=="Y":
            drink=str(input("Which one, Juice or Shake:")).title()#Choices displayed for drinks
            while drink!="Juice" and drink!="Shake":#Error handling for drink value
                print("Invalid option")
                drink=str(input("Which one, Juice or Shake:")).title()
            if drink=="Shake":#Route for shake
                print(shake_flav)
                shake_order=str(input("Enter a shake flavor:")).title()
                while shake_order not in shake_flav:
                    shake_order=str(input("That doesn't exist, try again:")).title()
                total_price=total_price+25
            else:#Route for juice
                print(juice_flav)
                juice_order=str(input("Enter a shake flavor:")).title()
                while juice_order not in juice_flav:#Error handling for juice selection
                    juice_order=str(input("That doesn't exist, try again:")).title()
                total_price=total_price+20
        break
    except ValueError:
        print("Error in values")
while True:
    try:#Error return and handling
        pay=str(input("Cash or Card?")).title()
        while pay!="Cash" and pay!="Card":
            pay=str(input("Try again, Cash or Online?")).title()
        break 
    except ValueError:
        print("Error in values")

        
        

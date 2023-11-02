from CoffeeMachine_data import MENU, resources

Machine_is_ON = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = [0]


# resourcesList = [resources["water"], resources["milk"], resources["coffee"]]

def report(water, milk, coffee , money):    
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money[0]}\n")
    
    # print(f"Water: {water}\n",f"Milk: {milk}\n",f"Coffee: {coffee}\n",f"Money: {money}\n")
    # print(f"\n{water}\n{milk}\n{coffee}\n{money}\n")


    
def coinsCounter(drinkPrice, money, drink_input ):
    print("Please insert coins.")
    
    quarters = int(input("\nhow many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))
    
    total_user_cash = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    
    if total_user_cash < drinkPrice:
        print("\nSorry that's not enough money. Money refunded.")
    else:
        if total_user_cash - drinkPrice > 0:
            print(f"\nHere is ${float(total_user_cash - drinkPrice)} in change.")
            
        print(f"\nHere is your {drink_input} ☕️. Enjoy!\n")
        money[0] += drinkPrice
    
    
while(Machine_is_ON):
    print("""
          
    -> Welcome to THE MODERN CAFFEE MAHCINE ☕☕
          
        Options:
            refill: will refill the Coffee Machine with given resources.
            off: will turn the Coffee Machine off.
            report: will print you a report with all available resources and Cash Amount.
            espresso/latte/cappuccino: are products that you can purchase.
        
        Pricing List:
            espresso: $1.5 
            latte: $2.5
            cappuccino: $3.0
          
          """)    
    user_select =  input("What would you like? (espresso/latte/cappuccino): ").lower()
    # while (user_select != "espresso" or user_select != "latte" or user_select != "cappuccino" or user_select != "report" or user_select != "off"):
    #     user_select =  input("Enter Again a valid option - What would you like? (espresso/latte/cappuccino): ")

    if user_select == "report":
        report(water, milk, coffee , money)
    
    elif user_select == "espresso" or user_select == "latte" or user_select == "cappuccino":
        drink_price = MENU[user_select]["cost"]
        coinsCounter(drink_price, money, user_select) 
        water = water - MENU[user_select]["ingredients"]["water"]
        milk = milk - MENU[user_select]["ingredients"]["milk"]
        coffee = milk - MENU[user_select]["ingredients"]["coffee"]
    
    elif user_select == "refill":
        water_refill = int(input("How much water you want to add in ml: "))
        milk_refill = int(input("How much milk you want to add in ml: "))
        coffee_refill = int(input("How much coffee you want to add in g: "))
        
        water = water + water_refill
        milk = milk + milk_refill
        coffee = coffee + coffee_refill
        
        print("\nrefilling is completed here are the updated resources details: \n")
        report(water, milk, coffee, money)
        
    elif user_select == "off":
        Machine_is_ON = False
    else:
        print("Enter a valid input ")
        
    

    
    
    
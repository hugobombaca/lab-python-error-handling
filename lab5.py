products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
customer_orders = set()

def initialize_inventory(products):
    for product in products:
        valid_input = False
        while not valid_input:
            try:
                quantity = int(input(f"Input the quantity of {product}'s available: "))
                if quantity >= 0:
                    inventory[product]=quantity
                    valid_input = True
                else:
                    print("Quantity cannot be negative.")
            except ValueError:
                    print("Invalid input")
    return inventory
def get_customer_orders(invup):
    valid_input = False
    valid_input2 = False
    while not valid_input:
        try:
            num_order = int(input("number of orders: "))
            if num_order <= 0:
                print("number of orders cannot be negative or 0")
            else:
                valid_input=True
        except ValueError:
            print("numbers plss")

    for y in range(num_order):
        while True:
            try:
                prdname = str(input(f"Enter product name #{y+1} from the list {products}"))
                if prdname not in products:
                    print("Item not in the inventory")
                else:
                    if invup.get(prdname,0)==0:
                        print(f"{prdname} out of stock")
                    else:
                        customer_orders.add(prdname)
                        break
            except ValueError:        
                print("idk")
    return customer_orders

def update_invetory(getorder, invup): 
    for orderedprd in getorder:
        invup[orderedprd]-=1

def calculate_order_statistics(getorder,products):
    TPO = len(getorder)
    PPO = (TPO/len(products))*100
    order_status = (PPO,TPO)
    print(f"Total Products Ordered: {order_status[1]}")
    print(f"Percentage of Products Ordered: {order_status[0]}%")

def print_inventory(invup):
    for product, x in invup.items():
        print(f"{product} : {x}")

def calculate_price(getorder):
    length = len(getorder)
    prices = 0
    for x in range(length):
        valid_price = False
        while not valid_price:
            try:
                pricing = float(input(f"Enter price for item #{x+1}: "))
                if pricing >= 0:
                    valid_price = True
                    prices += pricing
                else:
                    print("price cannot be negative haha!")
            except ValueError:
                    print("numbers pls")                
    return prices 

invup = initialize_inventory(products)
getorder = get_customer_orders(invup)
update = update_invetory(getorder,invup)
calculate_order_statistics(getorder,products)
print_inventory(invup)
whytho = calculate_price(getorder)
print(whytho)


def shopping_cart():
    print("Hi! Welcome to Going Bananas Market Place!")
    print("---- On Sale ----\napples $.50 each\nbananas $.15 each\nlemons: $1.49 each\ndates(pack) $10\nwalnuts(pack) $7")
    cart = {}
    prices = {'apples': 0.75, 'bananas': 0.35, 'lemons': 1.20, 'dates': 12.00, 'walnuts': 7.00}
    qty_items = []
    itemized = []
    cart_total = []
    while True:
        option = str(input("Enter shopping cart option (add/remove/view/quit): "))
        if option.lower() == "quit":
            print("> > > Thank you for shopping with us! < < <")
            break
        
        elif option.lower() == "add":      
            item = str(input("Enter item:"))
            if item in prices:
                item = item
            else:
                print("Please choose from the following list:\napples $.50 each\nbananas $.15 each\nlemons: $1.49 each\ndates(pack) $10\nwalnuts(pack) $7 ")
                item = str(input("Enter item:"))
            quantity = int(input(f"Enter {item} quantity:  "))
            cart[item] = quantity
            if item in cart:
                option = str(input(f"{quantity} {item} has been added to your cart.\nWould you like to add more {item}? yes / no > "))
                if option == "yes":
                    quantity = int(input(f"Enter how many {item} you would like to add:  "))
                    cart[item] += quantity
                if option == "no":
                        continue
                    
        elif option == "remove":
            item = str(input("Enter item to remove: "))
            del cart[item]
                
        elif option == "view":
            print("----- YOUR CART -----") 
            for item in cart:
                print(item, cart[item])
                
            for value in cart.values():
                itemized.append(value)

            for value in prices.values():
                if item in cart:
                    qty_items.append(value)

            for i in range(0, len(itemized)):
                cart_total.append(itemized[i] * qty_items[i])
            # print(cart_total)
            print("---- YOUR TOTAL ----")
            print(f"Your total is ${sum(cart_total):.2f}")
            cart_total = []

shopping_cart()

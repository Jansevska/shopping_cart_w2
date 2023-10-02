def shopping():
    print("Hi! Welcome to Going Bananas Market Place!")
    print("---- On Sale ----\napples $.50 each\nbananas $.15 each\nlemons: $1.49 each\ndates(pack) $10\nwalnuts(pack) $7")
    cart = {}
    # running_options = {"add", "remove", "view", "quit"}
    while True:
        option = str(input("Enter shopping cart option (add/remove/view/quit): "))
        if option.lower() == "quit":
            print("Thank you for shopping with us! A hui hou")
            break
        elif option.lower() == "add":      
            item = str(input("Enter item:"))
            quantity = int(input(f"Enter {item} quantity:  "))
            cart[item] = quantity
            if item in cart:
                option = str(input(f"You have added {quantity} {item} to your cart. Would you like to add more {item}? yes / no > "))
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
                            
shopping()                          
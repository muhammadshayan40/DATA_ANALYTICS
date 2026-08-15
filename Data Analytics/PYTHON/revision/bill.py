while True:
    print("--------BILLING SYSTEM--------")
    print("1. Generate Bill")
    print("2. Close the program")
    choice=int(input("Enter Choice: "))

    if choice == 1:
        cus_name = input("\nEnter your name: ")
        items = input("How many items you bought: ")
        price = []
        total = 0
        for i in range(int(items)):
            print(f"\nItem {i+1}")
            price.append(float(input("Enter the price:")))
            total += price[i]
        
        max_price = max(price)    
        idx = price.index(max_price)
            
        print("\n\n------BILL--------\n") 
        print(f"Customer Name: {cus_name}")
        print(f"Number of items: {items}")
        print(f"Total amount: {total}") 
        print(f"{idx+1} is the expensive item with price: {max_price}\n") 
        
        next_cus= input("Is there another customer? (yes/no): ")
        if next_cus.lower() == "no":
            print("Thank YOU for shopping with us!")
            exit()
            
            
    elif choice ==2:
        print("\n\nThank YOU")
        exit()
    
    else:
        print("\nInvalid Choice\n TRY again")        
 
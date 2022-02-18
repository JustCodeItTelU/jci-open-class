chart = []
total = 0
print("Welcome to JCI Store")
while True:
    print("""
    1. Add Chart
    2. Remove Chart
    3. View Chart
    4. Checkout
    5. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        print("""
        1. Shirt Rp.100000
        2. Jeans Rp.500000
        3. Hoodie Rp.250000
        """)
        product = input("Enter the product: ")
        if product == "1":
            quantity = int(input("Enter the quantity: "))
            chart.append({"product": "Shirt", "price": 100000, "quantity": quantity})
        elif product == "2":
            quantity = int(input("Enter the quantity: "))
            chart.append({"product": "Jeans", "price": 500000, "quantity": quantity})
        elif product == "3":
            quantity = int(input("Enter the quantity: "))
            chart.append({"product": "Hoodie", "price": 250000, "quantity": quantity})
        else:
            print("Invalid product")
    elif choice == "2":
        print("""
        1. Shirt Rp.100000
        2. Jeans Rp.500000
        3. Hoodie Rp.250000
        """)
        product = input("Enter the product to remove: ")
        if product == "1":
            quantity = int(input("Enter the quantity: "))
            chart.remove({"product": "Shirt", "price": 100000, "quantity": quantity})
        elif product == "2":
            quantity = int(input("Enter the quantity: "))
            chart.remove({"product": "Jeans", "price": 500000, "quantity": quantity})
        elif product == "3":
            quantity = int(input("Enter the quantity: "))
            chart.remove({"product": "Hoodie", "price": 250000, "quantity": quantity})
    elif choice == "3":
        if chart == []:
            print("Chart is empty")
        else:
            print(chart)
    elif choice == "4":
        for item in chart:
            total += item["price"] * item["quantity"]
        print(f"Total: {total}")
        print(f"Here Your Receipt: \n{chart}")
    elif choice == "5":
        break


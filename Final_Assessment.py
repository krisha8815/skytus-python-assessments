# To-Do List CLI
tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"'{removed}' removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice!")


# Simple E-Commerce Cart System

products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphones": 3000,
    "Keyboard": 1500
}

cart = {}

while True:
    print("\n===== E-COMMERCE CART =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nAvailable Products:")
        for product, price in products.items():
            print(f"{product} - ₹{price}")

    elif choice == "2":
        product = input("Enter product name: ")

        if product in products:
            qty = int(input("Enter quantity: "))

            if product in cart:
                cart[product] += qty
            else:
                cart[product] = qty

            print("Product added to cart.")
        else:
            print("Product not found.")

    elif choice == "3":
        total = 0

        print("\nYour Cart:")
        for product, qty in cart.items():
            cost = products[product] * qty
            total += cost
            print(f"{product} x {qty} = ₹{cost}")

        print("Total Amount = ₹", total)

    elif choice == "4":
        total = 0

        for product, qty in cart.items():
            total += products[product] * qty

        print("\nFinal Bill = ₹", total)
        print("Thank you for shopping!")
        cart.clear()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
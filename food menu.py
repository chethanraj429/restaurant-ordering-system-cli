menu = {
    "nonveg": {
        "starters": {
            "chicken wings": 250,
            "chicken 65": 200,
            "chicken lollipop": 300
        },
        "main course": {
            "chicken biryani": 350,
            "mutton biryani": 400,
            "chettinad chicken": 300
        }
    },
    "veg": {
        "starters": {
            "gobi manchurian": 150,
            "paneer tikka": 200,
            "aloo tikki": 100
        },
        "main course": {
            "veg biryani": 250,
            "veg pulao": 200,
            "fried rice": 180
        }
    }
}

print("Welcome to the Food Ordering System!\n")


def display_menu(menu):
    print("----------- MENU -----------")
    for food_type in menu:
        print(f"\n{food_type.upper()}")

        for category in menu[food_type]:
            print(f"  {category.capitalize()}")

            for item, price in menu[food_type][category].items():
                print(f"    {item.title():20} {price}rs")
    print("----------------------------")


def take_order(menu):

    orders = []

    while True:

        food_type = input("\nEnter food type (veg/nonveg): ").strip().lower()

        if food_type not in menu:
            print("Invalid food type.")
            continue

        category = input("Enter category (starters/main course): ").strip().lower()

        if category not in menu[food_type]:
            print("Invalid category.")
            continue

        print("\nAvailable Items:")

        for item, price in menu[food_type][category].items():
            print(f"{item.title():20} {price}rs")

        choice = input("\nChoose item: ").strip().lower()

        if choice not in menu[food_type][category]:
            print("Invalid item.")
            continue

        price = menu[food_type][category][choice]

        orders.append((choice, price))

        print(f"{choice.title()} added successfully.")

        more = input("Do you want to order more? (yes/no): ").strip().lower()

        if more == "no":
            break

    return orders


def print_orders(orders):

    if not orders:
        print("No orders placed.")
        return

    print("\n----------- BILL -----------")

    total = 0

    for item, price in orders:
        print(f"{item.title():20} {price}rs")
        total += price

    print("----------------------------")
    print(f"Total: {total}rs")


display_menu(menu)

orders = take_order(menu)

print_orders(orders)

final = input("\nFinalize order? (yes/no): ").strip().lower()

if final == "yes":
    print("\n✅ Order Confirmed!")
    print("Thank you for ordering with us.")
else:
    print("\n❌ Order Cancelled.")
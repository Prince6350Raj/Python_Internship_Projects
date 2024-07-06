print("Welcome!")
menu={
        'Spring Rolls': 120,
        'Garlic Bread': 100,
        'Bruschetta': 130,
        'Margherita Pizza': 250,
        'Pasta Alfredo': 280,
        'Vegetable Lasagna': 260,
        'Paneer Butter Masala': 240,
        'Chocolate Brownie': 150,
        'Cheesecake': 180,
        'Ice Cream Sundae': 120,
        'Gulab Jamun': 100,
        'Coca Cola': 50,
        'Orange Juice': 60,
        'Lemonade': 55,
        'Mojito': 70,
        'Cold Coffee': 90,
        'Hot Coffee': 80
}

print("\nOur Menu: ")
print("-----------")
total_order = 0
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

next_order = True

while next_order:
    order = input("\nEnter the name of item you want to add in your order: ")
    if order in menu:
        total_order += menu[order]
        print(f"{order} added in your order")
        another_order = input("\nDo you want to add another item? press (yes/no): ").lower()
        if another_order == "yes":
            next_order = True
        else:
            next_order = False
    else:
        print(f"{order} is not available")
        another_order = input("\nDo you want to add another item? press (yes/no): ").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False

print(f"Your total bill is: Rs.{total_order}")



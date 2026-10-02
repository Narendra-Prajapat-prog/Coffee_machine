# # jai shree ram


coffee = {
    'Espresso': {
        'prise': 250,
        'Water': 150,
        'milk': 100,
        'coffee': 20
    },

    'Latte': {
        'prise': 350,
        'Water': 100,
        'milk': 150,
        'coffee': 30
    },

    'Cappuccino': {
        'prise': 500,
        'Water': 50,
        'milk': 250,
        'coffee': 40
    }
}

stock = {
    'Water': 10000,
    'milk': 5000,
    'coffee': 1000
}

# Total sales
total_sales = 0

print("☕ COFFEE MENU")
print("1. Espresso")
print("2. Latte")
print("3. Cappuccino")

naru = False

while not naru:

    choice = input("\nEnter coffee name: ").strip().lower()

    selected_coffee = choice.title()

    if selected_coffee in coffee:

        selected = coffee[selected_coffee]

        print("\nYou selected:", selected_coffee)
        print("Price:", '₹', selected["prise"])
        print("Water:", selected["Water"], "ml")
        print("Milk:", selected["milk"], "ml")
        print("Coffee:", selected["coffee"], "g")

        required_water = selected["Water"]
        required_milk = selected["milk"]
        required_coffee = selected["coffee"]

        # Ingredient check
        if (stock["Water"] >= required_water
                and stock["milk"] >= required_milk
                and stock["coffee"] >= required_coffee):

            print("\n✅ Ingredients are sufficient.")
            print("You can make the coffee.")

            # Payment
            price = selected["prise"]

            payment = int(input("\nEnter payment amount: ₹"))

            if payment < price:

                print("❌ Insufficient payment")
                print("Please enter the correct amount.")

            else:

                # Payment successful
                print("✅ Payment successful")

                if payment > price:
                    change = payment - price
                    print("Your change is: ₹", change)

                # Update stock
                stock["Water"] -= required_water
                stock["milk"] -= required_milk
                stock["coffee"] -= required_coffee

                # Update total sales
                total_sales += price

                # Prepare coffee
                print("\n☕ Coffee is being prepared...")
                print("✅ Coffee ready!")

        else:

            print("❌ Sorry, not enough ingredients.")

    else:

        print("❌ Invalid coffee name. Please try again.")

    # Continue or stop
    naru = input("\nEnter Y to continue, N to stop: ").strip().lower()

    if naru == 'y':
        naru = False

    elif naru == 'n':
        naru = True

    else:
        print("❌ Invalid choice. Program stopped.")
        naru = True


# Final Report
print("\n================================")
print("☕ COFFEE MACHINE FINAL REPORT")
print("================================")

print("💰 Total Sales: ₹", total_sales)

print("\n📦 Remaining Stock:")
print("Water:", stock["Water"], "ml")
print("Milk:", stock["milk"], "ml")
print("Coffee:", stock["coffee"], "g")

print("\n🙏 Thank you for visiting!")

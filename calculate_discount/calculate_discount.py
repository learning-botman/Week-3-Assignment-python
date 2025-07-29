def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt the user for inputs
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    # Check if discount was applied
    if final_price < price:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${price:.2f}")

except ValueError:
    print("Please enter valid numeric input.")

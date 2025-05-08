def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
        
    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price
        return price

# Main program
def main():
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: KES "))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Validate input
        if original_price < 0 or discount_percentage < 0:
            print("Price and discount percentage must be positive numbers.")
            return
        
        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display results
        if discount_percentage >= 20:
            print(f"A {discount_percentage}% discount was applied.")
            print(f"Final price after discount: KES {final_price:.2f}")
        else:
            print(f"No discount applied (discount less than 20%).")
            print(f"Original price: KES {final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount.")
if __name__ == "__main__":
    main()
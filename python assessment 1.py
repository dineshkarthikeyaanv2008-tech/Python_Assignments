from decimal import Decimal
import milkrate

def run_calculator():
    print("--- Ksheera Village Milk Co-operative Calculator ---")
    print("Enter details for the farmer (or type 'exit' to stop)")
    
    total_ten_day_payout = Decimal("0.00")
    entry_count = 0

    while True:
        user_input = input("\nEnter litres (or 'exit'): ")
        if user_input.lower() == 'exit':
            break
            
        try:
            litres = float(user_input)
            if litres < 0:
                print("Error: Quantity cannot be negative.")
                continue

            fat = float(input("Enter fat %: "))
            snf = float(input("Enter SNF %: "))

            # Validation logic (as requested in Task 5/9)
            if not (2.0 <= fat <= 7.0):
                print("Error: Fat % must be between 2.0 and 7.0")
                continue
            if not (7.0 <= snf <= 10.0): # Example SNF range
                print("Error: SNF % is out of valid range")
                continue

            # Calculate using the imported module
            # Note: We convert to Decimal for the final total to maintain precision
            current_pay = milkrate.payout(litres, fat, snf)
            current_pay_decimal = Decimal(str(current_pay))
            
            total_ten_day_payout += current_pay_decimal
            entry_count += 1

            print(f"Result: Rate = Rs {milkrate.rate_per_litre(fat, snf):.2f}/L")
            print(f"Payment for this entry: Rs {current_pay:.2f}")
            print(f"Running 10-day Total: Rs {total_ten_day_payout:.2f}")

        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")

    print("\n" + "="*40)
    print(f"FINAL SUMMARY FOR {entry_count} ENTRIES")
    print(f"Total Ten-Day Payout: Rs {total_ten_day_payout:.2f}")
    print("="*40)

if __name__ == "__main__":
    run_calculator()

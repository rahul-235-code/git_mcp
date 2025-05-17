
def add(a, b):
    """
    Add two numbers and return the result
    """
    return a + b

def subtract(a, b):
    """
    Subtract b from a and return the result
    """
    return a - b

def main():
    """
    Main function to run the calculator
    """
    print("Welcome to Basic Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    
    while True:
        try:
            # Get user input
            choice = input("\nEnter operation choice (1/2) or 'q' to quit: ")
            
            # Check if user wants to quit
            if choice.lower() == 'q':
                print("Thank you for using Basic Calculator. Goodbye!")
                break
            
            # Validate operation choice
            if choice not in ['1', '2']:
                print("Invalid choice. Please enter 1, 2, or 'q'.")
                continue
            
            # Get numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform operation
            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            else:
                result = subtract(num1, num2)
                operation = '-'
                
            # Display result
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
        except ValueError:
            print("Error: Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

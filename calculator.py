import math

def add(a, b):
    """Add two numbers and return the result"""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result"""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result"""
    return a * b

def divide(a, b):
    """Divide a by b and return the result"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Return a raised to the power of b"""
    return a ** b

def square_root(a):
    """Return the square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def main():
    """Main function to run the calculator"""
    print("Welcome to Enhanced Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    
    while True:
        try:
            choice = input("\nEnter operation choice (1-6) or 'q' to quit: ")
            
            if choice.lower() == 'q':
                print("Thank you for using Enhanced Calculator. Goodbye!")
                break
            
            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Invalid choice. Please enter 1-6, or 'q'.")
                continue
            
            if choice == '6':
                num1 = float(input("Enter number: "))
                result = square_root(num1)
                print(f"\nResult: √{num1} = {result}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    operation = '+'
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = '-'
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = '*'
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = '/'
                else:
                    result = power(num1, num2)
                    operation = '^'
                
                print(f"\nResult: {num1} {operation} {num2} = {result}")
            
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
try:
    height = int(input("Enter the height for the upper triangular pattern: "))
    if height > 0:
        print("\nUpper Triangular Pattern:")
        for i in range(height, 0, -1):
            spaces = "  " * (height - i)
            print(spaces + "* " * i)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
input("\nPress Enter to exit...")


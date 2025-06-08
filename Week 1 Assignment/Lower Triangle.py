try:
    height = int(input("Enter the height for the lower triangular pattern: "))
    if height > 0:
        print("\nLower Triangular Pattern:")
        for i in range(1, height + 1):
            print("* " * i)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
input("\nPress Enter to exit...")

try:
    height = int(input("Enter the height for the full pyramid: "))
    if height > 0:
        print("\nFull Pyramid Pattern of Stars (*):")
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            stars = '* ' * (i + 1)
            print(spaces + stars)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
input("\nPress Enter to exit...")

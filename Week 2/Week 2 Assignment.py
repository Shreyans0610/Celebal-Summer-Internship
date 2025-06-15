# Author: Shreyans Jain
class Node:
    """
    A class to represent a node in the singly linked list.
    
    Attributes:
        data: The value stored in the node
        next: Reference to the next node in the list
    """
    
    def __init__(self, data):
        """
        Initialize a new node with the given data.
        
        Args:
            data: The value to store in the node
        """
        self.data = data
        self.next = None


class LinkedListException(Exception):
    """Custom exception class for linked list operations."""
    pass


class LinkedList:
    """
    A class to represent a singly linked list.
    
    Attributes:
        head: Reference to the first node in the list
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def add(self, data):
        """
        Add a new node with the given data to the end of the list.
        
        Args:
            data: The value to add to the list
        """
        new_node = Node(data)
        
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        # Add the new node at the end
        current.next = new_node
    
    def print_list(self):
        """
        Print all elements in the list.
        If the list is empty, prints a message indicating so.
        """
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements))
    
    def delete_nth(self, n):
        """Delete the node at position n (1-based index)."""

        # Check if the list is empty
        if not self.head:
            raise LinkedListException("Cannot delete from an empty list")
        
        # Check for invalid index
        if n < 1:
            raise LinkedListException("Index must be greater than 0 (1-based indexing)")
        
        # If deleting the first node
        if n == 1:
            self.head = self.head.next
            return
        
        current = self.head
        for i in range(1, n - 1):
            if not current.next:
                raise LinkedListException(f"Index {n} is out of range")
            current = current.next
        
        # Check if the nth node exists
        if not current.next:
            raise LinkedListException(f"Index {n} is out of range")
        
        # Delete the nth node
        current.next = current.next.next
    
    def size(self):
        """Return the number of elements in the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None


def display_menu():
    """Display the menu options for the user."""
    print("\n" + "="*50)
    print("         SINGLY LINKED LIST OPERATIONS")
    print("="*50)
    print("1. Add element to the list")
    print("2. Display the list")
    print("3. Delete nth element")
    print("4. Get list size")
    print("5. Check if list is empty")
    print("6. Run automated test")
    print("7. Exit")
    print("="*50)


def get_user_input(prompt, input_type=str):
    """
    Get user input with type validation.
    
    Args:
        prompt: The prompt message to display
        input_type: The expected type of input (int, str, etc.)
    
    Returns:
        The validated user input
    """
    while True:
        try:
            if input_type == int:
                return int(input("Enter " + prompt + ": "))
            else:
                return input("Enter " + prompt + ": ")
        except ValueError:
            print(f"Invalid input! Please enter a valid {input_type.__name__}.")


def interactive_linked_list():
    """Interactive function to perform linked list operations based on user input."""
    print("Welcome to the Interactive Singly Linked List Program!")
    ll = LinkedList()
    
    while True:
        display_menu()
        
        try:
            choice = get_user_input("your choice (1-7)", int)
            
            if choice == 1:
                # Add element
                data = get_user_input("the value to add")
                ll.add(data)
                print(f"Added '{data}' to your list.")
                
            elif choice == 2:
                # Display list
                print("\nCurrent List:")
                print("-" * 20)
                ll.print_list()
                
            elif choice == 3:
                # Delete nth element
                if ll.is_empty():
                    print(" Cannot delete from an empty list!")
                else:
                    print(f"Current list size: {ll.size()}")
                    ll.print_list()
                    try:
                        position = get_user_input("the position to delete (1-based index)", int)
                        ll.delete_nth(position)
                        print(f" Successfully deleted element at position {position}")
                        print("Updated list:")
                        ll.print_list()
                    except LinkedListException as e:
                        print(f"Error: {e}")
                        
            elif choice == 4:
                # Get size
                size = ll.size()
                print(f"Current list size: {size}")
                
            elif choice == 5:
                # Check if empty
                if ll.is_empty():
                    print(" The list is empty")
                else:
                    print(f" The list is not empty (contains {ll.size()} elements)")
                    
            elif choice == 6:
                # Run automated test
                print("\n Running automated test...")
                run_automated_test()
                
            elif choice == 7:
                # Exit
                print("Done! Exiting the linked list program")
                break
                
            else:
                print(" Invalid choice! Please select a number between 1 and 7.")
                
        except KeyboardInterrupt:
            print("\n\n Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f" An unexpected error occurred: {e}")


def run_automated_test():
    """Run the original automated test for demonstration."""
    print("\n=== Automated Test Demo ===")
    
    # Create a new linked list for testing
    test_ll = LinkedList()
    
    # Add sample data
    print("\n1. Adding elements [Apple, Banana, Cherry, Date, Elderberry]")
    for item in ["Apple", "Banana", "Cherry", "Date", "Elderberry"]:
        test_ll.add(item)
        print(f"   Added: {item}")
    
    print("\n2. Current list:")
    test_ll.print_list()
    print(f"   Size: {test_ll.size()}")
    
    # Delete middle element
    print("\n3. Deleting 3rd element (Cherry)...")
    try:
        test_ll.delete_nth(3)
        print("   After deletion:")
        test_ll.print_list()
    except LinkedListException as e:
        print(f"   Error: {e}")
    
    # Delete first element
    print("\n4. Deleting 1st element (Apple)...")
    try:
        test_ll.delete_nth(1)
        print("   After deletion:")
        test_ll.print_list()
    except LinkedListException as e:
        print(f"   Error: {e}")
    
    # Test exception handling
    print("\n5. Testing exception handling...")
    try:
        print("   Trying to delete element at position 10...")
        test_ll.delete_nth(10)
    except LinkedListException as e:
        print(f"   Caught expected exception: {e}")
    
    print("\n=== Automated Test Complete ===")


# Run the interactive program if this file is executed directly
if __name__ == "__main__":
    interactive_linked_list()

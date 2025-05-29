class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def print_list(self):
        """Print all elements in the linked list."""
        if not self.head:
            print("List is empty")
            return
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index) from the list."""
        if not self.head:
            raise ValueError("Cannot delete from an empty list")

        if n < 1 or n > self.size:
            raise IndexError(f"Index {n} out of range for list of size {self.size}")

        if n == 1:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        for _ in range(n - 2):
            current = current.next

        if current.next:
            current.next = current.next.next
            self.size -= 1
        else:
            raise IndexError("Unexpected error: next node not found")


def interactive_linked_list():
    ll = LinkedList()
    print("Enter elements to add to the linked list (type 'done' to finish):")

    while True:
        try:
            user_input = input("Enter an element (or 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            # Convert input to integer if possible, otherwise keep as string
            try:
                data = int(user_input)
            except ValueError:
                data = user_input
            ll.append(data)
            print("Current list:", end=" ")
            ll.print_list()
        except Exception as e:
            print(f"Error adding element: {e}")

    if ll.size == 0:
        print("No elements added to the list.")
        return

    # Print final list
    print("\nFinal list:")
    ll.print_list()

    # Delete a node
    while True:
        try:
            user_input = input("\nEnter the index (1-based) of the node to delete (or 'skip' to exit): ")
            if user_input.lower() == 'skip':
                break
            n = int(user_input)
            ll.delete_nth_node(n)
            print("List after deletion:")
            ll.print_list()
        except ValueError as e:
            if str(e).startswith("Cannot delete") or str(e).startswith("Index"):
                print(f"Error: {e}")
            else:
                print("Please enter a valid number or 'skip'.")
        except IndexError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    interactive_linked_list()
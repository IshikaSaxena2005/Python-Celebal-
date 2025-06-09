class Node:
    """Class representing a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
#initializing the class and creating functions: append,print_list, delete_nth_node
class LinkedList:
    """Class to manage the singly linked list."""
    def __init__(self):
        self.head = None



    def append(self, data):
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all nodes in the list."""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        print("Linked List: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node from the list (1-based index)."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        if n <= 0:
            raise Exception("Index must be 1 or greater.")
        if n == 1:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 1
        while current and count < n:
            prev = current
            current = current.next
            count += 1
        if not current:
            raise Exception("Index out of range.")
        prev.next = current.next



if __name__ == "__main__":

    ll = LinkedList()

   
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)

    ll.print_list()


    print("\nDeleting 3rd node...")
    try:
        ll.delete_nth_node(3)
    except Exception as e:
        print("Error:", e)
    ll.print_list()


    print("\nTrying to delete 10th node...")
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)

    print("\nDeleting all nodes one by one...")
    try:
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)  
    except Exception as e:
        print("Error:", e)

    ll.print_list()

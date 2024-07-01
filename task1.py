class Node:
    """
    Class representing a single node in a singly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    Class representing a singly linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Adds a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """
        Prints the contents of the singly linked list.
        """
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print("None")

def reverse_linked_list(linked_list):
    """
    Reverses the singly linked list by modifying the references between nodes.
    """
    prev = None
    curr = linked_list.head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    linked_list.head = prev

def merge_sort(head):
    """
    Implements merge sort for a singly linked list.
    """
    if not head or not head.next:
        return head
    
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    
    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    """
    Finds the middle node of the singly linked list.
    """
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sorted_merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    """
    if not left:
        return right
    if not right:
        return left
    
    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)  # Corrected this line to use right.next
    return result

def sort_linked_list(linked_list):
    """
    Sorts the singly linked list using merge sort.
    """
    linked_list.head = merge_sort(linked_list.head)

def merge_two_sorted_lists(list1, list2):
    """
    Merges two sorted singly linked lists into one sorted list.
    """
    dummy = Node(0)
    tail = dummy
    
    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next

# Example usage
if __name__ == "__main__":
    # Creating and printing the original singly linked list
    linked_list = SinglyLinkedList()
    linked_list.append(5)
    linked_list.append(3)
    linked_list.append(8)
    linked_list.append(1)
    linked_list.append(7)
    print("Original Singly Linked List:")
    linked_list.print_list()

    # Reversing the singly linked list
    reverse_linked_list(linked_list)
    print("Reversed Singly Linked List:")
    linked_list.print_list()

    # Sorting the singly linked list
    sort_linked_list(linked_list)
    print("Sorted Singly Linked List:")
    linked_list.print_list()

    # Merging two sorted singly linked lists
    list1 = SinglyLinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = SinglyLinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    merged_head = merge_two_sorted_lists(list1.head, list2.head)
    merged_list = SinglyLinkedList()
    merged_list.head = merged_head
    print("Merged Sorted Singly Linked List:")
    merged_list.print_list()


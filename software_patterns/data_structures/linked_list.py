class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node  # type: ignore
            self.tail = new_node

    def delete(self, value) -> bool:
        """1. The `delete()` method begins by setting a `temp` reference to the `head` of the **Linked List**. This temp reference will be used to traverse the list.
        2. The first `if` statement checks if the head of the list is not `None` or, in other words, if the list is not empty. Then, inside the `if` block, it checks if the head node is the node to be deleted _(i.e., its value matches the `value` parameter)_. If it is, the head is updated to be the next node in the list _(potentially `None` if the head was the only node in the list)_, and then the old head node is deleted by setting `temp` to `None`.
        3. If the head node is not the one to be deleted, the list is traversed in search of the node. The `prev` reference is updated as the current node before `temp` moves on to the next one. If at any point during the traversal, a node with a value matching the `value` parameter is found, the loop breaks, leaving `temp` pointing to the node to delete and `prev` pointing to its predecessor.
        4. After traversal, if `temp` is `None`, this means the node to delete was not found, and the function returns. Otherwise, the predecessor's `next` reference (which currently points to the to-be-deleted node) is updated to point to the successor of the node to be deleted, thus excluding it from the list. The node is then deleted by setting `temp` to `None`.

        Args:
            value (_type_): _description_

        Returns:
            bool: Returns `True` if the node was found and deleted, otherwise `False`.
        """
        # Step 1
        temp = self.head

        # Step 2
        if temp is not None and temp.value == value:
            self.head = temp.next
            temp = None  # NOTE: I believe this is to help the garbage collector
            return True

        prev = None
        # Step 3
        while temp is not None:
            if temp.value == value:
                break
            prev = temp
            temp = temp.next

        # Step 4
        if temp == None:
            return False

        prev.next = temp.next  # type: ignore
        temp = None  # NOTE: I believe this is to help the garbage collector
        return True

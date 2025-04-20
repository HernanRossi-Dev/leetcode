from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListAddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = None
        current_node = None
        carry = 0
        while True:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            vsum = v1 + v2 + carry
            carry = vsum // 10
            nval = vsum % 10
            new_node = ListNode(val=nval, next=None)
            if not result_head:
                result_head = new_node
            else:
                current_node.next = new_node
            current_node = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not l1 and not l2 and carry == 0:
                break
        return result_head
    
class TestLinkedListAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.add_linked_list = LinkedListAddTwoNumbers()


if __name__ == "__main__":
    unittest.main()

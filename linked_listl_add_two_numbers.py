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
            vsum = v1 + v1 + carry
            carry = vsum // 10
            nval = vsum % 10
            if not result_head:
                result_head = current_node = ListNode(val=nval, next=None)
            else:
                new_node = ListNode(val=nval, next=None)
                current_node.next = new_node
                current_node = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not l1 and not l2:
                break
        return result_head
    
class TestLinkedListAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.add_linked_list = LinkedListAddTwoNumbers()

    def test_case_one(self):
        test = [7, 1, 5, 3, 6, 4]
        result = self.find_max_profit.maxProfit(test)
        self.assertEqual(result, 7)

    def test_case_two(self):
        test = [1, 2, 3, 4, 5]
        result = self.find_max_profit.maxProfit(test)
        self.assertEqual(result, 4)

    def test_case_three(self):
        test = [7, 6, 4, 3, 1]
        result = self.find_max_profit.maxProfit(test)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()

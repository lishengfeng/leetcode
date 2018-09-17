class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :return: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        cval = l1.val + l2.val
        if cval < 10:
            res_node = ListNode(cval)
            res_node.next = self.add_two_numbers(l1.next, l2.next)
            return res_node
        else:
            cval = cval - 10
            res_node = ListNode(cval)
            res_node.next = self.add_two_numbers(
                    ListNode(1), self.add_two_numbers(l1.next, l2.next))
            return res_node

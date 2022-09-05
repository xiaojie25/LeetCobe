# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(10086)
        carry = 0
        move = res
        while l1 != None or l2 != None:
            if l1 == None:
                l1, l2 = l2, l1 # swap
            if l2 != None:
                carry, l1.val = divmod(l1.val+l2.val+carry, 10)
                move.next = l1
                l1, l2, move = l1.next, l2.next, move.next
            else:
                carry, l1.val = divmod(l1.val+carry, 10)
                move.next = l1
                l1, move = l1.next, move.next
            if carry ==1:
                move.next = ListNode(carry)

        return res.next


if __name__ == '__main__':
    pass
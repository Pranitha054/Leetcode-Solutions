# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            newnode = curr.next
            curr.next = prev
            prev = curr
            curr = newnode
        return prev  

    def addTwoNumbers(self, l1, l2):
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        num1, num2 = 0, 0   
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next       
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        total = num1 + num2
        dummy = ListNode(0)
        curr = dummy
        
        if total == 0:
            return ListNode(0)
        
        while total > 0:
            digit = total % 10
            total //= 10
            curr.next = ListNode(digit)
            curr = curr.next
        
        return dummy.next 
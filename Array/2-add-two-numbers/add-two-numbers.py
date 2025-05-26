# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        sum = 0
        carry = 0

        num1 = l1
        num2 = l2

        dummy = ListNode()
        out = dummy

        while num1 or num2:
            val1 = num1.val if num1 else 0
            val2 = num2.val if num2 else 0

            sum = carry + val1 + val2

            if sum < 10:
                out.next = ListNode(sum)
                carry = 0
            else:
                out.next = ListNode(sum % 10)
                carry = sum//10
                sum = 0
             



            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next

            out = out.next
        
        if carry:
            out.next =  ListNode(carry)
        
        return dummy.next

        
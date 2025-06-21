# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeList(self, list1, list2):
        dummy = ListNode()

        curr = dummy

        while list1 or list2:
            n1 = list1.val if list1 else float('inf')
            n2 = list2.val if list2 else float('inf')
            if n1<= n2:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        while len(lists) > 2:
            mid = len(lists)//2
            temp = []
            temp.append(self.mergeKLists(lists[:mid+1]))
            temp.append(self.mergeKLists(lists[mid+1:]))
            lists = temp
        
        if len(lists) == 2:
            return self.mergeList(lists[0], lists[1])
        elif len(lists) == 1:
            return lists[0]
        return None




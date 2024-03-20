# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=[]
        while head:
            s.append(head)
            head=head.next
        temp=ListNode()
        dummy=temp
        while s:
            temp.next=s.pop()
            temp=temp.next
        temp.next=None
        return dummy.next

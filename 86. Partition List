# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        s1=[]
        s2=[]
        tmp=head
        while head:
            y=head.val
            if y<x:
                s1.append(y)
            else:
                s2.append(y)
            head=head.next
        tmp1=tmp
        head=tmp
        i=0
        l=len(s1)
        while i<l:
            tmp=ListNode()
            tmp.val=s1[i]
            head.next=tmp
            head=head.next
            i+=1
        
        i=0
        l=len(s2)
        while i<l:
            tmp=ListNode()
            tmp.val=s2[i]
            head.next=tmp
            head=head.next
            i+=1
        return tmp1.next

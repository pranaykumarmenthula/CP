# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp=head
        l=''
        while temp is not None:
            l+=str(temp.val)
            temp=temp.next
        return int(l,2)


######

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=[]
        while head:
            s.append(head.val)
            head=head.next
        dec=0
        length=0
        while s:
            dec+=math.pow(2,length)*s.pop()
            length+=1
        return int(dec)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        while head:
            curval=head.val
            while stack and stack[-1] < curval:
                stack.pop()
            stack.append(head.val)
            head=head.next

        head=ListNode()
        temp1=head
        i=0
        l=len(stack)
        while i<l:
            temp=ListNode()
            temp.val=stack[i]
            head.next=temp
            head=head.next
            i+=1
        temp1=temp1.next
        return temp1
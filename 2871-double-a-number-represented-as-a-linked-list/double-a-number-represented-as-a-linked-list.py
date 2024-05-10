class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next

        nxt, carry = None, 0
        while stack:
            curr = stack.pop()
            curr.next = nxt
            nxt = curr
            carry += curr.val * 2
            curr.val = carry % 10
            carry //= 10

        if carry > 0:
            curr = ListNode(carry, nxt)

        return curr
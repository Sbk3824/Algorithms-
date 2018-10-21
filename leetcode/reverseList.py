class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            nexxt = cur.next
            cur.next = prev
            prev = cur
            cur = nexxt
        return prev
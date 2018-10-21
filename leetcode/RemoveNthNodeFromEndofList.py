class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        behind = head
        
        for i in range(n):
            cur = cur.next
        if cur is None:      
            head = head.next
            return head
        while cur.next != None:
            cur = cur.next
            behind = behind.next
        behind.next = behind.next.next
        return head
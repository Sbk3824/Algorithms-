class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        def findLength(head):
            leng = 0
            while head:
                head = head.next
                leng+= 1
            return leng
        
        leng = findLength(head)
        k = k%leng
        
        def findEnd(head):
            pre = ListNode(-1)
            pre.next = head
            cur = head
            while cur and cur.next:
                cur = cur.next
                pre = pre.next
            return cur,pre
        
        def rotate(head):
            end,pre = findEnd(head)
            end.next = head
            pre.next = None
            head = end
            return head
        
        for _ in range(k):
            head = rotate(head)
        return head
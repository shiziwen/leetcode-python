# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        p = head
        q = head
        pPre = None
        
        for i in range(n-1):
            q = q.next
        
        while q.next:
            pPre = p
            p = p.next
            q = q.next
        
        if pPre is None:
            head = p.next
            del p
        else:
            pPre.next = p.next
            del p
        
        return head
            
            

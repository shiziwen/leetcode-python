# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        new_node = ListNode(-1)
        new_node.next = head
        p = new_node
        tmp = new_node.next
        
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                val = tmp.val
                while tmp and tmp.val == val:
                    tmp = tmp.next
                p.next = tmp
            else:
                p = p.next
                tmp = tmp.next
        
        return new_node.next

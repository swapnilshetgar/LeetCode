# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """ 
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # move slow by 1 step
            fast = fast.next.next     # move fast by 2 steps
            
            if slow == fast:          # cycle detected
                return True
        
        return False  # no cycle
        
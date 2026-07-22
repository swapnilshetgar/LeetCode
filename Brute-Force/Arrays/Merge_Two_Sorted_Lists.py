
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []
         # Add all values from list1
        while list1:
            arr.append(list1.val)
            list1 = list1.next

        # Add all values from list2
        while list2:
            arr.append(list2.val)
            list2 = list2.next

        # Sort the combined list
        arr.sort()

        # Create a new linked list
        temp = ListNode(0)
        current = temp

        for num in arr:
            current.next = ListNode(num)
            current = current.next

        return temp.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev = None
        slow = head
        fast = head
        offset = 1
        while fast.next:
            fast = fast.next

            if offset >= n:
                prev = slow
                slow = slow.next
            offset += 1

        if prev and slow:
            prev.next = slow.next
            slow.next = None
        elif not prev and n == 1:
            return
        elif not prev and n == offset:
            return slow.next

        return head

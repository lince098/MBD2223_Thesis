# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reorderList(self, head):
        # No need to reorder if the list is empty or has 1 or 2 elements
        if not head or not head.next or not head.next.next:
            return

        # Find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # Reverse the second half of the list
        curr = head2
        prev = None

        while curr:
            holder = curr.next
            curr.next = prev
            prev = curr
            curr = holder

        # Merge the two halves of the list alternatively
        curr1 = head
        curr2 = prev  # Because after reversing the second half, the last node is actually the head of our reversed list

        while curr2:
            holder1, holder2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = holder1
            curr1, curr2 = holder1, holder2

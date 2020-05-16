# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if (head == None):
            return

        tmp = head.next
        prev, cur, next = None, head, head.next
        count = 1

        while (next != None):
            cur.next = next.next
            prev = cur
            cur = next
            next = next.next

            count += 1

        if (count % 2 == 0):
            prev.next = tmp
        else:
            cur.next = tmp

        return head

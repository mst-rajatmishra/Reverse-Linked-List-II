# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ptr1 = newList = ListNode(-1)
        rightSubList = None
        stack = []
        count = 0

        while head:
            count += 1
            if count >= left:
                stack.append(head)
                if count == right:
                    rightSubList = head.next
                    break
            else:
                ptr1.next = head
                ptr1 = ptr1.next
            head = head.next
            
        # print(stack)
        while len(stack):
            ptr1.next = stack.pop()
            ptr1 = ptr1.next
        ptr1.next = rightSubList
        return newList.next

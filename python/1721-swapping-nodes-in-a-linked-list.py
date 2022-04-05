# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        first = head
        second = head
        third = head    # Initialize ⭐

        pos = 1         # To check the Kth position ⤵️
        
        # Shift third to K pos forward from second
        while third.next and pos<k:
            third = third.next
            pos += 1
        
        pos = 1         # Reset position counter 🔃
        
        # Shift second and third till third ends
        while third.next:
            second = second.next
            third = third.next
            
        # Shift first to k pos
        while first and pos<k:
            first = first.next
            pos += 1
            
        first.val, second.val = second.val, first.val

        return head
            
            
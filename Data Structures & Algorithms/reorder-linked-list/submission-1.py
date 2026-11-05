# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1Parte: individuo le due metà
        #creo due puntatori
        slow, fast = head, head.next
        #velocità diverse, slow arriva a metà
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #2parte: inverto la seconda metà
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp
        
        #3parte: le ricollego in modo alternato
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 
        

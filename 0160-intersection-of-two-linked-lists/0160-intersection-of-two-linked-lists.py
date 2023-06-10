# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        curA = headA
        curB = headB

        endNodeA = None
        endNodeB = None

        countA = 0
        countB = 0

        while curA or curB:
            if curA == None:
                endNodeA = curA
                countA += 1
            if curB == None:
                countB += 1
                endNodeB = curB
            if curA != None:
                curA = curA.next
            if curB != None:
                curB = curB.next
        
        curA = headA
        curB = headB

        while curA or curB:
            if curA == curB:
                return curA
            if curA != None and countA == 0:
                curA = curA.next
            if curB != None and countB == 0:
                curB = curB.next
            if countA != 0:
                countA -= 1
            if countB != 0:
                countB -= 1
        
        
        if endNodeA != endNodeB:
            return None





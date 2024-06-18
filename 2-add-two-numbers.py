# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next        

class Solution:            
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1List = []
        l2List = []
        while l1:
            l1List.append(l1.val)
            l1 = l1.next
        
        while l2:
            l2List.append(l2.val)
            l2 = l2.next
            
        lNew = []
        total = 0
        
        for i in  range(len(l1List)):
            lNew.append(str(l1List[i]) + "0"*i)
        
        for j in range(len(l2List)):
            lNew.append(str(l2List[j]) + "0"*j)
            
        for num in lNew:
            total += int(num)
            
        
        totalList = list(str(total))
        totalList.reverse()
            
        def create_linked_list(values):
            if not values:
                return None
            
            head = ListNode(values[0])
            current = head
            
            for value in values[1:]:
                current.next = ListNode(value)
                current = current.next
                
            return head
        
        linked_list_head = create_linked_list(totalList)
        
        # def print_linked_list(head):
        #     current = head
        #     while current:
        #         print(current.val, end=" -> " if current.next else "\n")
        #         current = current.next
    
        # # Print the linked list to verify
        # print_linked_list(linked_list_head)
        
        # for values in totalList:
            
        #     newList = ListNode(5)
        #     newList.next = ListNode(7)
        #     newList.next.next = ListNode(9)
        
        return linked_list_head
        
solution = Solution()

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

print(solution.addTwoNumbers(l1, l2))
        
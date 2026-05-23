#143

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         slow = head
#         fast = head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         second = slow.next
#         slow.next = None 
#         prev = None
#         curr = second
#         while curr:
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node
#         second = prev
#         first = head
#         while second:
#             tmp1 = first.next
#             tmp2 = second.next
#             first.next = second
#             second.next = tmp1
#             first = tmp1
#             second = tmp2
        



#19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0, head)
#         fast = dummy
#         slow = dummy

#         for i in range(n + 1):
#             fast = fast.next
            
#         while fast is not None:
#             fast = fast.next
#             slow = slow.next
            
#         slow.next = slow.next.next
#         return dummy.next



#206


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         now = head
#         prev = None
#         while now is not None:
#             next_node = now.next
#             now.next = prev
#             prev = now
#             now = next_node
#         return prev



#2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         head = None  
#         tail = None  
#         carry = 0    
        

#         while l1 is not None or l2 is not None or carry > 0:
            
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
        
#             total = val1 + val2 + carry
#             carry = total // 10      
#             digit = total % 10       
#             new_node = ListNode(digit)
            
#             if head is None:
#                 head = new_node
#                 tail = new_node
#             else:
#                 tail.next = new_node 
#                 tail = new_node
#             if l1: l1 = l1.next
#             if l2: l2 = l2.next
            
#         return head

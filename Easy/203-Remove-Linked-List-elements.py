# Given the head of a linked list and an integer val, 
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # extra_node would be a new initial head - 
        # in case of the actual head containing value to be removed
        extra_node = ListNode(next=head)
        
        # use two pointers to iterate through the linked list: previous and current
        previous = extra_node
        current = head

        # iterate through the linked list while current != Null
        while current:
            next_node = current.next

            # delete val just by redirecting the pointer
            if current.val == val:
                previous.next = next_node
            
            # continue iteration through the linked list
            else:
                previous = current
                
            # current pointer always moves
            current = next_node

        # it always poimts to the actual head
        return extra_node.next





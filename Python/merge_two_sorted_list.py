# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            if l2 is not None:
                return l2
            return None
        if l2 is None:
            if l1 is not None:
                return l1
            return None
        
        temp1 = l1
        temp2 = l2
        output = []
        new_list = ListNode(min(l1.val, l2.val))
        temp_new_list = new_list
        while temp1:
            output.append(temp1.val)
            temp1 = temp1.next
        while temp2:
            output.append(temp2.val)
            temp2 = temp2.next
        output.sort()
        for i in range(1,len(output)):
            temp_new_list.next = ListNode(output[i])
            temp_new_list = temp_new_list.next
            
        temp_new_list.next = None
        return new_list

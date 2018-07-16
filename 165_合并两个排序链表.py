"""
将两个排序链表合并为一个新的排序链表

给出 1->3->8->11->15->null
      2->null
返回 1->2->3->8->11->15->null
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        temp = dummy
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        
        # 考虑尾巴
        if l1 is None:
            temp.next = l2
        else:
            temp.next = l1
        
        return dummy.next


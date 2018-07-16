"""
给定一个排序链表，删除所有重复的元素每个元素只留下一个。

给出 1->1->2->null，返回 1->2->null
给出 1->1->2->3->3->null，返回 1->2->3->null
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
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return head
        p = head
        while p.next is not None:
            if p.val == p.next.val:  # 比较的时候用val属性比较
                p.next = p.next.next
            else:
                p = p.next
        return head

"""
删除链表中等于给定值val的所有节点。

给出链表 1->2->3->3->4->5->3, 和 val = 3, 你需要返回删除3之后的链表：1->2->4->5。
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
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        
        #if head is None:
        #    return head
        # 这个写法包含了head是null的情况
        dummy = ListNode(-1, next=head)
        p = dummy
        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next    

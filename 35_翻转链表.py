"""
翻转一个链表:给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null
挑战：在原地一次翻转完成
"""

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# 翻转链表 基础中的基础
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        cur = None
        while head is not None:
            temp = head.next
            head.next = cur
            # 下一次迭代 把cur和head往前推一位
            cur = head
            head = temp
        return cur

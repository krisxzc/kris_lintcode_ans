"""
翻转一个链表：给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null
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
        pre = None
        while head is not None:
            temp = head.next
            head.next = pre
            # 下一次迭代 把cur和head往前推一位
            pre = head
            head = temp
        return pre

   
############## 翻转链表2
"""
翻转链表中第m个节点到第n个节点的部分：给出链表1->2->3->4->5->null， m = 2 和n = 4，返回1->4->3->2->5->null
# 234变成432
m，n满足1 ≤ m ≤ n ≤ 链表长度

挑战：在原地一次翻转完成
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
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    
    def reverse(self, head):
        # write your code here
        pre = None
        while head is not None:
            temp = head.next
            head.next = pre
            # 下一次迭代 把cur和head往前推一位
            pre = head
            head = temp
        return pre
    
    
    
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1, next=head)
        p = dummy
        q = dummy
        # 将p定位到m-1位，q定位到n位
        for _ in range(m-1):
            p = p.next
        for _ in range(n):
            q = q.next
        
        
        n_next = q.next     #第n+1位
        m_th = p.next       #第m位
        q.next = None
        # m位开始的链表
        # m -> m+1 -> ... -> n -> null
        
        A = self.reverse(m_th)
        # 翻转后  null <- m <- m+1 <- ... <- n    head为A
        
        m_th.next = n_next   
        p.next = A
        
        return dummy.next
            
            



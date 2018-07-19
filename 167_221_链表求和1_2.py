########### 链表求和1 ###############

"""
你有两个用链表代表的整数，其中每个节点包含一个数字。
数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
写出一个函数将两个整数相加，用链表形式返回和。

给出两个链表 3->1->5->null 和 5->9->2->null，  513+295
返回 8->0->8->null     808 
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
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        if l1 is None: 
            return l2
        if l2 is None: 
            return l1
        
        dummy = ListNode(0, next=l1)
        p = dummy.next
        
        while l1.next is not None or l2.next is not None:
            ####存在某一链表next为空时，构造next.val = 0，不影响加法结果
            #这个想法特别6
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            
            # 大于10则进一位
            SumNum = l1.val + l2.val
            if SumNum >= 10:
                p.val = SumNum % 10
                l1.next.val += 1   #或者l2的值加1也行
            else:
                p.val = SumNum
            
            l1 = l1.next
            l2 = l2.next
            p = p.next
        
        # 末尾节点单独处理，即l1.next和l2.next都为null时    
        else:
            p.val = l1.val + l2.val
            if p.val >= 10:
                p.val = p.val % 10
                p.next = ListNode(1)
        return dummy.next
        
        
        
        
        
        
        
        
        
        
########### 链表求和2 ###############
# 简单的思路就是先反转链表，然后跟上面一样链表相加，再翻转回来
# 不知道还有没有其他思路

"""
假定用一个链表表示两个数，其中每个节点仅包含一个数字。
假设这两个数的数字顺序排列，请设计一种方法将两个数相加，并将其结果表现为链表的形式。

给出 6->1->7 + 2->9->5。即，617 + 295。
返回 9->1->2。即，912 。
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
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """

    def addLists2(self, l1, l2):
        # write your code here
        def reverse(head):
            pre = None
            while head is not None:
                temp = head.next
                head.next = pre
            
                pre = head
                head = temp
            return pre
        
        
        l1 = reverse(l1)
        l2 = reverse(l2)
    
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        dummy = ListNode(0, next=l1)
        p = dummy.next
        
        while l1.next is not None or l2.next is not None:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            
            SumNum = l1.val + l2.val
            if SumNum >= 10:
                p.val = SumNum % 10
                l1.next.val += 1
            else:
                p.val = SumNum
                
            p = p.next
            l1 = l1.next
            l2 = l2.next
            
        else:
            SumNum = l1.val + l2.val
            if SumNum >= 10:
                p.val = SumNum % 10
                p.next = ListNode(1)
            else:
                p.val = SumNum
        
        return reverse(dummy.next)
        
        
        
        
        
        
        
        

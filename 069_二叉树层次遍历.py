"""
给一棵二叉树 {3,9,20,#,#,15,7} ：

  3
 / \
9  20
  /  \
 15   7

返回他的分层遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

挑战1：只使用一个队列去实现它
挑战2：用DFS算法来做
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


######## 两个队列
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        res = [] 
        # 如果根节点为空,则返回空列表 
        if root is None: 
            return res
        # 模拟一个队列储存节点 
        q = [] 
        # 首先将根节点入队 
        q.append(root) 
        # 列表为空时,循环终止 
        while len(q) != 0: 
            # 使用列表存储同层节点 
            tmp = [] 
            # 记录同层节点的个数 
            length = len(q) 
            # 将同层节点出列，同时记录下一层节点
            for i in range(length): 
                # 将同层节点依次出队 
                r = q.pop(0) 
                tmp.append(r.val) 
                if r.left is not None: 
                    # 非空左孩子入队 
                    q.append(r.left) 
                if r.right is not None: 
                    # 非空右孩子入队 
                    q.append(r.right) 
            res.append(tmp) 
        return res
        
        
        
# DFS 深度优先算法
class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        result = []
        
        if root is None:
            return result
        
        thisLevel = 0
        self.DFS(root, result, thisLevel)
        return result
    
    def DFS(self, root, result, thisLevel):
        if root is None:
            return
        if thisLevel > len(result) - 1:
            result.append([])
        result[thisLevel].append(root.val)
        thisLevel += 1
        self.DFS(root.left, result, thisLevel)
        self.DFS(root.right, result, thisLevel)
        return    

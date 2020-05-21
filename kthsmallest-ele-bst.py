# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node, st = root, []

        while(st or node):
            if node:
                st.append(node)
                node = node.left
            else:
                node = st.pop()
                k -= 1
                if (k == 0):
                    return node.val
                node = node.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        head=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        preorderleft=preorder[1:mid+1]
        preorderright=preorder[mid+1:]
        inorderleft=inorder[:mid]
        inorderright=inorder[mid+1:]
        head.left=self.buildTree(preorderleft,inorderleft)
        head.right=self.buildTree(preorderright,inorderright)
        return head

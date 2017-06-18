# http://www.lintcode.com/en/problem/convert-bst-to-greater-tree/
#
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
#
# Have you met this question in a real interview? Yes
# Example
# Given a binary search Tree ｀{5,2,3}｀:
#
#               5
#             /   \
#            2     13
# Return the root of new tree
#
#              18
#             /   \
#           20     13

class GreaterTree:
    total = 0

    def convertBST(self, root):
        self.helper(root)
        return root

    def helper(self, root):
        if root is None:
            return
        if root.right:
            self.helper(root.right)

        self.total += root.val
        root.val = self.total

        if root.left:
            self.helper(root.left)

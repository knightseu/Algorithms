class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def max_depth(self):
        return self._max_depth_helper(node=self)

    def _max_depth_helper(self, node):
        if node is None:
            return 0

        left_dep = self._max_depth_helper(node.left)
        right_dep = self._max_depth_helper(node.right)
        return max(left_dep, right_dep) + 1;
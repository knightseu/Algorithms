"""

V1:
http://www.lintcode.com/en/problem/binary-tree-path-sum/
Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.
Given a binary tree, and target = 5:

     1
    / \
   2   4
  / \
 2   3
 
return

[
  [1, 2, 2],
  [1, 4]
]

V2:
http://www.lintcode.com/en/problem/binary-tree-path-sum-ii/
Your are given a binary tree in which each node contains a value. Design an algorithm to get all paths which sum to a given value. The path does not need to start or end at the root or a leaf, but it must go in a straight line down.
Given a binary tree:

    1
   / \
  2   3
 /   /
4   2
for target = 6, return

[
  [2, 4],
  [1, 3, 2]
]


V3:
http://www.lintcode.com/en/problem/binary-tree-path-sum-iii/
Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.

Example
Given binary tree:

    1
   / \
  2   3
 /
4
and target = 6. Return :

[
  [2, 4],
  [2, 1, 3],
  [3, 1, 2],
  [4, 2]
]

"""

from Commons.TreeNode import TreeNode


def build_tree():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(4)
    node4 = TreeNode(2)
    node5 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    return node1


def build_tree2():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(2)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    return node1
    pass


def binary_tree_path_sum(root, target):
    result = []
    path = []
    dfs(root, path, result, 0, target)
    return result


def dfs(root, path, result, len, target):
    if root is None:
        return

    path.append(root.val)
    len += root.val

    if root.left is None and root.right is None and len == target:
        result.append(path[:])

    dfs(root.left, path, result, len, target)
    dfs(root.right, path, result, len, target)

    len -= root.val
    path.pop()


def binary_tree_path_sum_ii(root, target):
    result = []
    path = []
    dfs_ii(root, path, result, 0, target)
    return result


def dfs_ii(root, path, result, level, target):
    if root is None:
        return

    path.append(root.val)

    # check back in path
    tmp = target
    for i in range(level, -1, -1):
        tmp -= path[i]
        if tmp == 0:
            result.append(path[i:0])
    dfs(root.left, path, result, level+1, target)
    dfs(root.right, path, result, level+1, target)

    path.pop()


def binary_tree_path_sum_iii(root, target):
    """
    经典双重递归，第一重遍历，第二重找路径
    :param root: 
    :param target: 
    :return: 
    """
    result = []
    dfs_iii(root, result, target)
    return result


def dfs_iii(root, result, target):
    """
    遍历每个树的节点
    :param root: 
    :param result: 
    :param target: 
    :return: 
    """
    if root is None:
        return
    path = []
    find_sum(root=root, from_node=None, result=result, path=path, target=target)

    dfs_iii(root=root.left, result=result, target=target)
    dfs_iii(root=root.right, result=result, target=target)


def find_sum(root, from_node, result, path, target):
    path.append(root.val)
    target -= root.val
    if target == 0:
        result.append(path[:])

    # go up
    if root.parent not in [None, from_node]:
        find_sum(root=root.parent, from_node=root, result=result, path=path, target=target)
    # go left
    if root.left not in [None, from_node]:
        find_sum(root=root.left, from_node=root, result=result, path=path, target=target)
    # go right
    if root.right not in [None, from_node]:
        find_sum(root=root.right, from_node=root, result=result, path=path, target=target)

    path.pop()
    pass

##########
#
# v1
#
##########
root = build_tree()
print(root.max_depth())
# rst = binary_tree_path_sum(root=root, target=5)
# print(rst)





##########
#
# v2
#
##########
# root = build_tree2()
# rst = binary_tree_path_sum(root=root, target=5)
# print(rst)
#
#
# ##########
#
# v3
#
##########
# root = build_tree2()
# rst = binary_tree_path_sum(root=root, target=5)
# print(rst)

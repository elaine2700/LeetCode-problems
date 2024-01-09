class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def leafSimilar(self, root1, root2):
        
        leaf_1 = list()
        leaf_2 = list()

        self.dfs(root1, leaf_1)
        self.dfs(root2, leaf_2)

        return leaf_1 == leaf_2
    
    def dfs(self, node, leaf_list):
        if node:
            if not node.left and not node.right:
                leaf_list.append(node.val)
            self.dfs(node.left, leaf_list)
            self.dfs(node.right, leaf_list)
    
    



root_1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
root_2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))

run_program = Solution()
print(run_program.leafSimilar(root_1, root_2))
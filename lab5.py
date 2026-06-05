# # 102

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
        
#         result = []
#         # Использование deque обеспечивает быстрое извлечение элементов слева за O(1)
#         queue = deque([root])
        
#         while queue:
#             level_size = len(queue)
#             current_level = []
            
#             for i in range(level_size):
#                 node = queue.popleft()
#                 current_level.append(node.val)
                
#                 # Добавляем потомков в очередь для следующего уровня
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
            
#             result.append(current_level)
            
#         return result


# 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         # Базовый случай: если узел отсутствует (пустое дерево или конец ветви),
#         if not root:
#             return 0

#         # Рекурсивно вычисляем глубину левого поддерева.
#         left_depth = self.maxDepth(root.left)

#         # Рекурсивно вычисляем глубину правого поддерева.
#         right_depth = self.maxDepth(root.right)

#         # Глубина текущего дерева равна 1 (за текущий узел) плюс максимальная
#         # из глубин его левого и правого поддеревьев.
#         return 1 + max(left_depth, right_depth)



# 226


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return None
        
#         # Меняем местами левого и правого потомков
#         root.left, root.right = root.right, root.left
        
#         # Рекурсивно инвертируем поддеревья
#         self.invertTree(root.left)
#         self.invertTree(root.right)
        
#         return root


# 235

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         current = root
        
#         while current:
#             # Если оба узла в левом поддереве
#             if p.val < current.val and q.val < current.val:
#                 current = current.left
#             # Если оба узла в правом поддереве
#             elif p.val > current.val and q.val > current.val:
#                 current = current.right
#             # Точка разделения найдена — это и есть наименьший общий предок
#             else:
#                 return current



# 98

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def validate(node, low=-float('inf'), high=float('inf')):
#             # Пустое дерево всегда является валидным BST
#             if not node:
#                 return True
            
#             # Значение текущего узла должно строго лежать в границах (low, high)
#             if not (low < node.val < high):
#                 return False
            
#             # Рекурсивно проверяем левое и правое поддеревья с обновленными границами
#             return (validate(node.left, low, node.val) and 
#                     validate(node.right, node.val, high))
        
#         return validate(root)
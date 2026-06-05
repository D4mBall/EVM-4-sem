# 133

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:
#             return None
        
#         copied = {}  # наш «блокнот» для хранения копий
        
#         def dfs(curr):
#             # Если копия уже создана, сразу возвращаем её
#             if curr in copied:
#                 return copied[curr]
            
#             # Создаем копию и сохраняем её в блокнот
#             copied[curr] = Node(curr.val)
            
#             # Копируем соседей одной строкой
#             copied[curr].neighbors = [dfs(neighbor) for neighbor in curr.neighbors]
            
#             return copied[curr]
        
#         return dfs(node)
        


# 200


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
        
#         rows, cols = len(grid), len(grid[0])
#         islands_count = 0
        
#         def dfs(r: int, c: int):
#             # Проверка выхода за границы сетки или если ячейка — вода ('0')
#             if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
#                 return
            
#             # Помечаем ячейку как посещенную, меняя '1' на '0'
#             grid[r][c] = '0'
            
#             # Рекурсивно обходим соседей (вверх, вниз, вправо, влево)
#             dfs(r + 1, c)
#             dfs(r - 1, c)
#             dfs(r, c + 1)
#             dfs(r, c - 1)
            
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '1':
#                     islands_count += 1
#                     dfs(r, c)  # Запускаем DFS, чтобы пометить весь остров
                    
#         return islands_count



# 207


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # 1. Строим граф в виде списка смежности
#         # prereq -> course (чтобы пройти course, нужно сначала пройти prereq)
#         graph = {i: [] for i in range(numCourses)}
#         for course, prereq in prerequisites:
#             graph[prereq].append(course)
        
#         # Массив состояний для каждого курса: 0, 1 или 2
#         state = [0] * numCourses
        
#         def has_cycle(node: int) -> bool:
#             # Если встретили узел, который сейчас находится в текущем пути DFS — найден цикл
#             if state[node] == 1:
#                 return True
#             # Если узел уже полностью проверен и безопасен, пропускаем его
#             if state[node] == 2:
#                 return False
            
#             # Помечаем узел как находящийся в процессе обхода
#             state[node] = 1
            
#             # Проверяем все курсы, для которых текущий является пререквизитом
#             for neighbor in graph[node]:
#                 if has_cycle(neighbor):
#                     return True
            
#             # Помечаем узел как полностью проверенный и безопасный
#             state[node] = 2
#             return False
        
#         # 2. Проверяем каждый курс на наличие циклов
#         for course in range(numCourses):
#             if state[course] == 0:
#                 if has_cycle(course):
#                     return False  # Если обнаружен цикл, закончить обучение невозможно
                    
#         return True



# 417



# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         if not heights or not heights[0]:
#             return []
        
#         rows, cols = len(heights), len(heights[0])
#         pac = set()  # Достижимые из Тихого океана
#         atl = set()  # Достижимые из Атлантического океана
        
#         def dfs(r: int, c: int, visited: set, prev_height: int):
#             # Базовые проверки на выход за границы, повторное посещение
#             # и возможность течь "вверх" (высота соседа должна быть >= prev_height)
#             if (r < 0 or r >= rows or 
#                 c < 0 or c >= cols or 
#                 (r, c) in visited or 
#                 heights[r][c] < prev_height):
#                 return
            
#             visited.add((r, c))
            
#             # Рекурсивно проверяем четырех соседей
#             dfs(r + 1, c, visited, heights[r][c])
#             dfs(r - 1, c, visited, heights[r][c])
#             dfs(r, c + 1, visited, heights[r][c])
#             dfs(r, c - 1, visited, heights[r][c])
            
#         # 1. Запуск от верхней и нижней границ (горизонтальные линии)
#         for c in range(cols):
#             dfs(0, c, pac, heights[0][c])               # Верхняя граница (Тихий)
#             dfs(rows - 1, c, atl, heights[rows - 1][c]) # Нижняя граница (Атлантика)
            
#         # 2. Запуск от левой и правой границ (вертикальные линии)
#         for r in range(rows):
#             dfs(r, 0, pac, heights[r][0])               # Левая граница (Тихий)
#             dfs(r, cols - 1, atl, heights[r][cols - 1]) # Правая граница (Атлантика)
            
#         # Находим пересечение множеств — общие ячейки для обоих океанов
#         result = [list(cell) for cell in pac.intersection(atl)]
#         return result
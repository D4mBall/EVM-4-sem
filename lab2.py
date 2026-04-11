#20


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         good_or_not = True
#         for i in s:
#             if i in '({[':
#                 stack.append(i)
#             elif i in ')}]':
#                 if not stack:
#                     good_or_not = False
#                     break
#                 breaker = stack.pop()
#                 if breaker == '(' and i == ')':
#                     continue
#                 elif breaker == '{' and i == '}':
#                     continue
#                 elif breaker == '[' and i == ']':
#                     continue
#                 else:
#                     good_or_not = False
#         if len(stack) != 0:
#             good_or_not = False

#         return good_or_not
                
        
#150

# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

# stack = []

# for i in tokens:
#     if i not in '+-*/':
#         stack.append(int(i))
#     else:
#         chis_2 = int(stack.pop())
#         chis_1 = int(stack.pop())
#         if i == '+':
#             stack.append(chis_1 + chis_2)
#         if i == '-':
#             stack.append(chis_1 - chis_2)
#         if i == '*':
#             stack.append(chis_1 * chis_2)
#         if i == '/':
#             stack.append(int(chis_1 / chis_2))
# print(stack[0])



#22

# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         res = []
#         stack = [("", 0, 0)]
        
#         while stack:
#             current_str, opened, closed = stack.pop()
#             if opened == n and closed == n:
#                 res.append(current_str)
#                 continue
#             if opened < n:
#                 stack.append((current_str + "(", opened + 1, closed))
#             if closed < opened:
#                 stack.append((current_str + ")", opened, closed + 1))
                
#         return res


#232

# class MyQueue:

#     def __init__(self):
#         self.stack_in = []
#         self.stack_out = []

#     def push(self, x: int) -> None:
#         self.stack_in.append(x)

#     def pop(self) -> int:
#         self.peek()
#         return self.stack_out.pop()

#     def peek(self) -> int:
#         if not self.stack_out:
#             while self.stack_in:
#                 self.stack_out.append(self.stack_in.pop())
#         return self.stack_out[-1]

#     def empty(self) -> bool:
#         return not self.stack_in and not self.stack_out


# # Пример использования:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()


#622


# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.queue = [0] * k
#         self.head = 0
#         self.count = 0
#         self.capacity = k

#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         tail_index = (self.head + self.count) % self.capacity
#         self.queue[tail_index] = value
#         self.count += 1
#         return True

#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.head = (self.head + 1) % self.capacity
#         self.count -= 1
#         return True

#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.head]

#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         tail_index = (self.head + self.count - 1) % self.capacity
#         return self.queue[tail_index]

#     def isEmpty(self) -> bool:
#         return self.count == 0

#     def isFull(self) -> bool:
#         return self.count == self.capacity


# # Пример использования:
# # obj = MyCircularQueue(k)
# # param_1 = obj.enQueue(value)
# # param_2 = obj.deQueue()
# # param_3 = obj.Front()
# # param_4 = obj.Rear()
# # param_5 = obj.isEmpty()
# # param_6 = obj.isFull()
        

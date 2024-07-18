def solution(s):
    answer = True
    
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack
    
# 2차시       
#     stack = []
    
#     for e in s:
#         if e == "(":
#             stack.append(e)
#         elif stack and e == ")":
#             stack.pop()
    
#     if not stack: # 스택이 비었다면
#         return True
#     else:
#         return False
    
    
    
# 1차시
#     left = 0
#     right = 0
#     last  = True
    
    
#     for e in s:
#         # stack.append(e)
#         if e == "(":
#             left += 1
#         elif e == ")":
#             right += 1
            
#     if s[-1] == ")":
#         last = True
#     elif s[-1] == "(":
#         last = False
            
    
    
    
#     if left ==  right and last:
#         return True
        
    return False
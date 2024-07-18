def solution(n):
    
#     def fibo(n):
#         if n <= 1:
#             return n
#         return (fibo(n-2) + fibo(n-1))% 1234567
    
#     return fibo(n)

    arr = [0, 1]
    
    for i in range(2, n+1):
        arr.append((arr[i-2] + arr[i-1])%1234567)

    return arr[-1]
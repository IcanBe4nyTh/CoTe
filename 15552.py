import sys

T = int(input())

# for i in range (0,T):
#     A,B= sys.stdin.readline().strip().split(' ')
#     A=int(A)
#     B=int(B)
#     result = A+B
#     print(result)
i=0
while i<T:
    A, B = sys.stdin.readline().strip().split(' ')
    A = int(A)
    B = int(B)
    result = A + B
    print(result)
    i+=1
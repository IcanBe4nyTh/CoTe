import sys
N=int(input())
stack = []

for i in range(0,N):
    order1=sys.stdin.readline().strip()
    order = order1.split(' ')[0]
    if order == 'push' :
        num = int(order1.split(' ')[1])
        stack.append(num)
    elif order == 'pop':
        if len(stack)==0:
            print(-1)
        else :
            print(stack[-1])
            stack.pop()
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack)>=1:
            print(0)
        else : print(1)
    else :
        if len(stack)==0:
            print(-1)
        else : print(stack[-1])

"""
order1에 input()을 넣으니까 시간초과가 나왔길래 sys를 써보았다
sys공부해봐야겠
"""

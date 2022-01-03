import sys

K = int(input())
stack =[]
for i in range(0,K):
    num=int(sys.stdin.readline().strip())
    if num == 0 :
        stack.pop()
    else :
        stack.append(num)
sum=0
length=len(stack)
for j in range(0,length) :
    sum+=stack[j]

print(sum)
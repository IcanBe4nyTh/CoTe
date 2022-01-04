import sys

def check_vps(stack):
    length = len(stack)
    if length == 0:
        print("YES")
    elif stack[0] == ")":
        print("NO")
    else:
        for i in range(0, length):
            if stack[i] == "(" and stack[i + 1] == ")":
                stack.pop(i)
                stack.pop(i)
                check_vps(stack)
                break

T=int(input())

for i in range(0,T):
    VPS=sys.stdin.readline().strip()
    stack = [j for j in VPS]
    cnt_1 = stack.count('(')
    cnt_2 = stack.count(')')
    if len(stack)%2 != 0 :
        print("NO")
    elif cnt_1 != cnt_2 :
        print("NO")
    else :
        check_vps(stack)


"""
check_vps의 else부분을 구현하는게 좀 오래걸렸다...
break를 쓰지 않았을땐 계속 out of index가 떠서 elif 추가해서 예외처리하고 break를 넣어 for문을 탈출하게 하니까 해결이 되었다
근데 좀 찜찜한 느낌
왜냐면 재귀와 break를 적절하지 않게 쓴거 같다
좀 시간이 오래걸리는 느낌?
다시 한번더 고민을 해봐야겠다.

"""










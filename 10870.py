def Fibonacci(num):
    if num==0 :
        return 0
    elif num==1 :
        return 1
    else :
        a = Fibonacci(num-2)+Fibonacci(num-1)
        return a

if __name__ == "__main__":

    num=int(input())
    print(Fibonacci(num))
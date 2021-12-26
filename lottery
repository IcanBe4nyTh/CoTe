"""
2021 Dev-Matching: 웹 백엔드 개발자(상반기) 1. 로또의 최고 순위와 최저 순위
"""

def checking_goals(a):
    if a==6:        goals=1
    elif a==5:        goals=2
    elif a==4:  goals=3
    elif a==3:  goals=4
    elif a==2:  goals=5
    else :      goals=6
    return goals

def solution(lottos, win_nums):
    cnt=0
    best=0
    worst=0
    draw =0
    for n in range (len(lottos)):
        for j in range (len(lottos)):
            if win_nums[n] == lottos[j] :
                cnt+=1
            j+=1
        n+=1

    draw=lottos.count(0)

    best=checking_goals(cnt+draw)
    worst=checking_goals(cnt)


    answer = [best,worst]
    return answer

"""
2중 for문으로 풀었는데
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
이렇게 깔끔하게 푸는 방법이 있었네...
리뷰하면서 다시 봐야겠다
###


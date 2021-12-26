"""
2021 Dev-Matching: 웹 백엔드 개발자(상반기) 2. 행렬 테두리 회전하기 
"""
col=100
row=97
queries =[[1,1,100,97]]


def solution(rows, columns, queries):
    answer = []
    
    table = [[0 for col in range(columns)] for row in range(rows)]
    item = 1
    for i in range(rows):
        for j in range(columns):
            table[i][j] = item
            item += 1

    for a, b, c, d in queries:
        x_1 = a - 1
        y_1 = b - 1
        x_2 = c - 1
        y_2 = d - 1
        print(table[x_1][y_1])
        temp1 = table[x_1 + 1][y_1]
        temp2 = table[x_1][y_2]
        temp3 = table[x_2][y_2]
        temp4 = table[x_2][y_1]
        mini = temp1

        for i in range(y_2, y_1, -1):
            ckt = table[x_1][i - 1]
            table[x_1][i] = ckt
            mini = min(ckt, mini)
        table[x_1][y_1] = temp1
        for i in range(x_2, x_1, -1):
            ckt = table[i - 1][y_2]
            table[i][y_2] = ckt
            mini = min(ckt, mini)
        table[x_1 + 1][y_2] = temp2
        for i in range(y_1, y_2):
            ckt = table[x_2][i + 1]
            table[x_2][i] = ckt
            mini = min(ckt, mini)
        table[x_2][y_2 - 1] = temp3
        for i in range(x_1, x_2):
            ckt = table[i + 1][y_1]
            table[i][y_1] = ckt
            mini = min(ckt, mini)
        table[x_2 - 1][y_1] = temp4

        answer.append(mini)

    return answer

print(solution(row,col,queries))


"""
처음 테스트하는건 맞는데 검사하면 통과가 안되네
temp1,2,3,4,주는 방식이 잘못된듯함 3번째에서 뭔가 잘못된듯함 temp3가 out of range

"""


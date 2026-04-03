def solution(n, arr1, arr2):
    answer = []
    barr1 = [[] for _ in range(n)]
    barr2 = [[] for _ in range(n)]
    
    # 바이너리 2차원 배열로 변환
    for i in range(n):
        barr1[i] = list(map(int, format(arr1[i], f'0{n}b')))
        barr2[i] = list(map(int, format(arr2[i], f'0{n}b')))
    
    for i in range(n):
        a = ""
        for j in range(n):
            if barr1[i][j] == 1 or barr2[i][j] == 1:
                a += "#"
            elif barr1[i][j] == 0 and barr2[i][j] == 0:
                a += " "
        answer.append(a)
    
    return answer
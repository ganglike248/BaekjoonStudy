def solution(N, stages):
    answer = []
    result = []
    players = len(stages)
    
    for i in range(1, N + 1):
        if players == 0:
            result.append((i, 0))
            continue
        # 클리어하지 못 한 사용자 수
        c = stages.count(i)
        # 실패율
        r = c / players
        # 추가
        result.append((i, r))
        # 사용자 제거
        players -= c
    
    # 실패율로 정렬
    result.sort(key=lambda x: -x[1])
    
    answer = [x[0] for x in result]
    
    return answer
def solution(dartResult):
    scores = []
    
    dartResult = dartResult.replace('10', 'k')
    
    for i in dartResult:
        if i.isdigit():
            scores.append(int(i))
        elif i == 'k':
            scores.append(10)
        elif i == "S":
            scores[-1] = scores[-1] ** 1
        elif i == "D":
            scores[-1] = scores[-1] ** 2
        elif i == "T":
            scores[-1] = scores[-1] ** 3
        elif i == "*":
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
        elif i == "#":
            scores[-1] = scores[-1] * -1
    
    return sum(scores)
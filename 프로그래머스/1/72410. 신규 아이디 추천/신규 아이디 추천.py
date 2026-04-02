def solution(new_id):
    answer = ''
    
    # 1단계
    answer = new_id.lower()
    
    # 2단계
    temp = ""
    
    for ch in answer:
        if ch.islower() or ch.isdigit() or ch in "-_.":
            temp += ch
    
    answer = temp
    temp = ""
    
    # 3단계
    while (".." in answer):
        answer = answer.replace("..", ".")
    
    # 4단계
    answer = answer.strip(".")

    # 5단계
    if answer == "":
        answer += "a"
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.strip(".")
    
    # 7단계
    if len(answer) <= 2:
        while len(answer) <= 2:
            answer += answer[-1]
    
    return answer
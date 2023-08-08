# https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    deploy_cnt = 0
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses:
            if progresses[0] < 100: 
                break
            else:
                progresses.pop(0)
                speeds.pop(0)
                deploy_cnt += 1
        if deploy_cnt != 0:
            answer.append(deploy_cnt)
            deploy_cnt = 0
    return answer

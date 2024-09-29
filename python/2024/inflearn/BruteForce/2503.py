
def soluition(gameCnt: int) -> bool:
    result = 0
    hint = [list(map(int, input().split())) for _ in range(gameCnt)]
    
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                if a == b == c or a == b or a == c or b == c:
                    continue
                
                cnt = 0
                for arr in hint:
                    number = arr[0]
                    strike = arr[1]
                    ball = arr[2]

                    strikeCnt = 0
                    ballCnt = 0
                    
                    checkA = number // 100
                    checkB = (number % 100) // 10
                    checkC = number % 10
                    
                    if checkA == a:
                        strikeCnt += 1
                    if checkB == b:
                        strikeCnt += 1
                    if checkC == c:
                        strikeCnt += 1
                    
                    if checkA == b or checkA == c:
                        ballCnt += 1
                    if checkB == a or checkB == c:
                        ballCnt += 1
                    if checkC == a or checkC == b:
                        ballCnt += 1
                    
                    if ballCnt == ball and strikeCnt == strike:
                        cnt += 1

                if cnt == gameCnt:
                    result += 1
    
    return result
    
def main():
    gameCnt = int(input())
    
    result = soluition(gameCnt)
    
    print(result)
    
main()
    
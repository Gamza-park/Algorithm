
def soluition(candyNum: int) -> bool:
    result = 0
    
    if candyNum >= 5:
        for cntA in range(1, candyNum - 1):
            for cntB in range(1, candyNum - 1):
                for cntC in range(1, candyNum - 1):
                    totalCandyNum = cntA + cntB + cntC
                    
                    if totalCandyNum == candyNum:
                        if cntA + 2 <= cntB and cntC % 2 == 0:
                            result += 1
                    
                    if totalCandyNum > candyNum:
                        break
        
    return result            
            
    

def main():
    candyNum = int(input())
    
    result = soluition(candyNum)
    
    print(result)
    
    return 0
    
    
main()
    
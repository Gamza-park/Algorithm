
def soluition(password: int) -> bool:
    
    for i in range(2, 10 ** 6 + 1):
        if password % i == 0:
            return False
        
    return True
    

def main():
    cnt = int(input())
    
    for _ in range(cnt):
        
        password = int(input())
        
        isTrue = soluition(password)
        
        if isTrue:
            print("YES")
        else:
            print("NO")
            
    return 0
    
    
main()
    
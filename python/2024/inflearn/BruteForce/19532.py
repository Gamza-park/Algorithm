
def soluition(a: int, b: int, c: int, d: int, e: int, f: int) -> bool:
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
                print(x, y)
                return
            
    

def main():
    a, b, c, d, e, f = map(int, input().split())
    
    soluition(a, b, c, d, e, f)
    
main()
    
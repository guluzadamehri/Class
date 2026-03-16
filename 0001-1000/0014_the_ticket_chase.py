import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    data = sys.stdin.read().split()
    if len(data) < 2:
        return
    
    n = int(data[0])
    p_ticket = int(data[1])
    
    found = False
    for i in range(1, n):
        current_ticket = p_ticket + i
        if is_prime(current_ticket):
            print(i - 1)
            found = True
            break
            
    if not found:
        print("-1")

solve()

import sys
sys.setrecursionlimit(10**7)

def solve():
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        n = int(sys.stdin.readline())
        used = [False] * (n + 1)
        p = []

        def dfs(pos):
            if pos == n:
                return True
            
            prev = p[-1]
            i = pos  
            
            for x in range(1, n + 1):
                if not used[x] and abs(prev - x) % i == 0:
                    used[x] = True
                    p.append(x)
                    if dfs(pos + 1):
                        return True
                    p.pop()
                    used[x] = False
            return False

        
        for start in range(1, n + 1):
            used = [False] * (n + 1)
            p = [start]
            used[start] = True
            if dfs(1):
                print(*p)
                break

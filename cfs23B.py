import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n
        
        orig = 0
        for i in range(1, n):
            orig += abs(a[i] - a[i-1])
        
        best = orig 
        
      
        best = min(best, orig - abs(a[1] - a[0]))
      
        best = min(best, orig - abs(a[-1] - a[-2]))
        
        
        for i in range(1, n-1):
            val = orig - abs(a[i] - a[i-1]) - abs(a[i+1] - a[i]) + abs(a[i+1] - a[i-1])
            best = min(best, val)
        
        out.append(str(best))
    
    print("\n".join(out))

if __name__ == "__main__":
    solve()
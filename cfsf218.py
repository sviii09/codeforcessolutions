import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx + n])); idx += n
        
        if n == 1:
            results.append("Alice")
            continue
        
        min_val = min(arr)
        if min_val > 1:
            results.append("Bob")
        else:
            # min_val == 1
            ones = arr.count(1)
            if ones % 2 == 1:
                results.append("Alice")
            else:
                results.append("Bob")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
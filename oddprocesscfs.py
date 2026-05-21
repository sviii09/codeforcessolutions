import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    out_lines = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n
        
        a.sort(reverse=True)
        
        prefix_sum = [0]*(n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + a[i]
        
        # Precompute suffix max even and odd
        suffix_even = [-10**18]*(n+2)
        suffix_odd = [-10**18]*(n+2)
        for i in range(n-1, -1, -1):
            suffix_even[i] = suffix_even[i+1]
            suffix_odd[i] = suffix_odd[i+1]
            if a[i] % 2 == 0:
                suffix_even[i] = max(suffix_even[i], a[i])
            else:
                suffix_odd[i] = max(suffix_odd[i], a[i])
        
        ans = []
        min_odd_in_prefix = 10**18
        min_even_in_prefix = 10**18
        
        for k in range(1, n+1):
            total = prefix_sum[k]
            if total % 2 == 1:
                ans.append(total)
            else:
                # Need to adjust parity
                best = -1
                # Remove smallest odd from first k, add largest even from rest
                if min_odd_in_prefix < 10**18 and suffix_even[k] > -10**18:
                    best = max(best, total - min_odd_in_prefix + suffix_even[k])
                # Remove smallest even from first k, add largest odd from rest
                if min_even_in_prefix < 10**18 and suffix_odd[k] > -10**18:
                    best = max(best, total - min_even_in_prefix + suffix_odd[k])
                ans.append(max(0, best))
            
            # Update min odd/even in prefix
            if a[k-1] % 2 == 1:
                min_odd_in_prefix = min(min_odd_in_prefix, a[k-1])
            else:
                min_even_in_prefix = min(min_even_in_prefix, a[k-1])
        
        out_lines.append(' '.join(map(str, ans)))
    
    print('\n'.join(out_lines))

if __name__ == "__main__":
    solve()
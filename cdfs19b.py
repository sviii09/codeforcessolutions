def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        
        s = arr[0]  # first step, s = a1
        
        for i in range(1, n):
            # Compare ai + s vs s + ai
            option1 = arr[i] + s
            option2 = s + arr[i]
            if option1 < option2:
                s = option1
            else:
                s = option2
        
        print(s)

if __name__ == "__main__":
    solve()
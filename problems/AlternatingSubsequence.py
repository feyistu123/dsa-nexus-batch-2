def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    
    i = 0
    while i < n:
        curr_max = a[i]
        j = i + 1
        while j < n and (a[j] > 0) == (a[i] > 0):
            curr_max = max(curr_max, a[j])
            j += 1
        
        ans += curr_max
        i = j
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()


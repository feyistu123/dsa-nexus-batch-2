def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = []
    i = 0  # Pointer for array a

    for num in b:
        count = 0
        while i < n and a[i] < num:
            count += 1
            i += 1
        result.append(count)
    
    print(*result)

solve()


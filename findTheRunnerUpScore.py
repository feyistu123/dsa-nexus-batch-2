if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    array = list(set(arr))
    array.sort()
    print(array[len(array)-2])

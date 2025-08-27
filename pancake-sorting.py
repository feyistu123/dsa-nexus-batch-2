def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)
        for i in range(n, 0, -1):
            index = arr.index(i)
            if index != i - 1:
                if index != 0:
                    flips.append(index + 1)
                    arr[:index + 1] = reversed(arr[:index + 1])
                flips.append(i)
                arr[:i] = reversed(arr[:i])
        return flips

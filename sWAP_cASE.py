def swap_case(s):
    result = ""
    for char in s:
        if "a" <= char <= "z":
            result += char.upper()
        elif "A" <= char <= "Z":
            result += char.lower()
        else:
            result += char
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

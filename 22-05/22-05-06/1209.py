def removeDuplicates(s: str, k: int) -> str:
    stack = []
    for item in s:
        if stack and stack[-1][0] == item:
            stack[-1][1] += 1
        else:
            stack.append([item, 1])
        if stack and stack[-1][1] == k:
            stack.pop(-1)
    new_string = ""
    while stack:
        item = stack.pop(-1)
        while item[1] > 0:
            new_string += item[0]
            item[1] -= 1
    return new_string[::-1]


print(removeDuplicates("deeedbbcccbdaa", 3))

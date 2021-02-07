def shortestToChar(s, c):
    indices = []
    solution = [0 for i in range(len(s))]
    for i in range(len(s)):
        if s[i] == c:
            indices.append(i)
    indices_ptr = 0
    for i in range(len(solution)):
        if len(indices) == 1:
            solution[i] = abs(i - indices[0])
            continue
        if i == indices[indices_ptr]:
            if indices_ptr == len(indices) - 1:
                continue
            else:
                indices_ptr += 1
                continue
        if indices_ptr == len(indices) - 1:
            a= abs(indices[indices_ptr] - i)
            b = abs(indices[indices_ptr - 1] - i)
            solution[i] = min(a, b)
        else:
            a = abs(indices[indices_ptr] - i)
            b = abs(indices[indices_ptr - 1] - i)
            c = abs(indices[indices_ptr + 1] - i)
            solution[i] = min(a, b ,c)
    return solution

print(shortestToChar('cizokxcijwbyspcfcqws', 'c'))
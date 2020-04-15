def fib(n):
    li = [0, 1]
    if n == 1:
        return [0]
    elif n == 2:
        return li
    else:
        for i in range(2, n):
            li.append(li[i-2]+li[i-1])
    return li

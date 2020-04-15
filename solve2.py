def solve2(a, b, c):
    d = (b**2 - 4*a*c)**(1/2)
    if (a == 0) & (b == 0) & (c != 0):
        return None
    elif a == 0:
        return -c/b
    else:
        return (-b+d)/(2*a), (-b-d)/(2*a)

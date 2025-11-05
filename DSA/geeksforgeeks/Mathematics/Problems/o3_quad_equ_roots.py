from math import sqrt

def quadratic_roots(a: int, b: int, c: int):
    roots = []
    D = b*b - 4*a*c
    if D < 0:
        roots.append(-1)
    else:
        root1 = -b + sqrt(D)/2*a
        root2 = -b - sqrt(D)/2*a
        roots.append(max(root1,root2))
        roots.append(min(root1,root2))
    return roots



if __name__ == "__main__":
    print("result 1:", quadratic_roots(2,8,8))
    print("result 1:", quadratic_roots(1,-7,12))
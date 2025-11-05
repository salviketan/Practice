def mod_inverse(a, m):
    for i in range(m):
        if ((a * i) % m) == 1:
            return i
    return -1



if __name__ == "__main__":
    print(mod_inverse(10, 17))
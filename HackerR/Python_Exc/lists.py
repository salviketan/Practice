def exec_cmd(my_arr, cmd, args):
    if cmd == "append":
        my_arr.append(args[0])
    if cmd == "print":
        print(my_arr)
    if cmd == "remove":
        my_arr.remove(args[0])
    if cmd == "insert":
        my_arr.insert(args[0], args[1])
    if cmd == "sort":
        my_arr.sort()
    if cmd == "pop":
        my_arr.pop()
    if cmd == "reverse":
        my_arr.reverse()


if __name__ == '__main__':
    N = int(input())
    my_arr = []
    for _ in range(N):
        cmd, *args = input().split()
        args = list(map(int, args))
        exec_cmd(my_arr, cmd, args)         
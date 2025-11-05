def find_runner_up(arr):
    scr_list = sorted(set(arr))
    return scr_list[-2]


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    positon_2nd = find_runner_up(arr)
    print(positon_2nd)
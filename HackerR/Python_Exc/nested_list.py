def second_lowest(score_arr):
    second_score = sorted(set(i[1] for i in score_arr))[1]

    for student in sorted(score_arr):
        if student[1] == second_score:
            print(student[0])


if __name__ == '__main__':
    # score_list = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     score_list.append([name,score])

    score_list = [['Harry', 37.21], ['Tina', 37.2], ['Harsh', 39], ['Akriti', 41], ['Berry', 37.21]]

    second_lowest(score_list)
def student_percentage(data, query):
    averge = sum(data[query])/len(data[query])
    return "%.2f"%averge


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    perc = student_percentage(student_marks, query_name)
    print(perc)
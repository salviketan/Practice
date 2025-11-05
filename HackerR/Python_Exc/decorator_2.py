import operator

def person_lister(f):
    def inner(people):
        sort_ppl = sorted(people, key= operator.itemgetter(2))
        return [f(person) for person in sort_ppl]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    # people = [
    #             ['Mike','Thomas',20,'M'],
    #             ['Robert','Bustle',32,'M'],
    #             ['Andrea','Bustle',30,'F'],
    #             ['John','Doe',32,'M']
    #         ]

    print(*name_format(people), sep='\n')
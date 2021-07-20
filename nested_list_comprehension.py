if __name__ == '__main__':
    records = []

    for _ in range(int(input("Number of students:\n"))):
        name = input("Student's name:\n")
        score = float(input("Student's score:\n"))
        # storing all the names and scores in the records list
        records.append([score, name])
    # sorting records list by the score (since it's first)
    records.sort()
    # remove all instances of the lowest score from records list (it will be the first value taken from the sorted list)
    no_min = [i for i in records if i[0] != records[0][0]]
    # trim down list b to only those scores that are equal to that second-lowest overall score.
    final_list = [j for j in no_min if j[0] == no_min[0][0]]

    final_list.sort(key=lambda x: x[1])
    print("Student(s) with the lowest scores are:")
    for i in range(len(final_list)):
        print("{}".format(final_list[i][1]))

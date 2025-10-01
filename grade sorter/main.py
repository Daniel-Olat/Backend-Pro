# lists that take in students names and scores and prints the names in order and then filters out failed students

names = ["alice" , "kareem" , "john" , "Dara" , "Kareem" , "Eunice" , "Daniel" ,"Christian"]
scores = [10, 56, 76, 80 , 64, 45 , 47, 89] # this list contains integers

# Function expects scores first, then names
def sort_students(scores, names):
    print('Here is a sorted list of students! ')
    def passed_scores(score):
        return score >= 50
    passed_student_scores = list(filter(passed_scores, scores))
    for student_score in passed_student_scores:
        if student_score in scores:
            index = scores.index(student_score)
            print(names[index], " => ", student_score)

# Call with scores first, then names
sort_students(scores, names)
#
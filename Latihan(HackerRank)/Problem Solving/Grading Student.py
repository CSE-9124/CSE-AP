# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/grading/problem
# Difficulty: Easy

# ======================== Solution ========================

def gradingStudents(grades):
    final_grade = []
    for i in grades:
        if i < 38 :
            final_grade.append(i)

        elif i % 5 <= 2:
            final_grade.append(i)
        
        else:
            tmp = (i // 5 + 1) * 5
            final_grade.append(tmp)

    return final_grade

grades_count = int(input().strip())

grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)
print('\n'.join(map(str, result)))


# ======================== Test Case ========================
grades_count = 4
grades = [73, 67, 38, 33]
result = gradingStudents(grades)
print('\n'.join(map(str, result)))
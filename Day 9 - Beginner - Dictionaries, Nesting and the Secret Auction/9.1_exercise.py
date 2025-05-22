# Instructions

# Write a program that converts their scores to grades. By the end
# of your program, you should have a new dictionary called student_grades
# that should contain student names for keys and their grades for values.
# The final version of the student_grades dictionary will be checked.
#
# DO NOT write any print statements.

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    if 100 >= student_scores[student] >= 91:
        value = "Outstanding"
    elif 90 >= student_scores[student] >= 81:
        value = "Exceeded Expectations"
    elif 80 >= student_scores[student] >= 71:
        value = "Acceptable"
    else:
        value = "Failed"

    student_grades[student] = value


# 🚨 Don't change the code below 👇
print(student_grades)






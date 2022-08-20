# The keys in student_scores are the names of the students and the values are
# their exam scores. This is a program that converts their scores to grades.
# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}


for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grades[key] = 'Outstanding'
    elif score > 80:
        student_grades[key] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'

print(student_grades)

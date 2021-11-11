# Student Management System
# Run Data Analysis on student Marks
# Find highest scorer in a subject and highest marks ?

# sample input
# students name: Chandan, Bharath, Virat

student_1 = {
    "Maths": 45,
    "Social": 75,
    "Science": 96,
    "name": "Chandan"
}
student_2 = {
    "Maths": 74,
    "Social": 83,
    "Science": 100,
    "name": "Bharath"
}
student_3 = {
    "Maths": 98,
    "Social": 62,
    "Science": 23,
    "name": "Virat"
}
student_list = [student_1,student_2,student_3]
highest_score_in_Maths = 0
highest_score_in_Maths_name = ''
for student in student_list:
    if(student.get("Maths")>highest_score_in_Maths):
        highest_score_in_Maths = student.get("Maths")
        highest_score_in_Maths_name = student.get("name")
print(f"The highest scorer in Maths is {highest_score_in_Maths} by {highest_score_in_Maths_name}")




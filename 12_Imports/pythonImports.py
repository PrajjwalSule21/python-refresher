"""
Modules got used all the time throughout programming

It helps with creating more files, with unique purposes, to help with clean maintainable code.
"""

homework_assignment_grade = {
    "homework_1": 85,
    "homework_2": 100,
    "homework_3": 81
}


from grade_average_service import  calculate_homework


calculate_homework(homework_assignment_grade)
def calculate_homework(homework_assignment_arg):
    sum_of_grades = 0
    for homework in homework_assignment_arg.values():
        sum_of_grades = sum_of_grades + homework

    final_grades = round(sum_of_grades / len(homework_assignment_arg), 2)

    print(final_grades)
# Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are contained in a CSV file. The contents of the file follow this format:

# id;e1;e2;e3
# 12345678;4;1;4
# 12345687;3;5;3
# 12345699;10;2;2
# In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a total of 9 points.

# The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student.

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# pekka peloton 0
# jaana javanainen 1
# liisa virtanen 3

# Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc. Completing all 40 exercises awards 10 points. The number of points awarded is always an integer number.



Student_info = input("Student information: ")
exercise_done = input("Exercises completed: ")
exam_point = input("Exam points: ")

students = {}
with open(Student_info) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        id = parts[0]
        name = parts[1] + " " +  parts[-1]

        students[id] = name

exercises = {}
with open(exercise_done) as new_file:
    for line in new_file:
        total_exercise = 0
        parts = line.strip().split(";")

        if parts[0] == "id":
            continue
        id = parts[0]

        for exercise in parts[1:]:
            total_exercise += int(exercise)

        exercise_points = (total_exercise * 10) // 40
        exercises[id] = exercise_points



exam_pt = {}
with open(exam_point) as new_file:
    for line in new_file:
        parts = line.strip().split(";")

        if parts[0] == "id":
            continue
        id = parts[0]

        total_point = 0
        for point in parts[1:]:
            total_point += int(point)

        exam_pt[id] = total_point

for id in students:
    final = exam_pt[id] + exercises[id]

    if final < 15:
        grade = 0
    elif final <= 17:
        grade = 1
    elif final <= 20:
        grade = 2
    elif final <= 23:
        grade = 3
    elif final <= 27:
        grade = 4
    else:
        grade = 5

    print(students[id], grade)




    

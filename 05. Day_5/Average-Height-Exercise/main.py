student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


add_height = 0
student_count = 0
for student in student_heights:
    add_height += student
    student_count += 1

average_height = round(add_height/ student_count)
print(average_height)
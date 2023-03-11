student_height = input("Input a list of student height ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

# don't use sum() and len() another way find please 

# total_height = sum(student_height)
# number_of_students = len(student_height)
# average_height = round(total_height / number_of_students)
# print(average_height)

#use another way to calculate
total_height = 0
for height in student_height:
    total_height += height
# print(total_height)


number_of_students = 0
for student in student_height:
    number_of_students += 1
# print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)

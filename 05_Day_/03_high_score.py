print("high score in the class")

student_score = input("Input a list of student score ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

#don't use max function and min

heighest_score = 0
for score in student_score:
    if score > heighest_score:
        heighest_score = score
print(f"The highest score in the class is: {heighest_score}")

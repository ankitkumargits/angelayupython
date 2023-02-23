print("It's your time to control the emotion")

height = float(input("Enter your height in m."))
weight = float(input("Enter your weight in kg."))

bmi = round(weight / height * height)   # height * height = height ** 2

if(bmi < 18.5):
    print(f"Your bmi is {bmi} and you are underweight.")
elif (bmi < 25):
        print(f"Your bmi is {bmi} and you are normal weight.")
elif (bmi < 30):
    print(f"Your bmi is {bmi} and you are overweight.")
elif (bmi < 35):
    print(f"Your bmi is {bmi} and you are obese.")
else:
        print(f"Your bmi is {bmi} and you are clinically obese.")
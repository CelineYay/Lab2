print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight/(height**2)
    print("BMI = " + str(BMI) + "\n")
    if (BMI<18.5):
        print("Under weight")
    elif (BMI>25):
        print("over weight")
    else:
        print("Normal weight")

#calculate_bmi(weight="57", height="1.73")

calculate_bmi(1.73,57)
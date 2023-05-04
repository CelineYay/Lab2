print("\nBMI")


def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight / (height ** 2)
    print("BMI = " + str(BMI) + "\n")
    if BMI < 18.5:
        print(-1) #under
    elif BMI > 25:
        print(1) #over
    else:
        print(0) #normal


# calculate_bmi(weight="57", height="1.73")
calculate_bmi(1.73, 57)
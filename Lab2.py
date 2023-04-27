print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python \n")


# Part 2
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32")


def calc_average(t):
    tt = 0
    for i in range(len(t)):
        tt += t[i]
    return float(tt / len(t))


def get_user_input():
    n = input("Enter data: ")
    f = n.split(",")
    t = [float(x) for x in f]
    return t


def find_min_max(t):
    sort_temperature(t)
    return [float(t[0]), float(t[len(t) - 1])]


def sort_temperature(t):
    t.sort()


# def calc_median_temperature(t):


display_main_menu()
t = get_user_input()
print("average = " + str(calc_average(t)))
print("min , max = " + str(find_min_max(t)))


# Part 1
print("\nBMI")
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight / (height ** 2)
    print("BMI = " + str(BMI) + "\n")
    if BMI < 18.5:
        print("Under weight")
    elif BMI > 25:
        print("over weight")
    else:
        print("Normal weight")


# calculate_bmi(weight="57", height="1.73")
calculate_bmi(1.73, 57)

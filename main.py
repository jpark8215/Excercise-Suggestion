from basic import exercise_suggestions


def main():
    print("Welcome to Exercise Suggestions Generator")
    height = float(input("Please enter your height in centimeters: "))
    weight = float(input("Please enter your weight in kilograms: "))
    time = float(input("Please enter the amount of time you have for exercise in minutes: "))
    exercise_suggestions(height, weight, time)


if __name__ == "__main__":
    main()




def exercise_suggestions(height, weight, time):
    bmi = weight / (height/100)**2
    if bmi < 18.5:
        print("You are underweight. You should consider doing strength training exercises to build muscle and increase your weight.")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("You have a healthy weight. You should consider doing a mix of cardiovascular and strength training exercises to maintain your weight and improve overall fitness.")
    else:
        print("You are overweight. You should consider doing cardiovascular exercises such as running, cycling, or swimming to burn calories and lose weight.")
    if time < 30:
        print("Since you have limited time, you should focus on high-intensity interval training (HIIT) exercises to maximize the benefits in a short amount of time.")
    elif time >= 30 and time <= 60:
        print("You have a moderate amount of time to exercise. You can do a combination of HIIT and longer endurance exercises such as jogging or cycling.")
    else:
        print("You have a good amount of time to exercise. You can spend more time doing longer endurance exercises or split your time between HIIT and endurance exercises.")

# Example usage
# exercise_suggestions(173, 75, 45)
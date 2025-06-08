def recommend_diet(age, weight, goal, activity_level):
    if goal == "Lose Weight":
        return [
            "Morning: Oatmeal + Green Tea",
            "Lunch: Grilled veggies + Brown rice",
            "Dinner: Salad + Boiled Egg",
            "Snacks: Fruits, Nuts"
        ]
    elif goal == "Gain Weight":
        return [
            "Morning: Banana shake + Eggs",
            "Lunch: Chicken + Rice",
            "Dinner: Paneer/Tofu + Roti",
            "Snacks: Dry fruits, Cheese toast"
        ]
    else:  # Maintain
        return [
            "Morning: Milk + Toast",
            "Lunch: Dal + Roti + Veggies",
            "Dinner: Light soup + Rice",
            "Snacks: Fruits, Yogurt"
        ]

def recommend_exercise(goal, activity_level):
    if goal == "Lose Weight":
        return ["30 min Cardio", "15 min Strength Training", "Stretching"]
    elif goal == "Gain Weight":
        return ["Weight Lifting", "Protein-rich post-workout meal"]
    else:
        return ["Daily Walk", "Yoga or Light Exercise"]
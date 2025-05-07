import random

def filter_recipes(user_input, recipes):
    return [
        r for r in recipes 
        if r['difficulty'] == user_input['preference']
        and not any(a in r['ingredients'] for a in user_input['allergies'])
        and user_input['mood'] in r['moods']
    ]

def get_daily_meal_plan(user_input, recipes):
    filtered = filter_recipes(user_input, recipes)
    return random.sample(filtered, min(len(filtered), 3))

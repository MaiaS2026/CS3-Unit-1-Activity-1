# DEFINE YOUR FUNCTIONS HERE!
# PART A
def about_me():
    print("My name is Maia.")
    print("I'm a senior in high school.")
    print("I go to the Birch Wathen Lenox School")

def weather():
    print("Today is Monday, September 15th.")
    print("The high in NYC is 80 degress Farenheit.")
    print("There will be sunny skies all day.")

# PART B
def feeling(mood, overall_happiness):
    print(f"What mood are your in? {mood}")
    print(f"How happy are you on a scale of 1-10? {overall_happiness}")

# PART C
def make_plate(dish1, dish2):
    return f"{dish1} and {dish2} Surprise!"

# PART D
def add_seasoning(dish, seasoning="salt"):
    print(f"Adding a sprinkle of {seasoning} to the {dish}. Yum!")

def main():
    print("hello world")
    # CALL YOUR FUNCTIONS in the main here
    about_me()
    weather()
    feeling("Tired", 8)
    make_plate("Spaghetti", "meatballs")
    add_seasoning("Pasta")

if __name__ == "__main__":
    main()

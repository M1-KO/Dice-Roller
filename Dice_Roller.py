import random

def roll_dice(num_dice, num_sides):
    rolls = []
    for i in range(num_dice):
        rolls.append(random.randint(1, num_sides))
    return rolls

def main():
    print(".:Welcome to the dice roller:.")
    num_dice = int(input("How many dice would you like to roll? "))
    num_sides = int(input("How many sides does each die have? "))
    rolls = roll_dice(num_dice, num_sides)
    print("You rolled:")
    for roll in rolls:
        print(roll)

if __name__ == "__main__":
    main()
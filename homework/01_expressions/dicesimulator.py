import random

NUM_SIDES = 6

def roll_dice():
    die1 : int = random.randint(1, NUM_SIDES)
    die2 : int = random.randint(1, NUM_SIDES)
    total : int = die1 + die2
    print("Total of two dice: " + str(total))

def main():
    die1: int = 10
    print ("die in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die in main() is: " + str(die1))

if __name__ == '__main__':
    main()
         
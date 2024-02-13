import random

one_rolls = 0
two_rolls = 0
three_rolls = 0
four_rolls = 0
five_rolls = 0
six_rolls = 0

for e in range(100):
    dice_roll = random.randint(1,6)
    if dice_roll == 1:
        print("One")
        one_rolls = one_rolls + 1
    elif dice_roll == 2:
        print("Two")
        two_rolls = two_rolls + 1
    elif dice_roll == 3:
        print("Three")
        three_rolls = three_rolls + 1
    elif dice_roll == 4:
        print("Four")
        four_rolls = four_rolls + 1
    elif dice_roll == 5:
        print("Five")
        five_rolls = five_rolls + 1
    else:
        print("Six")
        six_rolls = six_rolls + 1

print(f"Total one rolls: {one_rolls}")
print(f"Total two rolls: {two_rolls}")
print(f"Total three rolls: {three_rolls}")
print(f"Total four rolls: {four_rolls}")
print(f"Total five rolls: {five_rolls}")
print(f"Total six rolls: {six_rolls}")

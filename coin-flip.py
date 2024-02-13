import random

heads = 0
tails = 0
for e in range(100):
    coin_flip = random.randint(1,2)
    if coin_flip == 1:
        print("heads")
        heads = heads + 1
    else:
        print("tails")
        tails = tails + 1
print(f"Total heads: {heads}")
print(f"Total tails: {tails}")

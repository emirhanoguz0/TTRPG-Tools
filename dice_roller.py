import random
def dice_roller(n,x):
    s = 0
    for i in range(x):
        s += random.randint(1,n)
    return s
import random
def randInt(min=0, max=100):
    return round(random.random() * (max - min) + min)
print(randInt(5, 10))
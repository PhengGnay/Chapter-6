import random
# elements = ["earth", "air", "fire", "water"]

# print("choice===>", random.choice(elements)) # looking at the list and randomizing the output
# print("sample===>", random.sample(elements, 2)) # now taking 2 items from the list randomly

# random.shuffle(elements)
# print("shuffle===>", elements) # randomly switching the order

# print("randint===>", random.randint(1, 5)) # random int from 1-5)

def main():
    for i in range(3):
        outcome = spin()
        print(outcome, end=" ") 

def spin():
    n = random.randint(1, 20)
    if n > 15:
        return "Cherries"
    elif n > 10:
        return "Orange"
    elif n > 5:
        return "Plum"
    elif n > 2:
        return "Melon"
    elif n > 1:
        return "Bell"
    else:
        return "Bar"

main()


#Test for Monty Hall Problem
import random

comment = 0

tries = input("Skriv inn antall forsøk: ")

doorCount = 3
doorCount = input("Hvor mange dører ønsker du? ")

switch = input("Ønsker du å bytte dør om mulig? (Ja/Nei) ")
correctTries = 0

doors = [0] * int(doorCount)

def resetDoors():
    for i in range(int(doorCount)):
        doors[i] = 0
    
    correct = random.randint(1,int(doorCount))
    doors[correct-1] = 1

    return correct

for _ in range(int(tries)):
    correct = resetDoors()
    chosen = random.randint(1,int(doorCount))
    if comment:
        print("Prøver dør %d" % (int(chosen)))
    info = random.randint(1,int(doorCount))
    while info == chosen or doors[info-1] == 1:
        info = random.randint(1,int(doorCount))

    if comment: 
        print("Var ikke dør %d" % (int(info)))
    
    if switch.lower() == "ja":
        newChosen = random.randint(1,int(doorCount))
        while newChosen == info or newChosen == chosen:
           newChosen = random.randint(1,int(doorCount))
        if comment: 
            print("Prøver nå dør %d" % (int(newChosen)))
    else:
        newChosen = chosen

    if doors[newChosen-1] == 1:
        correctTries += 1
        if comment: 
            print("Du gjettet riktig!")
    else:
        if comment: 
            print("Du gjettet feil")

prosent = (int(correctTries) / int(tries)) * 100
expected = (1 / int(doorCount)) * 100
print("Antall forsøk: %d, antall riktig: %d, antall feil: %d, totalt: %2.2f%%, forventa: %2.2f%%"
 % (int(tries), int(correctTries), int(tries)-int(correctTries), prosent, expected))
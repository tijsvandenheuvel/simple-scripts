import random

naam1 = input("Naam 1: ")
naam2 = input("Naam 2: ")
score=0
if naam1.lower() =="pippa" and naam2.lower() =="tijs":
    score=100
elif naam2.lower() =="pippa" and naam1.lower() =="tijs":
    score=100
else:
    score = random.randint(0,50)

print (f"lovemeter Score voor {naam1} en {naam2} is {score}%")
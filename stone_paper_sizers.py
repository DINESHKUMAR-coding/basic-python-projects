'''
-1 for rock 
0 for paper
1 for sizers
'''
import random

computer = random.choice([1, 0, -1])

yourstr=input("Enter your choice: ")
yourdict={"r":-1,"p":0,"s":1}
valuedict={1:"Sizers",0:"Paper",-1:"Rock"}
you=yourdict[yourstr]

print(f"you choose: {valuedict[you]}\nComputer choose: {valuedict[computer]}")

if(computer == -1 and you == 0):
    print("YOU WIN !")
elif(computer == -1 and you == 1):
    print("YOU LOSE !")
elif(computer == -1 and you == -1):
    print("IT'S A DRAW !")
elif(computer == 1 and you == -1):
    print("YOU WIN !")
elif(computer == 1 and you == 0):
    print("YOU LOSE !")
elif(computer == 1 and you == 1):
    print("IT'S A DRAW !")
elif(computer == 0 and you == 1):
    print("YOU WIN !")
elif(computer == 0 and you == -1):
    print("YOU LOSE !")
elif(computer == 0 and you == 0):
    print("IT'S A DRAW !")
else:
    ("YOU ENTER SOMETHING WRONG !")
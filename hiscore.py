'WAP for a game on high score'
import random
def game():
    print("YOU are playing a game")
    score=random.randint(1,100)
    # fetch hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"Your score is :{score}")
    if(score>hiscore):
    # Write this hiscore to this file
      with open("hiscore.txt","w") as f:
        f.write(str(score))

    return score
game()
import random

def game():
    print("You are playing the game")
    score  = random.randint(1,45)
    #FETCH THE SCORE FROM FILE
    with open("D:\\PYTHON\\FILE IINPUT-OUTPUT\\practice set\\game.txt") as f:
       hiscore = f.read()
       if(hiscore!=""):
           hiscore = int(hiscore)
       else:
           hiscore = 0    

    print(f"your score is {score}") 
    #writig to file 
    if(score>hiscore):
        with open("D:\\PYTHON\\FILE IINPUT-OUTPUT\\practice set\\game.txt" , "w") as f:
          f.write(str(score))

    return score      

game()      
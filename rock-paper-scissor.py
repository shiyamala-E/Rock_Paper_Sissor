import random
print("welcome to play Rock-Paper-Scissor")

tap_to_start=input("do you want to play : yes/no ?")
if tap_to_start.lower() != "yes":
    quit()
print("Ok lets play")
running=True
score=0

while running:
    player =input("Rock,Paper,Scissors? : ")
    computer =  random.choice(['Rock','Paper','Scissors'])

    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="Paper":
            print("You lose!",computer,"covers",player)
        else:
            print("You win ! ", player,"Smashes",computer)
            score+=1

    elif player=="Paper":
        if computer=="Scissors":
            print("You lose!",computer,"cut",player)
        else:
            print("You win ! ", player,"covers",computer)
            score+=1

    elif player=="Scissors":
        if computer=="Rock":
            print("You lose!",computer,"Smashes",player)
        else:
            print("You win ! ", player,"cut",computer)
            score+=1
    else:
        print("check your spelling !!")
    play_again=input("playing again?(y/n):").lower()
    if not play_again =="y":
        running=False
print("your score:"+str(score))

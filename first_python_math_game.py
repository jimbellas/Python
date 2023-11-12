import random


print("Do you want to play a Math game, Y or N?")
startAnswer = input ()
if startAnswer == 'Y':
    print("Okay lets make sure you know math with a basic question")
    
    random1 = random.randint(1, 5)
    random2 = random.randint(1, 5)
    random3 = random.randint(20, 70)
    random4 = random.randint(20, 70)
    uanswer1 = int(input("What is " + str(random1) + " + " + str(random2) + "? = "  ))
    if uanswer1 == random1 + random2:
        print("Good Job, we can move on")
        print("Lets try a harder question...")
        uanswer2 = int(input("What is " + str(random3) + " + " + str(random4) + "? = "  ))
        if uanswer2 == random3 + random4:
            print("YOU WIN!")
        else:
            print("You failed, restart the game")
    else: 
        print("That is not correct, I think this game isn't for you")
        

    
    pass

else: 
    print("Have a good day!")


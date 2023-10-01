import math
import random
n=0
stop_game = False

while(not stop_game):
    if(n>=10):
        print("Congratulation! You won the game .")
        break
    a=random.randint(0,99)
    b=random.randint(0,99)
    op = random.choice(["+", "-"])
    if(random.choice([True,False])):
        if(op=="+"):
            print(a,"+",b,"=",a+b)
        else:
            print(a,"-",b,"=",a-b)
        ans=input("yes/no\n")
        if(ans in "yes" or ans in "Yes" or ans in "YES"):
            print("Correct answer,next question. ")
            n+=1
        elif(ans in "no" or ans in "No" or ans in "NO"):
            print("Wrong answer, try again.")
            stop_game=True
        else:
            print("Syntax error. Try again")
            break
    else:
        print(a,op,b,"=",random.randint(0,99))
        ans=input("yes/no\n")
        if(ans in "yes" or ans in "Yes" or ans in "YES"):
            print("Wrong answer, try again.")
            stop_game=True
    
            
        elif(ans in "no" or ans in "No" or ans in "NO"):
            print("Correct answer,next question. ")
            n+=1
        else:
            print("Syntax error. Try again")
            break
            
            
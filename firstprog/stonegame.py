import random
print("Here presenting our childhood game->Stone,Paper & Scissor")
lst=["Stone","Paper","Scissor"]
n=10
print("Here's your game starts")
print("Rules:\n1:Stone\n2:Paper\n3:Scissor")
total_points=10
win_point=0
lose_point=0
while(n!=0):

        n=n-1
        a=input("Enter your choice: ")
        choice = random.choice(lst)
        if(int(a)==1 and choice=="Stone"):
            print("Computer chooses",choice)
            print("Oops...Tie...Try again")
            print("SCORE:",win_point,"points out of",total_points)
            print(n,"chances left")
            if(n==0):
                print("Gameover")
                if(win_point>lose_point):
                    print("YOU WIN by",win_point,"points")
                else:
                    print("YOU LOSE by",lose_point-win_point,"points")
            else:
                continue
        elif(int(a)==1 and choice=="Paper"):
            lose_point=lose_point+1
            print("Computer chooses",choice)
            print("Computer wins")
            print("SCORE: ",win_point,"points out of",total_points)
            print(n,"chances left")
            if (n == 0):
                print("Gameover")
                if (win_point > lose_point):
                    print("YOU WIN by", win_point, "points")
                else:
                    print("YOU LOSE by", lose_point - win_point, "points")
            else:
                continue
        elif(int(a)==1 and choice=="Scissor"):
            win_point=win_point+1
            print("Computer chooses",choice)
            print("You win")
            print(n,"chances left")
            print("SCORE: ", win_point, "points out of", total_points)

            if (n == 0):
                print("Gameover")
                if (win_point > lose_point):
                    print("YOU WIN by", win_point, "points")
                else:
                    print("YOU LOSE by", lose_point - win_point, "points")
            else:
                continue
        elif(int(a)==2 and choice=="Stone"):
            win_point=win_point+1
            print("Computer chooses",choice)
            print("You win")
            print("SCORE: ",win_point,"points out of",total_points)
            print(n, "chances left")
            if (n == 0):
                print("Gameover")
                if (win_point > lose_point):
                    print("YOU WIN by", win_point, "points")
                else:
                    print("YOU LOSE by", lose_point - win_point, "points")
            else:
                continue
        elif(int(a)==2 and choice=="Paper"):
            print("Computer chooses",choice)
            print("Tie")
            print(n, "chances left")
            print("SCORE:", win_point, "points out of", total_points)
            if (n == 0):
                print("Gameover")
                if (win_point > lose_point):
                    print("YOU WIN by", win_point, "points")
                else:
                    print("YOU LOSE by", lose_point - win_point, "points")
            else:
                continue
        elif(int(a)==2 and choice=="Scissor"):
            lose_point=lose_point+1
            print("Computer chooses",choice)
            print("Computer wins")
            print(n, "chances left")
            print("SCORE:", win_point, "points out of",total_points)
            if (n == 0):
                print("Gameover")
                if (win_point > lose_point):
                    print("YOU WIN by", win_point, "points")
                else:
                    print("YOU LOSE by", lose_point - win_point, "points")
            else:
                continue
        elif(int(a)==3 and choice=="Stone"):
            lose_point=lose_point+1
            print("Computer chooses",choice)
            print("Computer wins")
            print(n, "chances left")
            print("SCORE:", win_point, "points out of", total_points)
            if (n == 0):
                print("Gameover")
                if (win_point > lose_point):
                    print("YOU WIN by", win_point, "points")
                else:
                    print("YOU LOSE by", lose_point - win_point, "points")
            else:
                continue
        elif(int(a)==3 and choice=="Paper"):
            win_point=win_point+1
            print("Computer chooses",choice)
            print("You win")
            print(n, "chances left")
            print("SCORE:", win_point, "points out of", total_points)
            if (n == 0):
                print("Gameover")
                if (win_point > lose_point):
                    print("YOU WIN by", win_point, "points")
                else:
                    print("YOU LOSE by", lose_point - win_point, "points")
            else:
                continue
        elif(int(a)==3 and choice=="Scissor"):
            print("Computer chooses",choice)
            print("Tie")
            print(n, "chances left")
            print("SCORE:", win_point, "points out of", total_points)
            if (n == 0):
                print("Gameover")
                if (win_point > lose_point):
                    print("YOU WIN by", win_point, "points")
                else:
                    print("YOU LOSE by", lose_point - win_point, "points")
            else:
                continue
        else:
            print("Invalid Input")
            continue
        break
import random as rn

#setting the choices
series = ["Rock", "Paper", "Scissors"]

#setting the number of attempts
n = 0 #the number of tries per game
score = 0
comp_score = 0

#allowing the user to attempt
while n < 3:
    
    #once any score is 2, the winner is clear
    if score > 1 or comp_score > 1:
        break
    
    else:
        #computer and user choosing from series
        comp_choice = rn.choice(series) #random was imported as rn
        user_choice = input("Choose rock, paper, or scissors:").capitalize()
        n += 1
        
        #determing the winner, try again during draws and add scores during wins
        if user_choice not in series:
            print("Invalid Input. Try Again!")
            n -= 1
        elif user_choice == "Rock" and comp_choice == "Paper":
            comp_score += 1
            print(f"You lose! {comp_choice} beats {user_choice}")
        elif user_choice == "Paper" and comp_choice == "Scissors":
            comp_score += 1
            print(f"You lose! {comp_choice} beats {user_choice}")
        elif user_choice == "Scissors" and comp_choice == "Rock":
            comp_score += 1
            print(f"You lose! {comp_choice} beats {user_choice}")
        elif comp_choice == "Rock" and user_choice == "Paper":
            score += 1
            print(f"You win! {user_choice} beats {comp_choice}. Your score is now {score}.")
        elif comp_choice == "Paper" and user_choice == "Scissors":
            score += 1
            print(f"You win! {user_choice} beats {comp_choice}. Your score is now {score}.")
        elif comp_choice == "Scissors" and user_choice == "Rock":
            score += 1
            print(f"You win! {user_choice} beats {comp_choice}. Your score is now {score}.")
        else:
            n -= 1
            print(f"You both chose {comp_choice}. Try again!")


#notifying the winner based on the final scores            
if score > 1:
    print(f"You won the round! You scored {score} and the computer scored {comp_score}. Congrazulatione!")
else:
    print(f"Too sad, you lost the round. You scored {score} and the computer scored {comp_score}. Try again next time!")
    
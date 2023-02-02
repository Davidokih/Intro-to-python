#Collect all the components of your program to run it in a while loop
#Import the random library
import random


#Add the code to create a list containing the three actions of the game.
rounds = ["rock", "paper", "scissors"]

#Add the code to set the scores of players to 0
player1 = 0
player2 = 0
#Add a round_counter that is 0 at the beginning
round_counter = 0

#Add the code to ask the user how many rounds they want to play
number_of_rounds = input("input number of rounds")

#Write a while loop and put the game inside
while True:

  #increase round_counter by 1 and print it
  round_counter +=1
  print("Round number:", round_counter)

  #Add the code to select a random action for each player
  player1_choice = random.choice(rounds)
  player2_choice = rounds[random.randint(0,2)]

  #Add the code to print the players choices
  print("Player1:", player1_choice)
  print("Player2:", player2_choice)

  #Add the tie condition
  if player1_choice == player2_choice:
    print("its a tie")

  #Add the remaining condition
  elif player1_choice == 'paper' and player2_choice == 'rock':
    print("Winner is: Player 1")
    player1 +=1

  elif player1_choice == 'paper' and player2_choice == 'scissors':
    print("Winner is: Player 2")
    player2 +=1

  elif player1_choice == 'scissors' and player2_choice == 'rock':
    print("Winner is: Player 2")
    player2 +=1

  elif player1_choice == 'scissors' and player2_choice == 'paper':
    print("Winner is: Player 1")
    player1 +=1

  elif player1_choice == 'rock' and player2_choice == 'paper':
    print("Winner is: Player 2")
    player2 +=1

  elif player1_choice == 'rock' and player2_choice == 'scissors':
    print("Winner is: Player 1")
    player1 +=1

  #print the score
  print("Score:", "Player1 =",player1, "Player2 =",player2)

  #stop the while loop if the round_counter equals the number of total rounds
  if round_counter == int(number_of_rounds):
    break
#Print the outcome of the game by using conditional statements
if player1 == player2:
  print("There is no winner, tie.")
elif player1 > player2:
  print("Player 1 won with score", player1, ":", player2)
elif player1 < player2:
  print("Player 2 won with score", player1, ":", player2)  

# my_list = [1,5,5,5,5,1]
# top = my_list[0]
# for el in my_list:
#     if el > top:
#         top = el
# print(my_list[top])
    
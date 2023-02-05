import random
import time
"""If else statement"""

celcus = 10
hot = True
# if (celcus > 10):
    # print("Good")

if (celcus > 30):
    print("too hot")
elif (30 >= celcus > 20):
    print("Good temperature")
elif -272 < celcus <=20:
    print("Too cold")
else:
    print("the value is way too hot")

# For loops

volcano_name = "Ehjjjfjfrisp;ssjbbcucopwwj"

for i in volcano_name:
    print(i)
print("Loop is completed")


volcano_number = [1,2,3,4,5,6,7,8,9,10]

for i in volcano_number:
    print(i)
print("Loop is completed")


for i in range(1,101):
    if(i % 5 == 0):
        print(i)
print("Loop completed")

# While loop

while  celcus < 50:
    if (celcus > 30):
        print("too hot")
    elif (30 >= celcus > 20):
        print("Good temperature")
    elif -272 < celcus <=20:
        print("Too cold")
    else:
        print("the value is way too hot")

    print("The current temperature", celcus)
    celcus += 5
    time.sleep(1)

while True:
    random_number = random.randrange(1000)
    print(random_number)
    if random_number == 777:
        print("Found")
        break


# Rock paper and scissors game
"""with for loop"""
#Collect all the components of your program to run it in a while loop
#Import the random library
import random

#Add the code to create a list containing the three actions of the game.
rounds = ["rock", "paper", "scissors"]

#Add the code to set the scores of players to 0
player1 = 0
player2 = 0

#Write a while loop and put the game inside
while True:

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

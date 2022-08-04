# -*- coding: utf-8 -*-
"""RockPaperScissors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_8RdSlkG8p4Q2H-1kubl-M3SGxymZ6w1
"""

#Program written by Andrew West 7/20/22


import random

def getUserInput():
    check = 0
    while(check == 0):
      userPlay = input("Type either Rock Paper or Scissors: ")
      if(userPlay == "Rock" or userPlay == "Paper" or userPlay == "Scissors"):
        print("You chose " + userPlay +"! Good choise!")
        return userPlay
      else:
        print("Oops! That's not an option!")
      
def getWinner(comPlay, userPlay):
  if(comPlay == userPlay):
    return "tie"
  elif(comPlay == "Rock"):
    if(userPlay == "Scissors"):
      return "comp"
    elif(userPlay == "Paper"):
      return "user"
  elif(comPlay == "Scissors"):
    if(userPlay == "Paper"):
      return "comp"
    elif(userPlay == "Rock"):
      return "user"
  elif(comPlay == "Paper"):
    if(userPlay == "Rock"):
      return "comp"
    elif(userPlay == "Scissors"):
      return "user"

def play_rock_paper_scissors():
    #Talking to user and Getting input
    print("Let's play Rock Paper Scissors!")
    userPlay = getUserInput()
    num = random.randint(0,299)

    #Gets computer's play
    if num < 100:
        comPlay = "Rock"
    elif num < 200:
        comPlay = "Paper"
    else:
      comPlay = "Scissors"


    print("I chose " + comPlay)

    winner = getWinner(comPlay, userPlay)

    if(winner == "comp"): #Comp wins
      print(comPlay + " beats " + userPlay + " I won!")
    elif(winner == "tie"): #Players tie
      print("We tied! We both played " + comPlay )
    else: #User wins
      print(userPlay + " beats " + comPlay + " you won!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_rock_paper_scissors()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random
options = ["rock","scissor", "paper"]

user_wins = 0
computer_wins = 0


while True:
    user_input = input("plz type rock/scissor or paper or q for quite ").lower()
    var = random.randint(0,2)
  

    computer_input = options[var]
    if user_input == "q":
          break 
    elif user_input  not in options:
          continue
    elif user_input == computer_input:
          print("match tie")

    elif user_input == "rock" and computer_input == "scissor":
        print("you win")
        user_wins += 1
    elif user_input == "scissor" and computer_input == "paper":
            print("you win")
            user_wins += 1
    elif user_input == "paper" and computer_input == "rock":
            print("you win")
            user_wins += 1

    else:
        print("computer win")   
        computer_wins += 1




print("computer score", computer_wins)
print("your score", user_wins)

print("good luck for nex time")


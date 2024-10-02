
# Rock Paper Scissors Game

This is a simple Python-based **Rock, Paper, Scissors** game where the user plays against the computer.

## Game Description
The user can input either `rock`, `scissor`, or `paper` to play against the computer, which randomly chooses one of the three options. The game keeps track of the score for both the user and the computer until the user decides to quit.

## Game Logic
1. The computer randomly selects either "rock", "scissor", or "paper".
2. The user inputs their choice.
3. The game compares both choices and decides who wins:
    - "Rock" beats "Scissor"
    - "Scissor" beats "Paper"
    - "Paper" beats "Rock"
4. If both user and computer choose the same option, it's a tie.
5. The score is updated based on the result.

## How to Play:
- Type either `rock`, `scissor`, or `paper` to play.
- To quit the game, type `q`.

## Code Implementation

```python
import random
options = ["rock","scissor", "paper"]

user_wins = 0
computer_wins = 0

while True:
    user_input = input("plz type rock/scissor or paper or q for quit: ").lower()
    var = random.randint(0,2)

    computer_input = options[var]
    if user_input == "q":
        break 
    elif user_input not in options:
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
        print("computer wins")   
        computer_wins += 1

print("Computer score:", computer_wins)
print("Your score:", user_wins)
print("Good luck for next time!")
```

## Example:
```text
plz type rock/scissor or paper or q for quit: rock
computer wins
plz type rock/scissor or paper or q for quit: paper
you win
plz type rock/scissor or paper or q for quit: q
Computer score: 1
Your score: 1
Good luck for next time!
```

## Enjoy the game!

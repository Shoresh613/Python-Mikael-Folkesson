# There are no constants in Python, but the convention is 
# if it's intended not to change, use capital letters 

from random import choice

SIGNS = ["rock","paper","scissors"]
score = 0

def main():
    print(f"Welcome to the {', '.join(SIGNS)} game.\n")
    print_rules()
    number_of_rounds = select_number_of_rounds()
    print(f"Best of {number_of_rounds} wins. Let's start!")
    score=game_loop(number_of_rounds)
    print(f"You won {score} times out of {number_of_rounds}.")

def print_rules():
    print("Rules\n=====\nEach player picks a sign\n")
    for winner, loser in zip([0,1,2], [2,0,1]):
        print(f"{SIGNS[winner].title()} wins over {SIGNS[loser]}")

def select_number_of_rounds():
    while True:
        try:
            rounds = int(input("\nSelect number of rounds: "))
            if rounds > 0:
                return rounds
            else:
                print("Rounds must be at least 1")
        except ValueError:
            print("Enter a positive integer as a digit, e.g. 4")

def game_loop(number_of_rounds):
    global score
    for current_round in range(1,number_of_rounds+1):
        print(f"\nRound {current_round}")
        sign_player_a = get_sign_from_user()
        sign_player_b = get_sign_from_computer()
        
        print(f"The computer picks {sign_player_b}")

        if is_draw(sign_player_a,sign_player_b):
            print("It's a draw!")
        elif wins_over(sign_player_a,sign_player_b):
            print("You win!")
            score += 1
        else:
            print("The computer wins!")
        
def get_sign_from_user():
    while True:
        sign = input("Pick a sign: ").strip().lower()
        if sign in SIGNS: 
            return sign
        else:
            print(f"You must pick one of the signs: {', '.join(SIGNS)}")

def get_sign_from_computer():
    return choice(SIGNS)

def is_draw(sign_a,sign_b):
    return sign_a == sign_b

def wins_over(sign_a,sign_b):
    for winner, loser in zip([0,1,2], [2,0,1]):
        if sign_a == SIGNS[winner] and sign_b == SIGNS[loser]: return True
    return False

main()
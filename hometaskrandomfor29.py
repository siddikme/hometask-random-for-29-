# Task1 
# import random

# number_to_guess = 27  # You can set this to a specific number or use random.randint(1, 100)
# lives = 5

# while lives > 0:
#     guess = int(input("Enter your guess (1-100): "))

#     if guess == number_to_guess:
#         print("You Winnn!!!")
#         break
#     elif abs(guess - number_to_guess) == 1:
#         print("Too closer")
#     elif guess > number_to_guess:
#         print("Too high")
#     else:
#         print("Too low")
    
#     lives -= 1

#     if lives == 0:
#         print("Game Over!!!")
# solved:

# task2

# import random
# a1 = [random.randint(0, 1) for i in range(5)]
# a2 = [random.randint(0, 1) for i in range(5)]
# res = a1 == a2
# print("First array:")
# print(a1)
# print("Second array:")
# print(a2)
# print("Test above two arrays are equal or not!")
# print(res)
# solved:


# Task3

# import random
# import string
# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password


# length = int(input("Enter the desired password length: "))

# password = generate_password(length)
# print("Generated password:", password)
# solved:


# task4
# import random

# def get_computer_choice():
#     return random.choice(['Rock', 'Paper', 'Scissors'])

# def get_winner(player_choice, computer_choice):
#     if player_choice == computer_choice:
#         return "It's a tie!"
#     elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
#          (player_choice == 'Paper' and computer_choice == 'Rock') or \
#          (player_choice == 'Scissors' and computer_choice == 'Paper'):
         
#         return "You win!"
#     else:
#         return "You lose!"

# def play_game():
#     print("Welcome to Rock, Paper, Scissors!")
#     print("Select your move (1 for Rock, 2 for Paper, 3 for Scissors):")
    
#     choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
#     try:
#         player_input = int(input())
#         if player_input in choices:
#             player_choice = choices[player_input]
#             computer_choice = get_computer_choice()
#             print(f"Computer chose {computer_choice}.")
#             print(get_winner(player_choice, computer_choice))
#         else:
#             print("Invalid input. Please select 1, 2, or 3.")
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# if __name__ == "__main__":
#     play_game()
 


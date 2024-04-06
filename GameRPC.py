import random
r='''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''
p='''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''
s='''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
emote = {"rock": r, "paper": p, "scissors": s}
def rps():
    print("welcome to the Rock Paper Scissors Game\n--------------------------------------------------")
    user_choice = input("Choose your choice: Rock, Paper, Scissors\n").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    if user_choice in ["rock", "paper", "scissors"]:
        if user_choice == computer_choice:
            print(f"It's a tie!\nYou chose: {user_choice}{emote[user_choice]}\nComputer chose: {computer_choice}{emote[computer_choice]}")
        elif user_choice == "rock" and computer_choice == "scissors":
            print(f"You win!\nYou chose: {user_choice}{emote[user_choice]}\nComputer chose: {computer_choice}{emote[computer_choice]}")
        elif user_choice == "scissors" and computer_choice == "paper":
            print(f"You win!\nYou chose: {user_choice}{emote[user_choice]}\nComputer chose: {computer_choice}{emote[computer_choice]}")
        elif user_choice == "paper" and computer_choice == "rock":
            print(f"You win!\nYou chose: {user_choice}{emote[user_choice]}\nComputer chose: {computer_choice}{emote[computer_choice]}")
        else:
        
            print(f"You lose!\nYou chose: {user_choice}{emote[user_choice]}\nComputer chose: {computer_choice}{emote[computer_choice]}")
    else:
        print("Invalid choice!!! Try again")
        
    play_again = input("--------------------------------------------------\nWanna play again?\nYes or No\n ").lower()
    if play_again == "yes":
        print("--------------------------------------------------")
        rps()
    else:
        print("""--------------------------------------------------\nGG brah!!! See you again\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⣀⣴⡾⢿⢛⣛⡛⣛⢻⣛⠿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠓⢦⠀⠀
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⡟⡍⡞⠴⣣⠌⣇⠇⣎⠸⡑⠶⣈⠟⣻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⡠⠁⣸⠾⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡹⢎⡱⢳⠜⡣⢆⠩⢆⠭⣄⢣⠜⡢⢅⢎⡱⢎⡻⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⡔⢡⢂⠸⡇⠀⠀
⠤⠀⠀⠀⠀⠀⠀⠀⣰⡟⣶⡙⣮⠑⣏⣮⣵⣾⣿⣿⣻⣟⣿⣻⣿⣾⣬⣳⣍⠞⣭⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⢻⡵⣉⠖⡬⢸⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢐⡯⣝⢶⡹⣆⣿⣿⣿⣿⣽⡾⢷⠿⣛⣛⣛⣛⠿⠿⠿⠿⣾⣵⣏⣿⣆⠀⠀⠀⠀⠀⠀⠀⢸⡷⣍⠞⣡⢻⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⣟⡼⣣⣿⢿⣛⣭⡵⣞⣶⣿⣯⣿⣽⣧⣯⣽⣻⣟⣟⣻⢶⣯⣽⣫⣝⡿⣷⢦⣄⡀⠀⠀⢸⡷⢌⡛⢤⠹⣇⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⡿⢟⣯⢷⣯⣿⣾⣿⣿⣿⣿⣿⡿⢫⡟⣽⣿⣿⣿⣿⣿⣟⣯⢶⣛⣾⣽⣿⣾⣭⣿⣦⠶⡾⠷⠛⠟⠦⠥⡜⢧⡀
⠀⠀⠀⠀⣠⣶⣟⣯⢿⣻⣽⣿⣿⣿⣿⣿⢻⣿⣿⣿⠱⣣⠞⣩⣿⣿⣿⣿⣿⣿⣿⡿⠛⢉⠁⣁⠈⢄⠠⣀⠂⠤⡐⢠⠂⡄⢢⠐⡌⣷
⠀⠀⣠⣾⣿⢾⣻⣞⣯⣿⣿⣿⣿⣿⣿⢯⣹⣿⣿⡇⢣⡑⢎⠡⣻⣿⡇⣿⣿⣿⣿⠰⡁⢎⠐⡠⠉⡄⡑⣨⡘⢤⠑⣢⠱⢌⢢⡓⡼⣉
⣠⣾⣫⢿⣹⢯⣷⣾⣿⣿⣿⣿⣿⣿⣯⢓⡸⣿⢳⡃⢆⠘⡄⠃⢜⣻⡇⢞⣿⣿⣿⣧⣙⣦⣽⣴⡷⠾⠷⠿⠋⢆⠩⢀⠣⠌⢢⠝⡲⠥
⣿⣳⢯⣛⣧⡟⣯⣟⣾⣿⣿⣿⡿⣟⠿⢾⢶⣿⣹⡀⠌⡐⢠⠛⠩⣙⢃⡨⢿⣟⣿⡏⠉⡉⠤⢀⡐⢄⠢⡐⢡⠌⡠⢀⠄⡈⠆⡉⢖⠩
⣿⣟⣯⢳⡞⣽⢳⢾⣿⣿⣿⣿⡷⣉⣞⣠⣧⣌⡹⢛⣷⠀⢂⠸⣷⠟⠛⠛⣻⣷⣻⣇⠦⣁⢒⡠⡐⡌⠤⣡⢣⢎⡕⣣⠜⣤⢓⡜⡌⢒
⣿⣎⢷⣛⡾⣝⣯⡿⣿⣿⣹⣿⡗⡿⢋⠉⠉⠙⠻⠧⣾⡇⡀⢈⠁⣄⣲⣤⢿⣯⣿⢻⣷⠾⡶⠷⠷⠞⡛⠻⠛⠮⡙⢔⠫⠶⣯⢳⣍⡖
⠈⠛⠷⣯⣽⣹⠾⣽⢳⣿⢻⣿⣷⡘⣤⣂⣌⣠⠁⢂⠙⠿⠛⢀⣄⣤⣤⠿⠛⣻⣯⣿⡇⢦⠑⡌⢢⠁⢆⠡⢎⡐⠠⠈⠌⡱⢬⢳⡹⢜
⠀⠀⠀⠀⠈⠙⠻⢷⣿⡿⣷⣟⣿⣧⢹⣟⠛⢙⠛⠛⠻⠛⠟⠛⠉⠁⠀⣆⣠⣿⢣⣿⣿⣶⣭⣲⣥⣞⣤⣛⣶⣺⢥⢳⡸⣰⢏⠶⣑⢎
⠀⠀⠀⠀⠀⢀⣶⡟⣿⣟⡼⣿⣟⣿⣦⣻⣶⠼⣦⠄⠠⠤⠤⠔⠂⠐⠋⢹⣴⣿⣿⢻⣟⣿⣿⢭⡋⢭⠩⡍⣍⠛⠯⢖⡹⢟⡾⣹⢞⡼
⠀⠀⠀⠀⠀⣾⣿⣿⡼⣿⣗⣿⣿⣞⣿⣷⣽⣻⠶⣤⣄⣀⣀⣀⣠⣤⡶⣞⣷⠿⣌⣿⣯⣿⣿⣮⣳⢎⡵⣛⣬⣛⠴⣨⡱⣏⡾⣱⢏⡾
⠀⠀⠀⠀⢠⣿⣿⡽⣷⣻⣿⣞⣿⣟⡾⢿⣿⡿⣿⣾⣿⣯⣽⣭⣿⡷⣾⠿⡩⢃⣴⣿⢾⣿⢯⣟⡿⣿⣿⣷⣾⣿⣿⣷⣽⣧⣿⣷⣿⣿
⠀⠀⠀⠀⢼⣿⣻⣿⣿⣿⣞⡿⣞⡿⣿⣯⣟⣿⣷⣫⢷⡯⣝⠻⡜⢣⢃⣼⣴⣿⡿⣯⣿⣿⣻⣞⡿⣯⣿⣿⣿⣿⣾⣯⣟⣾⣽⣳⣿⣿
⠀⠀⠀⠀⣿⣻⢷⣿⣿⣿⣾⣿⢯⣿⣽⣿⣾⠷⣿⣿⣏⠛⢷⣱⡼⢞⣩⣾⠟⣿⣽⣿⣟⡷⣻⣼⣿⣿⣝⣿⣍⠙⠛⠿⣿⢿⣾⣿⣿⣿
⠀⠀⠀⢰⣿⣽⡿⣿⣻⣿⡿⣯⣿⣟⣾⡽⣿⣶⣿⡏⠙⢯⣚⣻⣶⢫⣷⠏⢠⢛⣿⡿⣾⣽⣿⣿⣿⣿⣾⣳⢿⣷⠀⠀⠀⠀⠻⣽⣿⣿
⠀⠀⠀⠘⣿⣧⣿⣿⣿⣟⣿⣿⡿⣿⣾⣿⣽⠾⣿⣯⣒⣌⣿⣯⣿⣯⣿⣦⡷⠿⣿⣿⣿⢯⣷⣿⣿⡾⣿⣯⣷⣿⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢻⣿⣿⣼⣿⣾⢏⠻⢿⣿⣿⣿⣷⣿⣿⡱⠟⣩⡄⣶⡤⠦⢏⣹⣷⣾⣿⣿⣿⣿⣷⣿⡿⣟⣿⣷⡿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣿⠙⠷⢮⣶⣢⣹⣿⣾⣽⣿⣿⣿⣷⠶⠶⠾⠷⡾⣛⣟⣷⣿⣟⣯⢿⣿⣯⣷⣿⡿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⢀⡈⢙⣿⣿⣻⣿⣯⣻⣝⡿⣻⣿⣿⣿⣿⣿⣿⣽⣣⣟⡞⣯⠾⣽⣻⣿⢿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")

rps()

    

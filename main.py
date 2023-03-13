import random
wins = 0
lose = 0
draw = 0
run = True
while run:
    choice_list = ["rock", "paper", "scissors"]
    your_choice = input("rock, paper, or scissors, or end game?   ")
    enemy_choice = random.choice(choice_list)
    print(enemy_choice)
    if your_choice == "rock":
        if enemy_choice == "scissors":
            print("You WIN!!! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
            wins += 1
        if enemy_choice == "paper":
            print("You LOSE ಥ_ಥ")
            lose += 1
        if enemy_choice == "rock":
            print("draw")
            draw += 1
            
    if your_choice == "paper":
        if enemy_choice == "rock":
            print("You WIN!!! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
            wins += 1
        if enemy_choice == "scissors":
            print("You LOSE ಥ_ಥ")
            lose += 1
        if enemy_choice == "paper":
            print("draw")
            draw += 1
            
    if your_choice == "scissors":
        if enemy_choice == "paper":
            print("You WIN!!! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
            wins += 1
        if enemy_choice == "rock":
            print("You LOSE ಥ_ಥ")
            lose += 1
        if enemy_choice == "scissors":
            print("draw")
            draw += 1
    if your_choice == "end game":
        print(f"you won {wins} times")
        print(f"you lose {lose} times")
        print(f"you tied {draw} times")

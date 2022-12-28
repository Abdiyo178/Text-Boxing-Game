import random
MAX_HEALTH = 100
MIN_POWER = 10
MAX_POWER = 20
player_health = MAX_HEALTH
player_name = input("Enter your name: ")
computer_health = MAX_HEALTH
computer_name = "Computer"
while True:
    print(f"{player_name}'s turn")
    print(f"{player_name}'s health: {player_health}")
    print(f"{computer_name}'s health: {computer_health}")
    player_input = input(f"{player_name}, do you want to attack or defend? ")

    if player_input.lower() == "attack":
        player_power = random.randint(MIN_POWER, MAX_POWER)
        computer_health -= player_power
        print(f"{player_name} attacks for {player_power} damage!")
    elif player_input.lower() == "defend":
        print(f"{player_name} defends.")
    else:
        print("Invalid input. Try again.")
        continue
    if computer_health <= 0:
        print(f"{player_name} wins!")
        break
    print(f"{computer_name}'s turn")
    print(f"{player_name}'s health: {player_health}")
    print(f"{computer_name}'s health: {computer_health}")
    computer_input = random.choice(["attack", "defend"])
    if computer_input == "attack":
        computer_power = random.randint(MIN_POWER, MAX_POWER)
        player_health -= computer_power
        print(f"{computer_name} attacks for {computer_power} damage!")
    else:
        print(f"{computer_name} defends.")
    if player_health <= 0:
        print(f"{computer_name} wins!")
        break

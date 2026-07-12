import random

def description():
    print("Welcome to 21 Number Game!\n" \
    "The objective of this game is to not be the one to call 21.\n" \
    "The game is played between you and the computer.\n" \
    "You can call 1 to 3 consecutive numbers in your turn.\n" \
    "Start from 1 and continue upward.\n" \
    "If you are the one to call 21, you lose! Else, you win!\n" \
    "Good luck and may the odds be ever in your favor!\n")

    starting_player = input("Do you want to go first or second? [F/S]: ")

    match starting_player:
        case "F":
            player_turn = True
            computer_turn = False
        case "S":
            computer_turn = True
            player_turn = False
        case _:
            return
        
    return player_turn, computer_turn

def player_loop(called_nums, last_num):
    end_reached = False
    player_nums = input("Call 1 to 3 consecutive numbers: ").split()

    if not player_nums:
        print("You must enter at least one number!")
    elif len(player_nums) > 3:
        print("You are disqualified!")
        return last_num, player_turn, computer_turn, called_nums, end_reached
    else:
        if (last_num + 1 >= 21):
            player_turn = True
            computer_turn = False
            end_reached = True
            return last_num, player_turn, computer_turn, called_nums, end_reached

        num1 = int(player_nums[0])
        if num1 != last_num + 1:
            print("You are disqualified!")
            return last_num, player_turn, computer_turn, called_nums, end_reached
        else:
            called_nums.extend([num1])
        if len(player_nums) > 1:
            num2 = int(player_nums[1])
            if num2 != num1 + 1:
                print("You are disqualified!")
                return last_num, player_turn, computer_turn, called_nums, end_reached
            else:
                called_nums.extend([num2])
        else:
            num2 = None
        if len(player_nums) > 2:
            num3 = int(player_nums[2])
            if num3 != num2 + 1:
                print("You are disqualified!")
                return last_num, player_turn, computer_turn, called_nums, end_reached
            else:
                called_nums.extend([num3])
        else:
            num3 = None

    player_turn = False
    computer_turn = True

    return last_num, player_turn, computer_turn, called_nums, end_reached

def computer_loop(called_nums, last_num):
    end_reached = False
    next_num = last_num + 1
    number_of_nums = random.randint(1,3)

    if (next_num >= 21):
        player_turn = False
        computer_turn = True
        end_reached = True
        return last_num, computer_turn, player_turn, called_nums, end_reached
    elif (next_num + 1 == 21):
        number_of_nums = 1
    elif (next_num + 2 == 21):
        number_of_nums = 2

    if (number_of_nums == 1):
        called_nums.extend([next_num])
    elif (number_of_nums == 2):
        called_nums.extend([next_num, next_num + 1])
    elif (number_of_nums == 3):
        called_nums.extend([next_num, next_num + 1, next_num + 2])

    computer_turn = False
    player_turn = True

    return last_num, computer_turn, player_turn, called_nums, end_reached

def end_condition(player_turn, computer_turn):
    if (player_turn):
        print("You lose!")
    elif (computer_turn):
        print("You win!")

    return

def game_loop(player_turn, computer_turn):
    called_nums = [0]  # start with zero to get last_num
    last_num = called_nums[len(called_nums)-1] # check for consecutiveness

    while (last_num < 21):
        last_num = called_nums[len(called_nums)-1]

        if (player_turn):
            last_num, player_turn, computer_turn, called_nums, end_reached = player_loop(called_nums, last_num)
            if (end_reached):
                end_condition(player_turn, computer_turn)
                break
            print(called_nums)
        elif (computer_turn):
            last_num, computer_turn, player_turn, called_nums, end_reached = computer_loop(called_nums, last_num)
            if (end_reached):
                end_condition(player_turn, computer_turn)
                break
            print(called_nums)

def main():
    player_turn, computer_turn = description()
    game_loop(player_turn, computer_turn)

if __name__ == "__main__":
    main()
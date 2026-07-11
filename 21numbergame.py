def description():
    print("Welcome to 21 Number Game!\n" \
    "The objective of this game is to not be the one to call 21.\n" \
    "The game is played between you and the computer.\n" \
    "You can call 1 to 3 consecutive numbers in your turn.\n" \
    "Start from 1 and continue upward.\n" \
    "If you are the one to call 21, you lose! Else, you win!\n" \
    "Good luck and may the odds be ever in your favor!\n")

def player_loop(player_turn):
    called_nums = [0]  # start with zero to get last_num

    last_num = called_nums[len(called_nums)-1]  # check for consecutiveness

    if (last_num < 21 and player_turn):

        last_num = called_nums[len(called_nums)-1]

        player_nums = input("Call 1 to 3 consecutive numbers: ").split()

        if not player_nums:
            print("You must enter at least one number!")
        elif len(player_nums) > 3:
            print("You are disqualified!")
            return
        else:
            num1 = int(player_nums[0])
            if num1 != last_num + 1:
                print("You are disqualified!")
                return
            else:
                called_nums.extend([num1])
            if len(player_nums) > 1:
                num2 = int(player_nums[1])
                if num2 != num1 + 1:
                    print("You are disqualified!")
                    return
                else:
                    called_nums.extend([num2])
            else:
                num2 = None
            if len(player_nums) > 2:
                num3 = int(player_nums[2])
                if num3 != num2 + 1:
                    print("You are disqualified!")
                    return
                else:
                    called_nums.extend([num3])
            else:
                num3 = None

        print(called_nums)

    return player_turn

def computer_loop(computer_turn):
    return computer_turn

def game_loop(player_loop, computer_loop):
    player_turn = player_loop()
    computer_turn = computer_loop()

def main():
    description()

if __name__ == "__main__":
    main()
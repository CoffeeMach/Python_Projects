def description():
    print("Welcome to 21 Number Game!\n" \
    "The objective of this game is to not be the one to call 21.\n" \
    "The game is played between you and the computer.\n" \
    "You can call 1 to 3 consecutive numbers in your turn.\n" \
    "Start from 1 and continue upward.\n" \
    "If you are the one to call 21, you lose! Else, you win!\n" \
    "Good luck and may the odds be ever in your favor!\n")

def game_loop():
    called_nums = [0]

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
        if len(player_nums) > 1:
            num2 = int(player_nums[1])
            if num2 != num1 + 1:
                print("You are disqualified!")
                return
        else:
            num2 = None
        if len(player_nums) > 2:
            num3 = int(player_nums[2])
            if num3 != num2 + 1:
                print("You are disqualified!")
                return
        else:
            num3 = None

    called_nums.extend([num1, num2, num3])
    print(called_nums)


def main():
    description()
    game_loop()

if __name__ == "__main__":
    main()
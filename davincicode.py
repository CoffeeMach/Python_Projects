import numpy as np

class Tiles:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        # used with "print" statement
        return f"[{self.color}{self.number}]"
    
    def __repr__(self):
        return f"[{self.color}]"
    
    def reveal_color(self):
        print("[" + self.color + "]", end=" ")

    def reveal_number(self):
        print("[" + self.number + "]", end=" ")

    def reveal(self):
        print("[" + self.color + self.number + "]", end=" ")

def reveal_tiles(display_tiles):
    for tiles in display_tiles:
        tiles.reveal()
    print("\n")

def reveal_colors(display_tiles):
    for tiles in display_tiles:
        tiles.reveal_color()
    print("\n")

def display_player(player_tiles, guess):
    for tiles in player_tiles:
        if int(tiles.number) != guess:
            tiles.reveal_color()
        else:
            tiles.reveal()
    print("\n")

    return player_tiles

def coda_sorting_algo(lst):
    for rng in range (len(lst)-1):
        for index in range (len(lst)-1-rng):
            if int(lst[index].number) > int(lst[index+1].number):
                lst[index], lst[index+1] = lst[index+1], lst[index]
            elif lst[index].number == lst[index+1].number:
                if lst[index].color > lst[index+1].color:
                    lst[index], lst[index+1] = lst[index+1], lst[index]

    return lst

def initialize_game():
    rng = np.random.default_rng()

    white_tiles = np.array([Tiles(color = "W", number = f"{i}") for i in range(12)])
    black_tiles = np.array([Tiles(color = "B", number = f"{i}") for i in range(12)])

    tiles_list = np.concatenate((white_tiles, black_tiles))
    shuffled_tiles_list = rng.permutation(tiles_list)

    print(shuffled_tiles_list)

    return shuffled_tiles_list

def setup(shuffled_tiles_list):
    t1, t2, t3, t4 = [int(x) for x in input("Pick four random tiles: ").split()]

    my_tiles = np.array([shuffled_tiles_list[t1-1], shuffled_tiles_list[t2-1],
                shuffled_tiles_list[t3-1], shuffled_tiles_list[t4-1]])
    
    other_tiles = np.delete(shuffled_tiles_list, [t1-1,t2-1,t3-1,t4-1])
    
    player2_tiles = np.array([other_tiles[0], other_tiles[1],
                other_tiles[2], other_tiles[3]])
    
    player3_tiles = np.array([other_tiles[4], other_tiles[5],
                other_tiles[6], other_tiles[7]])
    
    remaining_tiles = np.delete(other_tiles, [0,1,2,3,4,5,6,7])

    my_tiles = coda_sorting_algo(my_tiles)
    player2_tiles = coda_sorting_algo(player2_tiles)
    player3_tiles = coda_sorting_algo(player3_tiles)

    print("\nYour tiles:", end=" ")
    reveal_tiles(my_tiles)

    print("P2 tiles:", end=" ")
    reveal_tiles(player2_tiles)

    print("P3 tiles:", end=" ")
    display_player(player3_tiles, None)

    print("Remaining tiles:", end=" ")
    display_player(remaining_tiles, None)
    
    return my_tiles, player2_tiles, player3_tiles, remaining_tiles

def standard_play(my_tiles, player2_tiles, player3_tiles, remaining_tiles):
    clue_tile_index = int(input("Pick a clue tile: "))

    my_tiles = np.append(my_tiles, remaining_tiles[clue_tile_index-1])
    remaining_tiles = np.delete(remaining_tiles, clue_tile_index-1)

    print("Your tiles are currently displayed as:", end=" ")
    for tiles in my_tiles:
        tiles.reveal()
    print("\n")

    print("Pick a tile of another player and state the hidden number you think it might be.\n")
    player = input("Enter player as P2 or P3: ")
    tile_index, guess = [int(x) for x in input("Enter tile number and your guess: ").split()]

    match player:
        case "P2":
            if int(player2_tiles[tile_index-1].number) == guess:
                print("You have guessed correctly!")
                print("The opponent will now reveal the tile.\n")

                print("These are the current tiles: ")
                print("Your tiles:", end=" ")
                reveal_tiles(my_tiles)
                print("P2 tiles:", end=" ")
                display_player(player2_tiles, guess)
                print("P3 tiles:", end=" ")
                display_player(player3_tiles, None)
                print("Remaining tiles:", end=" ")
                display_player(remaining_tiles, None)

                answer = input("Do you want to continue guessing? [Y/N]: ")

                if answer == "Y":
                    standard_play(my_tiles, player2_tiles, player3_tiles, remaining_tiles)
                else:
                    my_tiles = coda_sorting_algo(my_tiles)
                    ai_players()
            else:
                print("You have guessed incorrectly! Your clue tile will be revealed to others.")
                my_tiles = coda_sorting_algo(my_tiles)
                ai_players()
        case "P3":
            if int(player3_tiles[tile_index-1].number) == guess:
                print("You have guessed correctly!")
                print("The opponent will now reveal the tile.\n")

                print("These are the current tiles: ")
                print("Your tiles:", end=" ")
                reveal_tiles(my_tiles)
                print("P2 tiles:", end=" ")
                display_player(player2_tiles, None)
                print("P3 tiles:", end=" ")
                display_player(player3_tiles, guess)
                print("Remaining tiles:", end=" ")
                display_player(remaining_tiles, None)

                answer = input("Do you want to continue guessing? [Y/N]: ")

                if answer == "Y":
                    standard_play(my_tiles, player2_tiles, player3_tiles, remaining_tiles)
                else:
                    ai_players()
                    my_tiles = coda_sorting_algo(my_tiles)
            else:
                print("You have guessed incorrectly! Your clue tile will be revealed to others.")
                my_tiles = coda_sorting_algo(my_tiles)
                ai_players()
        case _:
            return


def ai_players():
    print("ais turn")

def main():
    shuffled_tiles_list = initialize_game()
    my_tiles, player2_tiles, player3_tiles, remaining_tiles = setup(shuffled_tiles_list)
    standard_play(my_tiles, player2_tiles, player3_tiles, remaining_tiles)

if __name__ == "__main__":
    main()
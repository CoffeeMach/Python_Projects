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

    print("Your tiles:", end=" ")
    for tiles in my_tiles:
        tiles.reveal()
    print("\n")

    print("P2 tiles:", end=" ")
    for tiles in player2_tiles:
        tiles.reveal_color()
    print("\n")

    print("P3 tiles:", end=" ")
    for tiles in player3_tiles:
        tiles.reveal_color()
    print("\n")

    print("Remaining tiles:", end=" ")
    for tiles in remaining_tiles:
        tiles.reveal_color()
    print("\n")
    
    return my_tiles, player2_tiles, player3_tiles, remaining_tiles

def game_loop():
    return

def ai_players():
    return

def main():
    shuffled_tiles_list = initialize_game()
    my_tiles, player2_tiles, player3_tiles, remaining_tiles = setup(shuffled_tiles_list)

if __name__ == "__main__":
    main()
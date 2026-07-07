import numpy as np

class Tiles:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"[{self.color}{self.number}]"
    
    def __repr__(self):
        return f"[{self.color}]"
    
    def reveal(self):
        print(self.number)

def coda_sorting_algo(lst):
    for index in range(len(lst)-1):
        if lst[index].number <= lst[index+1].number:
            continue
        elif lst[index].number > lst[index+1].number:
            temp = lst[index+1]
            lst[index+1] = lst[index]
            lst[index] = temp
            coda_sorting_algo(lst)

    return lst

def initialize_game():
    rng = np.random.default_rng()

    white_tiles = np.array([Tiles("W", f"{i}") for i in range(12)])
    black_tiles = np.array([Tiles("B", f"{i}") for i in range(12)])

    tiles_list = np.concatenate((white_tiles, black_tiles))
    shuffled_tiles_list = rng.permutation(tiles_list)

    print(shuffled_tiles_list)

    return shuffled_tiles_list

def setup(shuffled_tiles_list):
    t1, t2, t3, t4 = [int(x) for x in input("Pick four random tiles: ").split()]

    my_tiles = np.array([f'{shuffled_tiles_list[t1-1]}', f'{shuffled_tiles_list[t2-1]}',
                f'{shuffled_tiles_list[t3-1]}', f'{shuffled_tiles_list[t4-1]}'])

    other_tiles = np.delete(shuffled_tiles_list, [t1-1,t2-1,t3-1,t4-1])
    
    player2_tiles = np.array([other_tiles[0], other_tiles[1],
                other_tiles[2], other_tiles[3]])
    
    player3_tiles = np.array([other_tiles[4], other_tiles[5],
                other_tiles[6], other_tiles[7]])
    
    remaining_tiles = np.delete(other_tiles, [0,1,2,3,4,5,6,7])

    # my_tiles = coda_sorting_algo(my_tiles)
    player2_tiles = coda_sorting_algo(player2_tiles)
    player3_tiles = coda_sorting_algo(player3_tiles)

    print(f" Your tiles: {my_tiles}\n",f"Tiles of p2: {player2_tiles}\n",
          f"Tiles of p3: {player3_tiles}\n\n",f"Remaining tiles: {remaining_tiles}")
    
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
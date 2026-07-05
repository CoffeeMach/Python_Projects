import numpy as np

class Tiles:
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.is_scramble = False

    def __str__(self):
        return f"[{self.color}{self.number}]"
    
    def __repr__(self):
        return f"[{self.color}]"
    
    def reveal(self):
        print(self.number)

def initialize_game():
    rng = np.random.default_rng()

    white_tiles = np.array([Tiles("W", f"{i}") for i in range(12)])
    black_tiles = np.array([Tiles("B", f"{i}") for i in range(12)])
    scramble_tiles = np.array([Tiles("W", "-"), Tiles("B", "-")])

    tiles_list = np.concatenate((white_tiles, black_tiles, scramble_tiles))
    shuffled_tiles_list = rng.permutation(tiles_list)

    print(shuffled_tiles_list)

    t1, t2, t3, t4 = [int(x) for x in input("Pick four random tiles: ").split()]

    my_tiles = np.array([f'{shuffled_tiles_list[t1-1]}', f'{shuffled_tiles_list[t2-1]}',
                f'{shuffled_tiles_list[t3-1]}', f'{shuffled_tiles_list[t4-1]}'])

    other_tiles = np.delete(shuffled_tiles_list, [t1-1,t2-1,t3-1,t4-1])
    
    player2_tiles = np.array([other_tiles[0], other_tiles[1],
                other_tiles[2], other_tiles[3]])
    
    player3_tiles = np.array([other_tiles[4], other_tiles[5],
                other_tiles[6], other_tiles[7]])
    
    middle_tiles = np.delete(other_tiles, [0,1,2,3,4,5,6,7])
    
    print(f" Your tiles: {my_tiles}\n",f"Tiles of p2: {player2_tiles}\n",
          f"Tiles of p3: {player3_tiles}\n\n",f"Remaining tiles: {middle_tiles}")

def main():
    initialize_game()

if __name__ == "__main__":
    main()
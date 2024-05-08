import random, copy

turn = {
    0: 'x',
    1: 'o'
}

wins = {
    'x': 0,
    'o': 0,
    'draw': 0
}

max_length = 5


class Game:

    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.move_num = 0

    def get_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == None]

    def make_move(self, move):
        player = turn[self.move_num % 2]
        self.board[move[0]][move[1]] = Mark(player)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != None and self.board[i][j].player == player:
                    self.board[i][j].increment()

                if self.board[i][j] != None and self.board[i][j].expired():
                    self.board[i][j] = None

        self.move_num += 1

    def is_over(self):

        for i in range(3):
            if self.board[i][0] != None and self.board[i][1] != None and self.board[i][2] != None:
                if self.board[i][0].player == self.board[i][1].player == self.board[i][2].player:
                    wins[self.board[i][0].player] += 1
                    return True

            if self.board[0][i] != None and self.board[1][i] != None and self.board[2][i] != None:
                if self.board[0][i].player == self.board[1][i].player == self.board[2][i].player:
                    wins[self.board[0][i].player] += 1
                    return True

        if self.board[0][0] != None and self.board[1][1] != None and self.board[2][2] != None:
            if self.board[0][0].player == self.board[1][1].player == self.board[2][2].player:
                wins[self.board[0][0].player] += 1
                return True

        if self.board[0][2] != None and self.board[1][1] != None and self.board[2][0] != None:
            if self.board[0][2].player == self.board[1][1].player == self.board[2][0].player:
                wins[self.board[0][2].player] += 1
                return True

        if self.move_num > max_length:
            wins['draw'] += 1
            return True

        return False

    def __str__(self):
        return '\n'+'\n--------------\n'.join([' | '.join([str(cell) if cell != None else '   ' for cell in row]) for row in self.board])+'\n'


class Mark:

    def __init__(self, player):
        self.player = player
        self.age = 0

    def increment(self):
        self.age += 1

    def expired(self):
        return self.age > 3

    def __str__(self):
        return f"{self.player} {self.age}"


def play_game():
    game = Game()

    while True:
        moves = game.get_moves()
        for i in range(len(moves)):
            print(f"{i} {moves[i]}")

        player_input = input("Enter move: ")

        if player_input == 'q':
            break

        choice = int(player_input)

        game.make_move(moves[choice])

        print(game)

        if game.is_over():
            print(f"game lasted {game.move_num} moves")
            print(wins)
            break


def simulate_game(num_sims):
    for i in range(num_sims):
        game = Game()

        while True:
            moves = game.get_moves()
            i = random.randint(0, len(moves) - 1)
            move = moves[i]
            game.make_move(move)
            if game.is_over():
                break

    print(wins)


def recursive_simulate_game():
    init_game = Game()

    def lmao(game):
        if game.is_over():
            return

        moves = game.get_moves()
        for move in moves:
            new_game = copy.deepcopy(game)
            new_game.make_move(move)
            lmao(new_game)

    lmao(init_game)
    print(wins)


def main():

    while True:
        print("1 Simulate game")
        print("2 Recursively Simulate game")
        print("3 Play game")
        print("4 Settings")

        player_input = input("Enter choice: ")

        if player_input == 'q':
            break

        try:
            choice = int(player_input)
        except:
            print("Invalid input")
            continue

        if choice == 1:
            num_sims = int(input("Enter number of simulations: "))
            simulate_game(num_sims)

        if choice == 2:
            recursive_simulate_game()

        if choice == 3:
            play_game()

        if choice == 4:
            print("1 Set Move Limit")

            player_input = input("Enter choice: ")
            if player_input == 'q':
                continue

            choice = int(player_input)

            if choice == 1:
                global max_length
                max_length = int(input("Enter new move limit: "))

        wins['x'] = 0
        wins['o'] = 0
        wins['draw'] = 0

main()

#{'x': 1440, 'o': 5328, 'draw': 49392}
#{'x': 1440, 'o': 5328, 'draw': 49392}

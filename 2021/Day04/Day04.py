import numpy as np


class BingoBoard:
    def __init__(self, board_size, id):
        self.board_id = id
        self.board_size = board_size
        self.empty_line = 0
        self.win = False
        self.board_hits = np.zeros([board_size, board_size])
        self.board_nums = np.zeros([board_size, board_size])

    def add_board_line(self, line):
        self.board_nums[:, self.empty_line] = [int(x) for x in line.strip().split()]
        self.empty_line += 1

    def dab(self, number):
        if number in self.board_nums:
            x_list, y_list = np.where(self.board_nums == number)
            for x, y in zip(x_list, y_list):
                self.board_hits[x][y] = 1
            return self.check_win()
        return False

    def check_win(self):
        if self.board_size in np.sum(self.board_hits, 1) or self.board_size in np.sum(
            self.board_hits, 0
        ):
            return True


def play_bingo(boards, game, goal):
    win_count = 0
    number_to_play = 0
    iter_game = iter(game)
    called_num = next(iter_game)
    while win_count < len(boards):
        for b in boards:
            if b.dab(called_num):
                score = int(
                    called_num
                    * np.sum(np.sum(b.board_nums * (b.board_hits == 0), 1), 0)
                )
                if b.win != True:
                    print(f"Board {b.board_id} won with score: {score}")
                    win_count += 1
                    b.win = True
                if goal == "win":
                    return score
        try:
            called_num = next(iter_game)
        except:
            break
    return score


if __name__ == "__main__":
    # initialize boards
    with open("Day04input.txt", "r") as f:
        game = [int(x) for x in f.readline().strip().split(",")]

        boards = []
        id = 0
        list = f.readlines()
        for line in list:
            if len(line) < 5:
                print(f"made new board id:{id}")
                boards.append(BingoBoard(5, id))
                id += 1
            else:
                boards[-1].add_board_line(line)

    play_bingo(boards, game, "win")
    play_bingo(boards, game, "lose")

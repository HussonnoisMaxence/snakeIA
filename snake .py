UP = 1
RIGHT = 2
DOWN = -1
LEFT = -2

class Snake:

    def __init__(self, width = 30, height = 20):
        self.height = height
        self.width = width
        self.turn_until_size_up = 10
        self.turn = 0

        self.snake1 = [[2, self.height // 2]]
        self.snake2 = [[self.width - 3, self.height // 2]]
        self.dir1 = RIGHT
        self.dir2 = LEFT

        self.board = [0] * self.width
        for i in range(0, self.width):
            self.board[i] = [0] * self.height

        for i in range(0, self.width):
            for j in range(0, self.height):
                if(i == 0 or j == 0 or i == self.width - 1 or j == self.height - 1):
                    self.board[i][j] = 1

    def display(self):

        print(chr(27) + "[2J")

        for j in range(0, self.height):
            for i in range(0, self.width):

                if(self.board[i][j] == 1):
                    print("\033[0;37;47m \033[0m", end = "")

                elif([i, j] in self.snake1):
                    if(self.snake1.index([i, j]) == 0):
                        print("\033[0;37;46mX\033[0m", end = "")
                    else:
                        print("\033[0;37;46m \033[0m", end = "")

                elif([i, j] in self.snake2):
                    if(self.snake2.index([i, j]) == 0):
                        print("\033[0;37;41mX\033[0m", end = "")
                    else:
                        print("\033[0;37;41m \033[0m", end = "")

                else:
                    print(" ", end = "")

            print("")


    def move(self, dir_snake1, dir_snake2):

        size = len(self.snake1)

        if(dir_snake1 != -self.dir1 and dir_snake1 != 0):
            self.dir1 = dir_snake1

        if(dir_snake2 != -self.dir2 and dir_snake2 != 0):
            self.dir2 = dir_snake2

        if(self.dir1 == UP):
            pos = [self.snake1[0][0], self.snake1[0][1] - 1]
        if(self.dir1 == RIGHT):
            pos = [self.snake1[0][0] + 1, self.snake1[0][1]]
        if(self.dir1 == DOWN):
            pos = [self.snake1[0][0], self.snake1[0][1] + 1]
        if(self.dir1 == LEFT):
            pos = [self.snake1[0][0] - 1, self.snake1[0][1]]

        self.snake1.insert(0, pos)

        if(self.dir2 == UP):
            pos = [self.snake2[0][0], self.snake2[0][1] - 1]
        if(self.dir2 == RIGHT):
            pos = [self.snake2[0][0] + 1, self.snake2[0][1]]
        if(self.dir2 == DOWN):
            pos = [self.snake2[0][0], self.snake2[0][1] + 1]
        if(self.dir2 == LEFT):
            pos = [self.snake2[0][0] - 1, self.snake2[0][1]]

        self.snake2.insert(0, pos)

        self.turn += 1
        if(self.turn % self.turn_until_size_up != 0):
            self.snake1.pop(size)
            self.snake2.pop(size)

        if(self.check()):
            return 1

        return 0

    def check(self):

        p1 = 0
        p2 = 0

        if(self.board[self.snake1[0][0]][self.snake1[0][1]] == 1 or [self.snake1[0][0], self.snake1[0][1]] in self.snake1[1:] or [self.snake1[0][0], self.snake1[0][1]] in self.snake2):
            p1 = 1

        if(self.board[self.snake2[0][0]][self.snake2[0][1]] == 1 or [self.snake2[0][0], self.snake2[0][1]] in self.snake2[1:] or [self.snake2[0][0], self.snake2[0][1]] in self.snake1):
            p2 = 1

        if(p1 != 0 or p2 != 0):
            if(p1 == 1 and p2 == 1):
                print("No winner !")
            elif(p1 == 1):
                print("Player 2 win !")
            elif(p2 == 1):
                print("Player 1 win !")

            return 1

        return 0

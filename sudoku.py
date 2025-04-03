import random
import copy

class Sudoku:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = None
        self.difficulty = None

    def generate_puzzle(self, difficulty='medium'):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        
        self._fill_diagonal_boxes()
        
        self._solve_board()
        
        self.solution = copy.deepcopy(self.board)
        
        self._create_puzzle(difficulty)
        self.difficulty = difficulty
        
        return self.board
    
    def _fill_diagonal_boxes(self):
        for box in range(0, 9, 3):
            self._fill_box(box, box)
    
    def _fill_box(self, row, col):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.board[row + i][col + j] = nums.pop()
    
    def _is_safe(self, row, col, num):
        for x in range(9):
            if self.board[row][x] == num:
                return False
        
        for x in range(9):
            if self.board[x][col] == num:
                return False
        
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        
        return True
    
    def _solve_board(self):
        empty_cell = self._find_empty()
        if not empty_cell:
            return True
        
        row, col = empty_cell
        
        for num in range(1, 10):
            if self._is_safe(row, col, num):
                self.board[row][col] = num
                
                if self._solve_board():
                    return True
                
                self.board[row][col] = 0
        
        return False
    
    def _find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def _create_puzzle(self, difficulty):
        if difficulty == 'easy':
            cells_to_remove = random.randint(30, 35)
        elif difficulty == 'medium':
            cells_to_remove = random.randint(40, 45)
        elif difficulty == 'hard':
            cells_to_remove = random.randint(50, 55)
        else:
            cells_to_remove = random.randint(55, 60)
        
        positions = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(positions)
        
        for i in range(cells_to_remove):
            if i < len(positions):
                row, col = positions[i]
                self.board[row][col] = 0
    
    def is_valid_move(self, row, col, num):
        if self.board[row][col] != 0:
            return False
        
        temp = self.board[row][col]
        self.board[row][col] = 0
        
        valid = self._is_safe(row, col, num)
        
        self.board[row][col] = temp
        
        return valid
    
    def make_move(self, row, col, num):
        if not (0 <= row < 9 and 0 <= col < 9):
            return False, "Invalid position"
        
        if not (1 <= num <= 9):
            return False, "Number must be between 1 and 9"
        
        if self.board[row][col] != 0:
            return False, "Cell is already filled"
        
        if not self.is_valid_move(row, col, num):
            return False, "Invalid move"
        
        self.board[row][col] = num
        return True, "Move successful"
    
    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
                
        return self._is_valid_solution()
    
    def _is_valid_solution(self):
        for row in range(9):
            if set(self.board[row]) != set(range(1, 10)):
                return False
        
        for col in range(9):
            if set(self.board[i][col] for i in range(9)) != set(range(1, 10)):
                return False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_values = []
                for i in range(3):
                    for j in range(3):
                        box_values.append(self.board[box_row + i][box_col + j])
                if set(box_values) != set(range(1, 10)):
                    return False
        
        return True
    
    def get_hint(self):
        if not self.solution:
            return None
        
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    empty_cells.append((i, j))
        
        if not empty_cells:
            return None
        
        row, col = random.choice(empty_cells)
        value = self.solution[row][col]
        
        self.board[row][col] = value
        
        return (row, col, value)
    
    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                
                if self.board[i][j] == 0:
                    print(".", end=" ")
                else:
                    print(self.board[i][j], end=" ")
            
            print()

class SudokuGame:
    def __init__(self):
        self.sudoku = Sudoku()
        self.current_puzzle = None
        self.start_time = None
    
    def new_game(self, difficulty='medium'):
        import time
        self.current_puzzle = self.sudoku.generate_puzzle(difficulty)
        self.start_time = time.time()
        print(f"New {difficulty} game started!")
        self.sudoku.print_board()
    
    def make_move(self, row, col, num):
        success, message = self.sudoku.make_move(row, col, num)
        print(message)
        
        if success:
            self.sudoku.print_board()
            
            if self.sudoku.is_solved():
                import time
                elapsed_time = time.time() - self.start_time
                minutes, seconds = divmod(int(elapsed_time), 60)
                print(f"Congratulations! You solved the puzzle in {minutes}m {seconds}s!")
                return True
        
        return False
    
    def get_hint(self):
        hint = self.sudoku.get_hint()
        
        if hint:
            row, col, value = hint
            print(f"Hint: {value} at position ({row+1},{col+1})")
            self.sudoku.print_board()
            
            if self.sudoku.is_solved():
                print("Puzzle solved with hints!")
                return True
        else:
            print("No hints available or puzzle is solved!")
        
        return False
    
    def check_solution(self):
        if self.sudoku.is_solved():
            print("The puzzle is solved correctly!")
            return True
        else:
            print("The puzzle is not solved yet or has errors.")
            return False

if __name__ == "__main__":
    game = SudokuGame()
    
    print("Welcome to Sudoku!")
    print("1. New Game")
    print("2. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Select difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Very Hard")
        
        diff_choice = input("Enter your choice: ")
        difficulty = {
            "1": "easy",
            "2": "medium",
            "3": "hard",
            "4": "very hard"
        }.get(diff_choice, "medium")
        
        game.new_game(difficulty)
        
        while True:
            print("\nCommands:")
            print("- move <row> <col> <num>: Make a move")
            print("- hint: Get a hint")
            print("- check: Check if puzzle is solved")
            print("- print: Print the current board")
            print("- exit: Quit the game")
            
            cmd = input("\nEnter command: ").strip().lower()
            
            if cmd.startswith("move"):
                try:
                    _, row, col, num = cmd.split()
                    solved = game.make_move(int(row)-1, int(col)-1, int(num))
                    if solved:
                        break
                except ValueError:
                    print("Invalid input. Format: move <row> <col> <num>")
            
            elif cmd == "hint":
                solved = game.get_hint()
                if solved:
                    break
            
            elif cmd == "check":
                game.check_solution()
            
            elif cmd == "print":
                game.sudoku.print_board()
            
            elif cmd == "exit":
                print("Thanks for playing!")
                break
            
            else:
                print("Unknown command.")
    
    else:
        print("Thanks for playing!")

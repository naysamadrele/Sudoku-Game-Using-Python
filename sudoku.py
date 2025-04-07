from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import copy
import time

app = Flask(__name__)
CORS(app)

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
    
    def to_dict(self):
        return {
            'board': self.board,
            'solution': self.solution,
            'difficulty': self.difficulty,
            'game_over': self.is_solved()
        }

sudoku = Sudoku()

@app.route('/start', methods=['POST'])
def start_game():
    data = request.json
    difficulty = data.get('difficulty', 'medium')
    board = sudoku.generate_puzzle(difficulty)
    return jsonify(sudoku.to_dict()), 200

@app.route('/move', methods=['POST'])
def make_move():
    data = request.json
    row = data['row']
    col = data['col']
    num = data['num']
    success, message = sudoku.make_move(row, col, num)
    return jsonify({'success': success, 'message': message, 'game': sudoku.to_dict()}), 200

@app.route('/hint', methods=['GET'])
def get_hint():
    hint = sudoku.get_hint()
    return jsonify({'hint': hint, 'game': sudoku.to_dict()}), 200

if __name__ == '__main__':
    app.run(debug=True)
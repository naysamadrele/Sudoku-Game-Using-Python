<h1 align="center">🧩 Sudoku Solver using Backtracking Algorithm</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python">
  <img src="https://img.shields.io/badge/Algorithm-Backtracking-yellow?logo=python">
  <img src="https://img.shields.io/badge/NumPy-Matrix_Operations-yellow?logo=numpy">
</p>

<p align="center">
  🧠 Solves Sudoku puzzles using a backtracking algorithm in Python!
</p>

---

## 🌟 Overview

This project implements a **Sudoku Solver** using the **backtracking algorithm**, which fills the empty cells of a 9x9 Sudoku grid while ensuring that the solution is valid. The algorithm tries to place numbers 1–9 in each empty spot while checking that they do not conflict with existing numbers in the same row, column, or 3x3 subgrid.

---

## 🎯 Features

✅ Solves 9x9 Sudoku puzzles  
✅ Backtracking algorithm for solution  
✅ Easy-to-understand code  
✅ Can be used with any valid Sudoku puzzle (unsolved grid with numbers 0–9)  
✅ Visualizes the solved grid

---

## 📂 File Structure

sudoku-solver/
├── solve_sudoku.py # Main script
├── example_input.txt # Input Sudoku puzzle (unsolved grid)
├── solved_output.txt # Output solved Sudoku puzzle
└── README.md # This file

yaml
Copy
Edit

---

## 🧑‍💻 How to Run the Script

### 🛠️ Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver
🐍 Step 2: Set Up Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
📦 Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
▶️ Step 4: Run the Script
bash
Copy
Edit
python solve_sudoku.py
Output:

Displays the solved Sudoku puzzle.

Saves the solved grid as solved_output.txt.

📈 Algorithm Explanation
Backtracking: Tries placing each number (1–9) in empty spots one by one and checks if it leads to a valid solution. If it does not, it "backtracks" and tries a different number.

Validation: Ensures the number does not violate Sudoku rules (no repeats in rows, columns, or subgrids).

Recursion: The process repeats itself until the entire grid is filled or no valid configuration exists.

🧪 Example Input and Output
Input Sudoku Puzzle (example_input.txt):

Copy
Edit
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
Output Sudoku Puzzle (solved_output.txt):

Copy
Edit
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
📦 requirements.txt
txt
Copy
Edit
numpy
📝 Notes
The Sudoku grid should be in a text file format with zeros (0) representing empty cells.

The solution is written to the solved_output.txt file.

The algorithm is based on a backtracking technique, which ensures all Sudoku rules are respected while solving the puzzle.

❤️ Credits
NumPy for matrix operations and handling arrays.

document.getElementById('start-game').addEventListener('click', async () => {
    const difficulty = document.getElementById('difficulty').value;
    const response = await fetch('http://127.0.0.1:5000/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ difficulty })
    });
    const gameData = await response.json();
    renderBoard(gameData);
});

async function makeMove(row, col, num) {
    const response = await fetch('http://127.0.0.1:5000/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ row, col, num })
    });
    const gameData = await response.json();
    document.getElementById('game-message').textContent = gameData.message;
    renderBoard(gameData.game);
    if (gameData.game.game_over) {
        document.getElementById('game-message').textContent = 'Congratulations! You solved the puzzle!';
    }
}

async function getHint() {
    const response = await fetch('http://127.0.0.1:5000/hint');
    const gameData = await response.json();
    renderBoard(gameData.game);
    if (gameData.hint) {
        const [row, col, value] = gameData.hint;
        document.getElementById('game-message').textContent = `Hint: ${value} at position (${row + 1}, ${col + 1})`;
    } else {
        document.getElementById('game-message').textContent = 'No hints available or puzzle is already solved!';
    }
}

function renderBoard(game) {
    const boardElement = document.getElementById('board');
    boardElement.innerHTML = '';
    for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
            const cellElement = document.createElement('div');
            cellElement.classList.add('cell');
            if (game.board[row][col] !== 0) {
                cellElement.classList.add('fixed');
                cellElement.textContent = game.board[row][col];
            } else {
                cellElement.addEventListener('click', () => {
                    const num = prompt('Enter a number (1-9):');
                    if (num >= 1 && num <= 9) {
                        makeMove(row, col, parseInt(num));
                    }
                });
            }
            boardElement.appendChild(cellElement);
        }
    }
}
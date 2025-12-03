// let currentPlayer = 'X';
// const cells = document.querySelectorAll('.cell');
// const resetButton = document.querySelector('.reset-button');
// const resultMessage = document.getElementById('result-message');
// const winnerName = document.getElementById('winner-name');

// // Initialize the game board
// const board = Array(9).fill(null);

// // Function to check for a win
// function checkWin() {
//     const winningCombos = [
//         [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
//         [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
//         [0, 4, 8], [2, 4, 6]             // Diagonals
//     ];

//     for (const combo of winningCombos) {
//         const [a, b, c] = combo;
//         if (board[a] && board[a] === board[b] && board[a] === board[c]) {
//             // Show the winner message
//             resultMessage.classList.remove('d-none');
//             winnerName.textContent = board[a];
//             return true;
//         }
//     }

//     // Check for a draw
//     if (!board.includes(null)) {
//         resultMessage.classList.remove('d-none');
//         winnerName.textContent = "تعادل!";
//         return true;
//     }

//     return false;
// }

// // Function to handle cell click
// cells.forEach((cell, index) => {
//     cell.addEventListener('click', () => {
//         if (board[index] || checkWin()) return;

//         board[index] = currentPlayer;
//         cell.textContent = currentPlayer;

//         if (checkWin()) return;

//         currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
//     });
// });

// // Function to reset the game
// function resetGame() {
//     board.fill(null);
//     cells.forEach(cell => {
//         cell.textContent = '';
//     });
//     currentPlayer = 'X';

//     // Hide the result message
//     resultMessage.classList.add('d-none');
// }

// // Add event listener to the reset button
// resetButton.addEventListener('click', resetGame);
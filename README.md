README.md
# Tic Tac Toe & Connect 4 with AI

This is a **web-based game project** featuring **Tic Tac Toe** and **Connect 4**, both playable against an AI using the **Minimax algorithm** (Tic Tac Toe) or random moves (Connect 4). Built with **Python Flask** and a modern **single-page HTML interface**.

---

## Features

- **Tic Tac Toe** with:
  - Easy, Medium, Hard difficulty
  - AI powered by Minimax with alpha-beta pruning
- **Connect 4** with:
  - Easy, Medium, Hard difficulty (AI currently random)
- Modern **single-page UI** with interactive grid
- Reset game and change difficulty dynamically
- No external templates required, all HTML, CSS, and JS in one file

---

## Project Structure



tic_tac_toe_project/
├─ app.py # Flask backend
├─ tic_tac_toe.py # Tic Tac Toe AI logic
├─ connect_4.py # Connect 4 AI logic
├─ index.html # Frontend UI
├─ README.md # Project documentation
├─ .gitignore # Git ignore file


---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/motsem021/tic_tac_toe_using_min_max_algo.git
cd tic_tac_toe_using_min_max_algo


Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install Flask:

pip install flask

Running the Project

Start the Flask server:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Click Tic Tac Toe or Connect 4 to start playing.

Select difficulty and reset the game using the controls.

Future Improvements

Implement Minimax AI for Connect 4

Add animations and sound effects

Add dark mode toggle

Deploy as a live web app

License

This project is open-source and free to use.

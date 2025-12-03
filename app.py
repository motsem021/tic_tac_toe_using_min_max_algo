# app.py
from flask import Flask, request, jsonify, send_file
import tic_tac_toe
import connect_4

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/tictactoe/move', methods=['POST'])
def tictactoe_move():
    data = request.get_json()
    board = data.get('board')
    player = data.get('player')
    difficulty = data.get('difficulty','medium')
    if board is None or player is None:
        return jsonify({'error':'Missing board or player'}),400
    move = tic_tac_toe.find_best_move_tic_tac_toe(board, player, difficulty)
    return jsonify({'move':move})

@app.route('/connect4/move', methods=['POST'])
def connect4_move():
    data = request.get_json()
    board = data.get('board')
    player = data.get('player')
    difficulty = data.get('difficulty','medium')
    if board is None or player is None:
        return jsonify({'error':'Missing board or player'}),400
    move = connect_4.find_best_move_connect4(board, player, difficulty)
    return jsonify({'move':move})

if __name__=='__main__':
    app.run(debug=True)

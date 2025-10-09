## Main function
```
function main():
    board = [" " for each of 9 positions]
    display_board(board)
    
    input player_symbol = "Choose your symbol (X/O): "
    computer_symbol = "O" IF player_symbol == "X" ELSE "X"
    
    current_turn = "Player"
    
    while True:
        if current_turn == "Player":
            input move = "Enter position (1-9): " -1 to get the index
            if move in range(0,9) and board[move] == " ":
                board[move] = player_symbol
            else:
                print "Invalid move. Try again."
                continue
        else:
            move = get_computer_move(board)
            place_move(board, move, computer_symbol)
        
        display_board(board)
        
        if check_winner(board, current_turn == "Player" ? player_symbol : computer_symbol):
            print current_turn + " wins!"
            break
        
        if " " not in board anymore:
            print "It's a draw!"
            break
        
        current_turn = "Computer" if current_turn == "Player" else "Player"
    
    print "Game Over."
```

## Display the board
```
function display_board(board):
    print board[0] + "|" + board[1] + "|" + board[2]
    print "-+-+-"
    print board[3] + "|" + board[4] + "|" + board[5]
    print "-+-+-"
    print board[6] + "|" + board[7] + "|" + board[8]
```

## Get computer move (return random valid move)
```
function get_computer_move(board):
    empty_positions = indices of board where cell == " "
    return random choice from empty_positions
```
### Alternative: Choose computer move out of prededefined winning combinations
```
function get_computer_move(board, computer_symbol, player_symbol):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    # 1. Try to win
    for each combo in winning_combinations:
        cells = values of board at combo positions
        if cells contain 2 of computer_symbol and 1 empty space:
            return position of empty space in combo
    
    # 2. Try to block player's win
    for each combo in winning_combinations:
        cells = values of board at combo positions
        if cells contain 2 of player_symbol and 1 empty space:
            return position of empty space in combo
    
    # 3. Choose best strategic position
    if center position (index 4) is empty:
        return 4
    
    for each corner in [0, 2, 6, 8]:
        if board[corner] is empty:
            return corner
    
    for each side in [1, 3, 5, 7]:
        if board[side] is empty:
            return side
```

## Check for winner
```
function check_winner(board, symbol):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for each combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False
```
import random

def display_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")


# def get_computer_move(board):
#     empty_positions = [i for i, cell in enumerate(board) if cell == " "]
#     return random.choice(empty_positions)

def get_computer_move(board, computer_symbol, player_symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    # search for winning combination
    for combo in winning_combinations:
        cells = [board[i] for i in combo]
        if cells.count(computer_symbol) == 2 and cells.count(" ") == 1:
            return combo[cells.index(" ")]

    # search for blocking combination
    for combo in winning_combinations:
        cells = [board[i] for i in combo]
        if cells.count(player_symbol) == 2 and cells.count(" ") == 1:
            return combo[cells.index(" ")]
    
    # else return random choice
    empty_positions = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_positions)


def check_winner(board, symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    # return true if one of current combinations is a winning combination
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False


def main():
    board = [" " for _ in range(9)]
    print("Ready for a game of Tic-Tac-Toe?")

    # choose symbol
    player_symbol = input("Choose your symbol (X/O): ").upper()
    while player_symbol not in ["X", "O"]:
        player_symbol = input("Invalid choice. Please choose X or O: ").upper()

    computer_symbol = "O" if player_symbol == "X" else "X"
    current_turn = "Player"
    
    # print available positions
    print("The board looks like this. Place your symbol in a field by choosing a number between 1 and 9.")
    display_board([i for i in range(9)])
    print("Ready? Let's play!")

    while True:
        # Player move
        if current_turn == "Player":
            try:
                move = int(input("Enter position (1-9): ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            # place move
            if move in range(0, 9) and board[move] == " ":
                board[move] = player_symbol
            else:
                print("Invalid move. Try again.")
                continue
        # Computer move
        else:
            move = get_computer_move(board, computer_symbol, player_symbol)
            board[move] = computer_symbol
            print(f"Computer chose position {move + 1}")

        # display board after each move
        display_board(board)

        # check whether someone has won
        symbol_to_check = player_symbol if current_turn == "Player" else computer_symbol
        if check_winner(board, symbol_to_check):
            print(f"{current_turn} wins!")
            break

        # check whether it's a draw
        if " " not in board:
            print("It's a draw!")
            break

        # switch turn
        current_turn = "Computer" if current_turn == "Player" else "Player"

    print("Game Over.")


if __name__ == "__main__":
    main()

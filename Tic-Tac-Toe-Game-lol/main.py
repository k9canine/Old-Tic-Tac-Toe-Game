board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

def display_board(board):
  top_row = board[0:3]
  middle_row = board[3:6]
  bottom_row = board[6:9]
  print(' | '.join(top_row))
  print(' | '.join(middle_row))
  print(' | '.join(bottom_row))

def place_x(board, location): #location should be entered using 1-9
  if board[location-1] == '-':
    board[location-1] = 'X'
  else:
    location = int(input("That spot is taken. Choose an available position from 1-9: "))
    place_x(board, location)

def place_o(board, location): #location uses 1-9 rather than 0-8
  if board[location-1] == '-':
    board[location-1] = 'O'
  else:
    location = int(input("That spot is taken. Choose an available position from 1-9: "))
    place_o(board, location)

def check_win(board):
  #columns 
  if board[0] != '-' and board[0] == board[3] == board[6]:
    return board[0]
  if board[1] != '-' and board[1] == board[4] == board[7]:
    return board[1]
  if board[2] != '-' and board[2] == board[5] == board[8]:
    return board[2]
  #rows
  if board[0] != '-' and board[0] == board[1] == board[2]:
    return board[0]
  if board[3] != '-' and board[3] == board[4] == board[5]:
    return board[3]
  if board[6] != '-' and board[6] == board[7] == board[8]:
    return board[6]
  #diagonals
  if board[0] != '-' and board[0] == board[4] == board[8]:
    return board[0]     
  if board[2] != '-' and board[2] == board[4] == board[6]:
    return board[2]

  return None

def check_tie(board):
  for space in board:
    if space == '-':
      return False
  return True

def start_game(board):
  ocounter = 0
  xcounter = 0

  display_board(board)
  print('')

  while check_win(board) == None and check_tie(board) == False:
    while True:
      if ocounter == xcounter: #let player O go
        placement = input("Player O's turn. Choose a position from 1-9: ")
        available_choices = [str(x) for x in range(1, 10)]
        if placement in available_choices:
          placement = int(placement)
        else:
          print("Invalid position.")
          continue
        place_o(board, placement)
        
        ocounter += 1
        display_board(board)
        print('')
        break
      else: #otherwise, ocounter must be greater than xcounter; let player X make a move
        placement = input("Player X's turn. Choose a position from 1-9: ")
        available_choices = [str(x) for x in range(1, 10)]
        if placement in available_choices:
          placement = int(placement)
        else:
          print("Invalid position.")
          continue
        place_x(board, placement)

        xcounter += 1
        display_board(board)
        print('')
        break

  if check_win(board) == None:
    print("Tie Game")
  else:
    winner = check_win(board)
    print("Player " + winner + " wins!")

  #while loop (while no win or tie), counter for O and X = 0, if O <= X, input for O, place_o(board, input), increase counter, check win/tie


  #start with O
  #go to X
  #check win/tie

start_game(board)
# import data
import requests
import json
def get_prediction(data):
  url = 'https://06el0zvnri.execute-api.us-east-1.amazonaws.com/Predict/f0f2c065-611e-4922-8e7b-84c2000c7f76'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  

  index = response.find("predicted_label")
  response = response[index+len("preidcted_label")+6:]
  index = response.find("\\")
  response = response[:index]
  return response

def getRowCol(num):
  if(num<4): 
    row = 1
    col = num
  elif (num<7):
    row = 2
    col = num-3 
  else:
    row = 3
    col = num - 6
  return [row-1,col-1]

def getIntValue(num):
  if(num=="One"): return 1
  elif(num=="Two"): return 2
  elif(num=="Three"): return 3
  elif(num=="Four"): return 4
  elif(num=="Five"): return 5
  elif(num=="Six"): return 6
  elif(num=="Seven"): return 7
  elif(num=="Eight"): return 8
  return 9

def isValid(num, ticTacToeBoard):
  num = getRowCol(num)
  row = num[0]
  col = num[1]

  if(ticTacToeBoard[row][col]==" "): return True
  return False

def makeMove(ticTacToeOpponent, ticTacToeBoard):
  num = getIntValue(get_prediction(ticTacToeOpponent))

  counter = 0
  while(isValid(num, ticTacToeBoard)==False and counter<=15):
    num = getIntValue(get_prediction(ticTacToeOpponent))
    counter+=1

  if(isValid(num,ticTacToeBoard)==True):
    row = getRowCol(num)[0]
    col = getRowCol(num)[1]

    rowColNum = [row,col,num]
    return rowColNum
  else:
    return -1

def getMe(ticTacToeOpponent, ticTacToeBoard):
  move = makeMove(ticTacToeOpponent, ticTacToeBoard)
  if(move==-1): return -1
  row = move[0]
  col = move[1]
  num = move[2]
  string = "Cell "+str(num)
  ticTacToeOpponent[string] = "opponent"
  ticTacToeBoard[row][col] = "O" 
  return 1

def getOpponent(ticTacToeOpponent, ticTacToeBoard, row, col):
  num = (3*(row-1)+col)-1
  ticTacToeOpponent["Cell "+str(num)] = "opponent"
  ticTacToeBoard[row-1][col-1] = "X"

def printBoard(ticTacToeBoard):
  print("--- --- ---")
  for x in range(3):
    print("|"+ ticTacToeBoard[x][0]+"| |" + ticTacToeBoard[x][1]+"| |" + ticTacToeBoard[x][2]+"|")
    print("--- --- ---")
  print("\n")

def checkWin(ticTacToeBoard):
  if(checkDiagonal(ticTacToeBoard)==True): return True
  elif(checkRows(ticTacToeBoard)==True): return True
  elif(checkCols(ticTacToeBoard)==True): return True
  return False

def checkDiagonal(ticTacToeBoard):
  if (ticTacToeBoard[0][0]==ticTacToeBoard[1][1] and ticTacToeBoard[0][0]==ticTacToeBoard[2][2]):
    if(ticTacToeBoard[1][1]!= " "): return True
  if (ticTacToeBoard[0][2]==ticTacToeBoard[1][1] and ticTacToeBoard[0][2]==ticTacToeBoard[2][0]):
    if(ticTacToeBoard[1][1]!= " "): return True
  return False

def checkRows(ticTacToeBoard):
  if (ticTacToeBoard[0][0]==ticTacToeBoard[0][1] and ticTacToeBoard[0][1]==ticTacToeBoard[0][2]):
    if(ticTacToeBoard[0][1]=="X" or ticTacToeBoard[0][1]=="O"): return True
  if (ticTacToeBoard[1][0]==ticTacToeBoard[1][1] and ticTacToeBoard[1][1]==ticTacToeBoard[1][2]):
    if(ticTacToeBoard[1][1]=="X" or ticTacToeBoard[1][1]=="O"): return True
  if (ticTacToeBoard[2][0]==ticTacToeBoard[2][1] and ticTacToeBoard[2][1]==ticTacToeBoard[2][2]):
    if(ticTacToeBoard[2][1]=="X" or ticTacToeBoard[2][1]=="O"): return True
  return False

def checkCols(ticTacToeBoard):
  if (ticTacToeBoard[0][0]==ticTacToeBoard[1][0] and ticTacToeBoard[1][0]==ticTacToeBoard[2][0]):
    if(ticTacToeBoard[1][0]!= " "): return True
  if (ticTacToeBoard[0][1]==ticTacToeBoard[1][1] and ticTacToeBoard[1][1]==ticTacToeBoard[2][1]):
    if(ticTacToeBoard[1][1]!= " "): return True
  if (ticTacToeBoard[0][2]==ticTacToeBoard[1][2] and ticTacToeBoard[1][2]==ticTacToeBoard[2][2]):
    if(ticTacToeBoard[1][2]!= " "): return True
  return False

def checkFull(ticTacToeBoard):
  for i in range(3):
    if(" " in ticTacToeBoard[i]): return False
  return True

def playGame():
  print("You will be playing as Player X")

  notWon = True
  ticTacToeBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
  ticTacToeOpponent = {"Cell 1": "empty", "Cell 2":"empty", "Cell 3":"empty", "Cell 4":"empty", "Cell 5":"empty",                         "Cell 6": "empty", "Cell 7":"empty", "Cell 8":"empty", "Cell 9":"empty"}


  while(notWon == True):
    row = int(input("What row do you choose? "))
    col = int(input("What column do you choose? "))
    
    getOpponent(ticTacToeOpponent, ticTacToeBoard, row, col)
    printBoard(ticTacToeBoard)

    if(checkWin(ticTacToeBoard)==True): 
      print("Yay! You win!!!")
      notWon = False
      break
    elif(checkFull(ticTacToeBoard)==True):
      print("It's a tie!")
      notWon = False


    if(notWon == True):
      print("Now the computer is making a move...")
      if(getMe(ticTacToeOpponent,ticTacToeBoard)==1):
        printBoard(ticTacToeBoard)

        if(checkWin(ticTacToeBoard)==True): 
          print("Sorry, the computer won!!!")
          notWon = False
          break
        elif(checkFull(ticTacToeBoard)==True):
          print("It's a tie!")
          notWon = False
      else:
        print("The computer can't come up with a move! You win!!!")
        notWon = False
        break
    

playGame()
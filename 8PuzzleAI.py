#    Initial state  |   Goal state
#    1 2 3          |   1 2 3
#    5 - 6          |   4 5 6
#    7 8 4          |   7 8 -

n=3

def DrawBoard(board):
	for i in range(n):
		for j in range(n):
			print(board[i][j],end=" ")
		print("")
	print("-----")

def GetBlankPos(board):
	for i in range(n):
		for j in range(n):
			if board[i][j]==0:
				return i,j

def MoveUp(board):
	row,col=GetBlankPos(board)
	if(row-1>=0):
		board[row][col],board[row-1][col]=board[row-1][col],board[row][col]
	DrawBoard(board)
	
def MoveDown(board):
	row,col=GetBlankPos(board)
	if(row+1<=n):
		board[row][col],board[row+1][col]=board[row+1][col],board[row][col]
	DrawBoard(board)

def MoveLeft(board):
	row,col=GetBlankPos(board)
	if(col-1>=0):
		board[row][col],board[row][col-1]=board[row][col-1],board[row][col]
	DrawBoard(board)

def MoveRight(board):
	row,col=GetBlankPos(board)
	if(col<=n):
		board[row][col],board[row][col+1]=board[row][col+1],board[row][col]
	DrawBoard(board)


if __name__ == '__main__':
	board=[
		[1,2,3],
		[5,0,6],
		[7,8,4]
	]
	DrawBoard(board)
	MoveUp(board)
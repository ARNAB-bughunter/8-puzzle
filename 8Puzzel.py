from tkinter import *
import random
from tkinter import messagebox   

root=Tk()
w=350
h=350
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry('%dx%d+%d+%d'%(w,h,x,y))
root.resizable(False,False)
root.configure(bg="black")
root.title("8 PUZZLE")
label_list=[]
n=3
font=('Impact',70,'bold')
board=[
		[1,2,3],
		[4,5,0],
		[7,8,6]
]

def IsWin():
	temp=sum(board,[])
	x=[1, 2, 3, 4, 5, 6, 7, 8, 0]
	if(temp==x):
		messagebox.showinfo("","YOU WIN !!!") 

def data_shuffle():
	random.shuffle(board)
	for i in board:
		random.shuffle(i)

def GetBlankPos():
	for i in range(n):
		for j in range(n):
			if board[i][j]==0:
				return i,j

def draw_board():
	
	for i in range(n*n):
		label_list.append(Label(root,text=i))
	count=0
	for i in range(n):
		for j in range(n):
			label_list[count].grid(row=i,column=j,sticky="nswe",padx=2,pady=2)
			label_list[count]['text']=str(board[i][j])
			label_list[count]['font']=font
			if(board[i][j]==0):
				label_list[count]['bg']='black'
			else:
				label_list[count]['bg']='red'
			root.grid_columnconfigure(i,weight=1)
			root.grid_rowconfigure(j,weight=1)
			count+=1
	IsWin()

def MoveUp(e):
	row,col=GetBlankPos()
	if(row-1>=0):
		board[row][col],board[row-1][col]=board[row-1][col],board[row][col]
	draw_board()

def MoveDown(e):
	row,col=GetBlankPos()
	if(row+1<n):
		board[row][col],board[row+1][col]=board[row+1][col],board[row][col]
	draw_board()

def MoveLeft(e):
	row,col=GetBlankPos()
	if(col-1>=0):
		board[row][col],board[row][col-1]=board[row][col-1],board[row][col]
	draw_board()

def MoveRight(e):
	row,col=GetBlankPos()
	if(col+1<n):
		board[row][col],board[row][col+1]=board[row][col+1],board[row][col]
	draw_board()


if __name__ == '__main__':
	data_shuffle()
	draw_board()
	root.bind('<Left>',MoveRight);
	root.bind('<Right>',MoveLeft)
	root.bind('<Up>',MoveDown);
	root.bind('<Down>',MoveUp)
	root.mainloop()
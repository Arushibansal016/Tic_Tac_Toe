from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
ActivePlayer = 1
p1=[]
p2=[] 
state = 0
root=Tk()
root.title("TIC-TAC-TOE")



s = ttk.Style()
s.configure('my.TButton', font=('Times', 20))


bu1=ttk.Button(root,text ='',style='my.TButton')
bu1.grid(row=0,column=0,sticky='snew',ipadx=10,ipady=20)
bu1.config(command=lambda:ButtonClick(1, state))

bu2=ttk.Button(root,text ='',style='my.TButton')
bu2.grid(row=0,column=1,sticky='snew',ipadx=10,ipady=20)
bu2.config(command=lambda:ButtonClick(2, state))

bu3=ttk.Button(root,text ='',style='my.TButton')
bu3.grid(row=0,column=2,sticky='snew',ipadx=10,ipady=20)
bu3.config(command=lambda:ButtonClick(3, state))


bu4=ttk.Button(root,text ='',style='my.TButton')
bu4.grid(row=1,column=0,sticky='snew',ipadx=10,ipady=20)
bu4.config(command=lambda:ButtonClick(4, state))

bu5=ttk.Button(root,text ='',style='my.TButton')
bu5.grid(row=1,column=1,sticky='snew',ipadx=10,ipady=20)
bu5.config(command=lambda:ButtonClick(5, state))

bu6=ttk.Button(root,text ='',style='my.TButton')
bu6.grid(row=1,column=2,sticky='snew',ipadx=10,ipady=20)
bu6.config(command=lambda:ButtonClick(6, state))

bu7=ttk.Button(root,text ='',style='my.TButton')
bu7.grid(row=2,column=0,sticky='snew',ipadx=10,ipady=20)
bu7.config(command=lambda:ButtonClick(7, state))

bu8=ttk.Button(root,text ='',style='my.TButton')
bu8.grid(row=2,column=1,sticky='snew',ipadx=10,ipady=20)
bu8.config(command=lambda:ButtonClick(8, state))
 
bu9=ttk.Button(root,text ='',style='my.TButton')
bu9.grid(row=2,column=2,sticky='snew',ipadx=10,ipady=20)
bu9.config(command=lambda:ButtonClick(9, state))



def ButtonClick(id, st):
	global ActivePlayer
	global p1
	global p2

	
	if (ActivePlayer==1):
		SetLayout(id,"X")
		p1.append(id)
		root.title("TIC-TAC-TOE:Player 2")
		ActivePlayer=2
		print("p1:{}".format(p1))
	elif(ActivePlayer==2):
		SetLayout(id,"0")
		p2.append(id)
		root.title("TIC-TAC-TOE:Player 1")
		ActivePlayer=1
		print("p2:{}".format(p2))

	CheckWinner(st)


def SetLayout(id,PlayerSymbol):

	if id ==1:
		bu1.config(text=PlayerSymbol)
		bu1.state(['disabled'])
	elif id == 2:
		bu2.config(text=PlayerSymbol)
		bu2.state(['disabled'])
	elif id == 3:
		bu3.config(text=PlayerSymbol)
		bu3.state(['disabled'])
	elif id == 4:
		bu4.state(['disabled'])
		bu4.config(text=PlayerSymbol)
	elif id == 5:
		bu5.config(text=PlayerSymbol)
		bu5.state(['disabled'])
	elif id == 6:
		bu6.config(text=PlayerSymbol)
		bu6.state(['disabled'])
	elif id == 7:
		bu7.config(text=PlayerSymbol)
		bu7.state(['disabled'])
	elif id == 8:
		bu8.config(text=PlayerSymbol)
		bu8.state(['disabled'])
	elif id == 9:
		bu9.config(text=PlayerSymbol)
		bu9.state(['disabled'])

def EnableButton(id,PlayerSymbol):
	if id ==1:
		bu1.config(text=PlayerSymbol)
		bu1['state'] = 'normal'
	elif id == 2:
		bu2.config(text=PlayerSymbol)
		bu2['state'] = 'normal'
	elif id == 3:
		bu3.config(text=PlayerSymbol)
		bu3['state'] = 'normal'
	elif id == 4:
		bu4['state'] = 'normal'
		bu4.config(text=PlayerSymbol)
	elif id == 5:
		bu5.config(text=PlayerSymbol)
		bu5['state'] = 'normal'
	elif id == 6:
		bu6.config(text=PlayerSymbol)
		bu6['state'] = 'normal'
	elif id == 7:
		bu7.config(text=PlayerSymbol)
		bu7['state'] = 'normal'
	elif id == 8:
		bu8.config(text=PlayerSymbol)
		bu8['state'] = 'normal'
	elif id == 9:
		bu9.config(text=PlayerSymbol)
		bu9['state'] = 'normal'

def resetGame():

	ActivePlayer = 1
	state = 0
	p1.clear()
	p2.clear()

	for btn in [1,2,3,4,5,6,7,8,9]:
		
		EnableButton(btn,"")
	print(state)
	print(p1)
	print(p2)
	print(ActivePlayer)

def CheckWinner(s):

	global state

	s += 1
	state = s

	print("State : " + str(state))
	Winner=-1#dont have any winner yet

	if(( 1 in p1) and (2 in p1) and (3 in p1)):
		print("1")
		Winner=1
	if(( 1 in p2) and (2 in p2) and (3 in p2)):
		print("2")
		Winner=2

	if(( 4 in p1) and (5 in p1) and (6 in p1)):
		print("3")
		Winner=1
	if(( 4 in p2) and (5 in p2) and (6 in p2)):
		print("4")
		Winner=2
	
	if(( 7 in p1) and (8 in p1) and (9 in p1)):
		print("5")
		Winner=1
	if(( 7 in p2) and (8 in p2) and (9 in p2)):
		print("6")
		Winner=2

	if(( 1 in p1) and (4 in p1) and (7 in p1)):
		print("7")
		Winner=1
	if(( 1 in p2) and (4 in p2) and (7 in p2)):
		print("8")
		Winner=2

	if(( 2 in p1) and (5 in p1) and (8 in p1)):
		print("9")
		Winner=1
	if(( 2 in p2) and (5 in p2) and (8 in p2)):
		print("10")
		Winner=2

	if(( 3 in p1) and (6 in p1) and (9 in p1)):
		print("11")
		Winner=1
	if(( 3 in p2) and (6 in p2) and (9 in p2)):
		print("12")
		Winner=2

	if(( 1 in p1) and (5 in p1) and (9 in p1)):
		print("13")
		Winner=1
	if(( 1 in p2) and (5 in p2) and (9 in p2)):
		print("14")
		Winner=2

	if(( 3 in p1) and (5 in p1) and (7 in p1)):
		print("15")
		Winner=1
	if(( 3 in p2) and (5 in p2) and (7 in p2)):
		print("16")
		Winner=2

	if Winner==1:
		messagebox.showinfo("Congo","Player 1 is the Winner")
		state = 0
		resetGame()
	elif Winner==2: 
		messagebox.showinfo("Congo","Player 2 is the Winner")
		state = 0
		resetGame()

	elif (Winner==-1) and (state == 9):
		messagebox.showinfo("Congo","Its a Tie!")
		state = 0
		resetGame()

root.mainloop()


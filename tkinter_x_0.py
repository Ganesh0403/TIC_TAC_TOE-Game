import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = tk.Tk()
# win.geometry("1350x750+0+0")
win.resizable(0,0)
win.title("X_O_Game")
win.configure(bg = "cadet blue")

top = tk.Frame(win, width = 1350, pady = 2, height = 100, relief = "ridge", bg = "cadet blue")
top.grid(row = 0, column = 0)

mainframe = tk.Frame(win, width = 1350, pady = 2, height = 650, relief = "ridge", bg = "powder blue")
mainframe.grid(row = 1, column = 0)

# bottom = tk.Frame(win, width = 1350, pady = 2, height = 50, relief = "ridge", bg = "cadet blue")
# bottom.grid(row = 2, column = 0)

label = tk.Label(top, font = ('arial',50,'bold'), text = 'TIC TAC TOE', bg = 'cadet blue', bd = 20, justify = 'center', fg = 'Green')
label.grid(row = 0, column = 0)

leftframe = tk.Frame(mainframe, width = 1350/2, pady = 2, padx = 10, height = 500, relief = "ridge", bg = "cadet blue", bd = 10)
leftframe.grid(row = 0, column = 0)

rightframe = tk.Frame(mainframe, width = 1350/2, pady = 2, padx = 10, height = 500, relief = "ridge", bg = "cadet blue", bd = 10)
rightframe.grid(row = 0, column = 1)

rightframe1 = tk.Frame(rightframe, width = 560, pady = 2, padx = 10, height = 200, relief = "ridge", bg = "cadet blue", bd = 10)
rightframe1.grid(row = 0, column = 0)

rightframe2 = tk.Frame(rightframe, width = 560, pady = 2, padx = 10, height = 200, relief = "ridge", bg = "cadet blue", bd = 10)
rightframe2.grid(row = 1, column = 0)

player1 = tk.IntVar()
player2 = tk.IntVar()
player1.set(0)
player2.set(0)

buttons = tk.StringVar()
click = True
count = 0

def checker(buttons):
    global click
    global count
    if buttons['text'] == '' and click == True:
        buttons['text'] = 'X'
        click = False
        count = count + 1
        score()
    if buttons['text'] == '' and click == False:
        buttons['text'] = 'O'
        click = True
        count = count + 1
        score()

def score():
    if button1['text']=='X' and button2['text']=='X' and button3['text']=='X':
        button1.configure(bg = 'light blue')
        button2.configure(bg = 'light blue')
        button3.configure(bg = 'light blue')
        a = float(player1.get())
        a = a + 2
        player1.set(a)
        messagebox.showinfo("Winner Player1", "You won the Game")
    elif button4['text']=='X' and button5['text']=='X' and button6['text']=='X':
        button4.configure(bg = 'light blue')
        button5.configure(bg = 'light blue')
        button6.configure(bg = 'light blue')
        a = float(player1.get())
        a = a + 2
        player1.set(a)
        messagebox.showinfo("Winner Player1", "You won the Game")
    elif button7['text']=='X' and button9['text']=='X' and button8['text']=='X':
        button7.configure(bg = 'light blue')
        button8.configure(bg = 'light blue')
        button9.configure(bg = 'light blue')
        a = float(player1.get())
        a = a + 2
        player1.set(a)
        messagebox.showinfo("Winner Player1", "You won the Game")
    elif button1['text']=='X' and button4['text']=='X' and button7['text']=='X':
        button1.configure(bg = 'light blue')
        button4.configure(bg = 'light blue')
        button7.configure(bg = 'light blue')
        a = float(player1.get())
        a = a + 2
        player1.set(a)
        messagebox.showinfo("Winner Player1", "You won the Game")
    elif button2['text']=='X' and button5['text']=='X' and button8['text']=='X':
        button8.configure(bg = 'light blue')
        button2.configure(bg = 'light blue')
        button5.configure(bg = 'light blue')
        a = float(player1.get())
        a = a + 2
        player1.set(a)
        messagebox.showinfo("Winner Player1", "You won the Game")
    elif button1['text']=='X' and button5['text']=='X' and button9['text']=='X':
        button1.configure(bg = 'light blue')
        button5.configure(bg = 'light blue')
        button9.configure(bg = 'light blue')
        a = float(player1.get())
        a = a + 2
        player1.set(a)
        messagebox.showinfo("Winner Player1", "You won the Game")
    elif button3['text']=='X' and button6['text']=='X' and button9['text']=='X':
        button9.configure(bg = 'light blue')
        button6.configure(bg = 'light blue')
        button3.configure(bg = 'light blue')
        a = float(player1.get())
        a = a + 2
        player1.set(a)
        messagebox.showinfo("Winner Player1", "You won the Game")
    elif button3['text']=='X' and button5['text']=='X' and button7['text']=='X':
        button5.configure(bg = 'light blue')
        button7.configure(bg = 'light blue')
        button3.configure(bg = 'light blue')
        a = float(player1.get())
        a = a + 2
        player1.set(a)
        messagebox.showinfo("Winner Player1", "You won the Game")

    elif button1['text']=='O' and button2['text']=='O' and button3['text']=='O':
        button1.configure(bg = 'light blue')
        button2.configure(bg = 'light blue')
        button3.configure(bg = 'light blue')
        a = float(player2.get())
        a = a + 2
        player2.set(a)
        messagebox.showinfo("Winner Player2", "You won the Game")
    elif button4['text']=='O' and button5['text']=='O' and button6['text']=='O':
        button4.configure(bg = 'light blue')
        button5.configure(bg = 'light blue')
        button6.configure(bg = 'light blue')
        a = float(player2.get())
        a = a + 2
        player2.set(a)
        messagebox.showinfo("Winner Player2", "You won the Game")
    elif button7['text']=='O' and button9['text']=='O' and button8['text']=='O':
        button7.configure(bg = 'light blue')
        button8.configure(bg = 'light blue')
        button9.configure(bg = 'light blue')
        a = float(player2.get())
        a = a + 2
        player2.set(a)
        messagebox.showinfo("Winner Player2", "You won the Game")
    elif button1['text']=='O' and button4['text']=='O' and button7['text']=='O':
        button1.configure(bg = 'light blue')
        button4.configure(bg = 'light blue')
        button7.configure(bg = 'light blue')
        a = float(player2.get())
        a = a + 2
        player2.set(a)
        messagebox.showinfo("Winner Player2", "You won the Game")
    elif button2['text']=='O' and button5['text']=='O' and button8['text']=='O':
        button8.configure(bg = 'light blue')
        button2.configure(bg = 'light blue')
        button5.configure(bg = 'light blue')
        a = float(player2.get())
        a = a + 2
        player2.set(a)
        messagebox.showinfo("Winner Player2", "You won the Game")
    elif button1['text']=='O' and button5['text']=='O' and button9['text']=='O':
        button1.configure(bg = 'light blue')
        button5.configure(bg = 'light blue')
        button9.configure(bg = 'light blue')
        a = float(player2.get())
        a = a + 2
        player2.set(a)
        messagebox.showinfo("Winner Player2", "You won the Game")
    elif button3['text']=='O' and button6['text']=='O' and button9['text']=='O':
        button9.configure(bg = 'light blue')
        button6.configure(bg = 'light blue')
        button3.configure(bg = 'light blue')
        a = float(player2.get())
        a = a + 2
        player2.set(a)
        messagebox.showinfo("Winner Player2", "You won the Game")
    elif button3['text']=='O' and button5['text']=='O' and button7['text']=='O':
        button5.configure(bg = 'light blue')
        button7.configure(bg = 'light blue')
        button3.configure(bg = 'light blue')
        a = float(player2.get())
        a = a + 2
        player2.set(a)
        messagebox.showinfo("Winner Player2", "You won the Game")
    
    elif count==9: 
        a = float(player1.get())
        b = float(player2.get())
        a = a + 1
        b = b + 1
        player1.set(a)
        player2.set(b)
        messagebox.showinfo("Match Tied", "Play One more Game")

def reset():
    global count
    button1['text']=''
    button2['text']=''
    button3['text']=''
    button4['text']=''
    button5['text']='' 
    button6['text']=''
    button7['text']=''
    button8['text']=''
    button9['text']=''

    button1.configure(bg = 'light grey')
    button2.configure(bg = 'light grey')
    button3.configure(bg = 'light grey')
    button4.configure(bg = 'light grey')
    button5.configure(bg = 'light grey')
    button6.configure(bg = 'light grey')
    button7.configure(bg = 'light grey')
    button8.configure(bg = 'light grey')
    button9.configure(bg = 'light grey')
    count = 0

def new():
    reset()
    player1.set(0)
    player2.set(0)

p1label = tk.Label(rightframe1, font = ('verdana',20,'bold'), text ="Player1 : ", bg = 'cadet blue', bd = 8, justify = 'left',fg = 'black')
p1label.grid(row = 0, column = 0)

p2label = tk.Label(rightframe1, font = ('verdana',20,'bold'), text ="Player2 : ", bg = 'cadet blue', bd = 8, justify = 'left',fg = 'black')
p2label.grid(row = 1, column = 0)

p1 = tk.Entry(rightframe1, bg = 'white', width = 14, bd = 2, justify = 'left',fg = 'black', textvariable = player1, font = 16)
p1.grid(row = 0, column = 1)

p2 = tk.Entry(rightframe1, bg = 'white', width = 14, bd = 2, justify = 'left',fg = 'black', textvariable = player2, font = 16)
p2.grid(row = 1, column = 1)

button1 = tk.Button(leftframe, text = '', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 3, width = 8, command = lambda:checker(button1))
button1.grid(row = 1, column = 0, sticky = tk.S+tk.W+tk.N+tk.E)

button2 = tk.Button(leftframe, text = '', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 3, width = 8, command = lambda:checker(button2))
button2.grid(row = 1, column = 1, sticky = tk.S+tk.W+tk.N+tk.E)

button3 = tk.Button(leftframe, text = '', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 3, width = 8, command = lambda:checker(button3))
button3.grid(row = 1, column = 2, sticky = tk.S+tk.W+tk.N+tk.E)

button4 = tk.Button(leftframe, text = '', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 3, width = 8, command = lambda:checker(button4))
button4.grid(row = 2, column = 0, sticky = tk.S+tk.W+tk.N+tk.E)

button5 = tk.Button(leftframe, text = '', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 3, width = 8, command = lambda:checker(button5))
button5.grid(row = 2, column = 1, sticky = tk.S+tk.W+tk.N+tk.E)

button6 = tk.Button(leftframe, text = '', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 3, width = 8, command = lambda:checker(button6))
button6.grid(row = 2, column = 2, sticky = tk.S+tk.W+tk.N+tk.E)

button7 = tk.Button(leftframe, text = '', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 3, width = 8, command = lambda:checker(button7))
button7.grid(row = 3, column = 0, sticky = tk.S+tk.W+tk.N+tk.E)

button8 = tk.Button(leftframe, text = '', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 3, width = 8, command = lambda:checker(button8))
button8.grid(row = 3, column = 1, sticky = tk.S+tk.W+tk.N+tk.E)

button9 = tk.Button(leftframe, text = '', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 3, width = 8, command = lambda:checker(button9))
button9.grid(row = 3, column = 2, sticky = tk.S+tk.W+tk.N+tk.E)

resetbutton = tk.Button(rightframe2, text = 'Reset', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 1, width = 20, command = reset)
resetbutton.grid(row = 0, column = 0, padx = 6, pady = 10)

newbutton = tk.Button(rightframe2, text = 'New Game', bg = 'light grey', fg= 'black', font = ('times',26,'bold'), height = 1, width = 20, command = new)
newbutton.grid(row = 1, column = 0, padx = 6, pady = 11)


win.mainloop()
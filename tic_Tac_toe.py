import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        root.title("Tic Tac Toe")
        root.geometry("660x370")
        root.resizable(False, False)
        self.current_player = 'X'
        self.clicked = 0
        self.name_of_player1=self.name_of_player2=""
        
# creating top left frame for player 1
        self.top_frame_left=tk.Frame(root,bg='black',border=4,height=2,width=40,relief='groove')
        tk.Label(self.top_frame_left,text="Player1:",font=('Arial', 20),bg='white',fg='black',border=2,relief='solid').grid(row=1,column=0)
        tk.Label(self.top_frame_left,text="Score: ",font=('Arial', 20),bg='white',fg='black',border=2,relief='solid').grid(row=1,column=1)

        self.top_frame_left.grid(row=0,column=0,sticky='nsew')

# creating middle frame to fill the gap 
        self.top_frame_middle=tk.Frame(root,bg='black',border=4,height=2,width=40,relief='groove')
        tk.Label(self.top_frame_middle,text="|   TIC TAC TOE   |",font=('Arial', 20),bg='black',fg='Skyblue').pack()
        self.top_frame_middle.grid(row=0,column=1,sticky='nsew')

# creating top right frame for player2
        self.top_frame_right=tk.Frame(root,bg='black',border=4,height=2,width=22,relief='groove')
        tk.Label(self.top_frame_right,text="Player2:",font=('Arial', 20),bg='white',fg='black',border=2,relief='solid').grid(row=1,column=0)
        tk.Label(self.top_frame_right,text="Score: ",font=('Arial', 20),bg='white',fg='black',border=2,relief='solid').grid(row=1,column=1)
        self.top_frame_right.grid(row=0,column=2,sticky='nsew',ipadx=2)
# Creating board and button 
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text='', font=('Arial', 20),width=1,height=1 ,command=lambda i=i, j=j: self.handle_click(i, j), border=8, relief="sunken",bg='black',fg='green')
                button.grid(row=i+1, column=j, sticky='nsew',ipadx=2,ipady=2)
                self.buttons[i][j] = button
# Start button 
        start_button = tk.Button(root, text='Start', font=('Arial', 20), command=self.start,border=5,relief='raised',bg='black',fg='green')
        start_button.grid(row=4, column=0,  sticky='nsew',ipadx=2,ipady=2)
# Restart Button 
        restart_button = tk.Button(root, text='Restart', font=('Arial', 20), command=self.restart,border=5,relief='raised',bg='black',fg='white')
        restart_button.grid(row=4, column=1,  sticky='nsew',ipadx=2,ipady=2)
# finish Button 
        finish_button = tk.Button(root, text='Finish', font=('Arial', 20), command=self.finish,border=5,relief='raised',bg='black',fg='red')
        finish_button.grid(row=4, column=2,  sticky='nsew',ipadx=2,ipady=2)

#  starting game 
    def start(self):
        global s1,s2
        self.score_of_player1=self.score_of_player2=0
        if self.clicked == 0 or self.name_of_player1=="" or self.name_of_player2=="":
            self.clicked+=1
    # declaring name of first player 
            self.name_of_player1 = simpledialog.askstring(title="Name", prompt="Enter the name of first player:")
            tk.Label(self.top_frame_left,text=self.name_of_player1.title(),font=('Arial', 20),bg='black',fg='grey').grid(row=2,column=0)
            s1 = tk.Label(self.top_frame_left,text=self.score_of_player1,font=('Arial', 20),bg='black',fg='grey')
            s1.grid(row=2,column=1)
    # declaring name of second player 
            self.name_of_player2 = simpledialog.askstring(title="Name", prompt="Enter the name of Second player:")
            tk.Label(self.top_frame_right,text=self.name_of_player2.title(),font=('Arial', 20),bg='black',fg='orange').grid(row=2,column=0)
            s2 = tk.Label(self.top_frame_right,text=self.score_of_player2,font=('Arial', 20),bg='black',fg='orange')
            s2.grid(row=2,column=1)
        else:
            messagebox.showinfo("Game Start","Game has already started!")


# works when users starts playing game     
    def handle_click(self, row, col):
        
        
        if self.name_of_player1 != "" and self.name_of_player2 !="": 
            if self.board[row][col] == '':
                self.board[row][col] = self.current_player
                self.buttons[row][col].config(text=self.current_player)
                if self.check_win():

                    if self.current_player == "X":
                        self.current_player = self.name_of_player1
                        self.score_of_player1 += 1
                        s1.config(text = self.score_of_player1)
                        print(self.score_of_player1 ) 
                    else:
                        self.current_player = self.name_of_player2 
                        self.score_of_player2 +=1               
                        s2.config(text=self.score_of_player2)       
                    messagebox.showinfo('Game Over', f'{self.current_player} wins!')
                    self.restart()
                elif self.check_tie():
                    messagebox.showinfo('Game Over', 'It\'s a tie!')
                    self.restart()
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            messagebox.showinfo("Sorry!", "Start the game first")
# Checking condition for winning the game 
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False
# Checking condition for tie 
    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    return False
        return True
# To restart the game 
    def restart(self):
        ques = messagebox.askquestion("RESTART"," Want to restart ?")
        if ques.lower() == "yes":
            self.current_player = 'X'
            self.board = [['' for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(text='')
            
        else:
            quit()
# Finish button 
    def finish(self):
        choice = messagebox.askyesno("Finish Game", "Do you want to quit?")
        if choice:
            self.root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

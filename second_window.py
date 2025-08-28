from tkinter import *
from tkinter import ttk

class SecondWindow(Frame):
    def __init__(self, root):
        super().__init__(root)
        
        
    def second_window(self):
        self.window = Tk()
        self.window.title('База даних')
        self.window.geometry('1000x500')
    
    
    def tree_view(self):
        self.tree = ttk.Treeview(show='tree')
        self.tree.pack(padx=10, pady=10)
        
        

root = Tk()
s_win = SecondWindow(root)

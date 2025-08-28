from tkinter import *
from tkinter import ttk

class SecondWindow(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title('База даних')
        self.root.geometry('1000x500')
        
    
    def tree_view(self):
        self.tree = ttk.Treeview(show='tree')
        self.tree.pack(padx=10, pady=10)
        self.columns = ('name', 'surname', 'group_work', 'date_created')
        
        
    def sort(self, col, reverse):
        self.l = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]
        self.l.sort(reverse=reverse)
        
        for idx, (_, k) in enumerate(self.l):
            self.tree.move(k, '', idx)
        
        self.tree.heading(col, command=lambda: self.sort(col, not reverse))
        
        
    def add_data(self):
        self.tree.heading('name', text='Ім`я', anchor=W, command=lambda: self.sort(0, False))
        self.tree.heading('name', text='Прізвище', anchor=W, command=lambda: self.sort(1, False))
        self.tree.heading('name', text='Група', anchor=W, command=lambda: self.sort(2, False))
        self.tree.heading('name', text='Дата створення', anchor=W, command=lambda: self.sort(3, False))
        

if __name__ == '__main__':
    root = Tk()
    s_win = SecondWindow(root)     
    
    root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

from db import user
from second_window import s_win


class MainWindow(Frame):
    def __init__(self, root):
        super().__init__(root)
        
        self.notebook = ttk.Notebook()
        
        self.Register = Register(self.notebook)
        self.Login = Login(self.notebook)
        
        self.notebook.add(self.Register, text='Реєстрація')
        self.notebook.add(self.Login, text='Вхід')
        self.notebook.pack(padx=10, pady=10)


class Register(Frame):
    def __init__(self, root):
        super().__init__(root)  
        
        self.greet = Label(self, text='Реєстрація', font=('Arial', 14))
        self.greeting = Label(self, text='Введіть, будь ласка, бажаний логін та пароль', font=('Arial', 14))
        
        self.greet.pack()
        self.greeting.pack()
        
        self.login = Label(self, text='Логін', font=('Arial', 14))
        self.password = Label(self, text='Пароль', font=('Arial', 14))
        
        self.login.pack(padx=10, pady=10)
        self.login_entry = Entry(self, width=50, font=('Arial', 14))
        self.login_entry.pack()
        
        self.password.pack(padx=10, pady=10)
        
        self.passwd_entry = Entry(self, width=50, font=('Arial', 14))
        self.passwd_entry.pack(padx=10, pady=10)
        
        self.button_reg = Button(self, width=10, font=('Arial', 12), text='Реєстрація', command=self.write_to_db)
        self.button_reg.pack(padx=10, pady=10)
        
        
    def write_to_db(self):
        if self.login_entry.get() and self.passwd_entry.get():
            user.insert_user(self.login_entry.get(), self.passwd_entry.get())
            showinfo(title='Інформація', message='Реєстрація успішна!')
        else:
            showerror(title='Помилка', message='Помилка при реєстрації.')
           
            
class Login(Frame):
    def __init__(self, root):
        super().__init__(root)

        self.greet = Label(self, text='Вітаю у системі!', font=('Arial', 14))
        self.greeting = Label(self, text='Введіть, будь ласка, логін та пароль', font=('Arial', 14))
        
        self.greet.pack()
        self.greeting.pack()
        
        self.login = Label(self, text='Логін', font=('Arial', 14))
        self.password = Label(self, text='Пароль', font=('Arial', 14))
        
        
        self.login.pack(padx=10, pady=10)
        
        self.login_log_entry = Entry(self, width=50, font=('Arial', 14))
        self.login_log_entry.pack()
        
        self.password.pack(padx=10, pady=10)
        
        self.passwd_log_entry = Entry(self, width=50, font=('Arial', 14))
        self.passwd_log_entry.pack(padx=10, pady=10)
        
        self.button_log = Button(self, width=10, font=('Arial', 12), text='Увійти', command=s_win.second_window)
        self.button_log.pack(padx=10, pady=10)
    

class User(Frame):
    def __init__(self, root):
        super().__init__(root)
        

    def get_user(self):
        self.login_entry.get() and self.passwd_entry.get()       


if __name__ == '__main__':
    root = Tk()
    
    window = MainWindow(root)
    
    root.title('База даних')
    root.geometry('1000x500')
    root.mainloop()
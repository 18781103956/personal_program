import tkinter
import pymysql
from tkinter import ttk

#==================================数据库====================================
class Phone_data():
    def __init__(self):
        self.mydb = pymysql.connect("127.0.0.1", "root", "root", "phone_number")
        self.mycursor = self.mydb.cursor()

    def look_infor(self):
        sql = "select * from linkman"
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        return result

class run_win():
    def __init__(self):
        self.win = tkinter.Tk()

    def win_label(self):
        lb = tkinter.Label(self.win)
        lb.place(x=0, y=0, height=400, width=400)
        pass

    def show_win(self):
        pass
        self.win.title("电话簿")
        self.win.maxsize(600, 250)
        self.win.minsize(600, 250)
        self.show_tel()
        self.win.mainloop()

    def show_tel(self):
        cols = ('序号', '姓名', '电话号码')
        listBox = ttk.Treeview(self.win, columns=cols, show='headings')
        for col in cols:
            listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        closeButton = tkinter.Button(self.win, text="Close", bg='gray', width=15, command=exit).grid(row=4, column=1)

        tempList = []
        sql = Phone_data()
        result = sql.look_infor()
        for item in range(len(result)):
            tempList.append(result[item])

        for i, (name, score) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(i, name, score))




if __name__ == '__main__':
    w = run_win()
    w.show_win()
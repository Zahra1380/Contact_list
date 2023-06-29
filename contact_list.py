from audioop import add
import os
from tkinter import *
from sqlite3 import *

def r_file():
    file = open("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contry number code.txt", "r")
    l = file.readlines()
    file.close()
    return l

class Graphic(object):
    def __init__(self, w: Tk):

        '''make graphic items'''
        self.w = w
        self.w.geometry("505x260")
        self.w.resizable(False, False)
        self.w.title("contact book")
        self.v1 = StringVar()
        self.l1 = Label(self.w, font= "tahoma 14 normal", text= "name")
        self.l1.place(x = 10, y = 10)
        self.e1 = Entry(self.w, textvariable = self.v1, font= "tahoma 14 normal", width = 24)
        self.e1.place(x = 150, y = 11)

        self.v3 = StringVar()
        self.l3 = Label(self.w, font= "tahoma 14 normal", text= "Contry Code")
        self.l3.place(x = 10, y = 60)
        self.e3 = Entry(self.w, textvariable = self.v3, font= "tahoma 14 normal", width = 24)
        self.e3.place(x = 150, y = 61)

        self.v4 = IntVar()
        self.l4 = Label(self.w, font= "tahoma 14 normal", text= "Phone number")
        self.l4.place(x = 10, y = 110)
        self.e4 = Entry(self.w, textvariable = self.v4, font= "tahoma 14 normal", width = 24)
        self.e4.place(x = 150, y = 111)

        self.v5 = StringVar()
        self.l5 = Label(self.w, font= "tahoma 14 normal", text= "Email Addres")
        self.l5.place(x = 10, y = 160)
        self.e5 = Entry(self.w, textvariable = self.v5, font= "tahoma 14 normal", width = 24)
        self.e5.place(x = 150, y = 161)

        # add delete search edit show_all
        self.b1 = Button(self.w, text = "add", font = "tahoma 14 normal", bg= "green", fg= "white", width= 8, command= self.add_)
        self.b1.place(x = 405, y= 10)

        self.b3 = Button(self.w, text = "delete", font = "tahoma 14 normal", bg= "green", fg= "white", width= 8, command= self.delete_)
        self.b3.place(x = 405, y= 60)

        self.b4 = Button(self.w, text = "search", font = "tahoma 14 normal", bg= "green", fg= "white", width= 8, command= self.seach)
        self.b4.place(x = 405, y= 110)

        self.b5 = Button(self.w, text = "show all", font = "tahoma 14 normal", bg= "green", fg= "white", width= 8, command= self.show)
        self.b5.place(x = 405, y= 160)

        self.b2 = Button(self.w, text = "edit by name", font = "tahoma 14 normal", bg= "green", fg= "white", command= self.edit_name)
        self.b2.place(x = 10, y= 210)

        self.b6 = Button(self.w, text = "edit by phone", font = "tahoma 14 normal", bg= "green", fg= "white", command= self.edit_phone)
        self.b6.place(x = 140, y= 210)

        self.b6 = Button(self.w, text = "edit by email", font = "tahoma 14 normal", bg= "green", fg= "white", command= self.edit_email)
        self.b6.place(x = 275, y= 210)

        self.b7 = Button(self.w, text = "clear", font = "tahoma 14 normal", bg= "green", fg= "white", width= 8, command= self.clear_db)
        self.b7.place(x = 405, y= 210)
    def clear(self):
        self.v1.set("")
        self.v3.set("")
        self.v4.set(0)
        self.v5.set("")

    def db_creat(self):
        'this part make database if doesnt exsist'
        try:
            con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
            c = con.cursor()
            c.execute("create table contacs (name text primary key, contry_code text, cell_number int,\
                 email text, contry text, contry_abrivision text)")
            con.commit()
            con.close()
        except:
            pass

    def add_(self):
        '''add item to db if this file is created we check this entry name this name is in db or not if be break func or not
        we check this entry is not empity and entry code exists in txt file if not in file break for and left func else we add to db'''
        self.db_creat()
        lst = r_file()
        nam = self.v1.get()
        code = self.v3.get()
        cel_num = self.v4.get()
        emaill = self.v5.get()

        if os.path.exists("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db") == True:
            con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
            c = con.cursor()
            c.execute("select name from contacs")
            q = c.fetchall()
            l = [i[0] for i in q]

            if nam in l:
                self.tablee('')
                con.commit()
                con.close() 
                self.clear()
                return

        for  i in lst:
            if i.split()[1] != code:
                pass
            else:
                if nam is None or code is None or cel_num is None or emaill is None:
                    break
                else:
                    try:
                        print(i.split()[0])
                        contry = i.split()[0]
                        co_abrivation = i.split()[2]
                        con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
                        c = con.cursor()
                        c.execute("insert into contacs values ('{}', '{}', {}, '{}', '{}', '{}')"\
                            .format(nam, code, cel_num, emaill, contry, co_abrivation))
                        con.commit()
                        con.close()
                        break
                    except:
                        pass
        self.clear()

    def show(self):
        '''get all element in db'''
        con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
        c = con.cursor()
        c.execute("select * from contacs")
        q = c.fetchall()
        self.tablee(q)
        con.commit()
        con.close()

    def tablee(self, lst):
        """shows that item in the table shape and show extra page about error"""
        win = Tk()
        if type(lst) == str:
            win.title("Error")
            Label(win, text= "one element with this name is exsist you cant add the an other one", font= "tahoma 14 normal").pack()
            Button(win, text= "Ok", font= "tahoma 14 normal", command= win.destroy, bg= "green", fg= "white").pack()

        elif type(lst) == tuple:
            win.title("Error")
            Label(win, text= "this item doesnt in database", font= "tahoma 14 normal").pack()
            Button(win, text= "Ok", font= "tahoma 14 normal", command= win.destroy, bg= "green", fg= "white").pack()   

        elif lst == []:
            win.title("Error")
            win.title("all elements")
            Label(win, text= "we can not find this element or the database was cleared", font= "tahoma 14 normal").pack()
            Button(win, text= "Ok", font= "tahoma 14 normal", command= win.destroy, bg= "green", fg= "white").pack()

        else:
            win.title("all elements")
            for i in range(len(lst)):
                for j in range(len(lst[0])):
                    e = Entry(win, width= 10,font= "tahom 12 normal")
                    e.grid(row=i, column=j)
                    e.insert(END, lst[i][j])

    def seach(self):
        '''search between all element'''
        nam = self.v1.get()
        code = self.v3.get()
        cel_num = self.v4.get()
        emaill = self.v5.get()
        print(cel_num)
        con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
        c = con.cursor()
        if nam != "":
            c.execute("select * from contacs where name = '{}'".format(nam))
            q = c.fetchall()
            self.tablee(q)
        elif code != "":
            c.execute("select * from contacs where contry_code = '{}'".format(code))
            q = c.fetchall()
            self.tablee(q)
        elif cel_num != 0:
            c.execute("select * from contacs where cell_number = {}".format(cel_num))
            q = c.fetchall()
            self.tablee(q)
        elif emaill != "":
            c.execute("select * from contacs where email = '{}'".format(emaill))
            q = c.fetchall()
            self.tablee(q)
        elif nam != "" and code != "":
            c.execute("select * from contacs where name = '{}', contry_code = '{}'".format(nam, code))
            q = c.fetchall()
            self.tablee(q)
        elif nam != "" and cel_num != 0:
            c.execute("select * from contacs where name = '{}', cell_number = {}".format(nam, cel_num))
            q = c.fetchall()
            self.tablee(q)
        elif nam != "" and emaill != "":
            c.execute("select * from contacs where name = '{}', email = '{}'".format(nam, emaill))
            q = c.fetchall()
            self.tablee(q)
        elif code != "" and cel_num != 0:
            c.execute("select * from contacs where contry_code = '{}', cell_number = {}".format(code, cel_num))
            q = c.fetchall()
            self.tablee(q)
        elif code != "" and emaill != "":
            c.execute("select * from contacs where contry_code = '{}', email = '{}'".format(code, emaill))
            q = c.fetchall()
            self.tablee(q)
        elif emaill != "" and cel_num != 0:
            c.execute("select * from contacs where email = '{}', cell_number = {}".format(emaill, cel_num))
            q = c.fetchall()
            self.tablee(q)
        elif emaill != "" and cel_num != '' and nam != "":
            c.execute("select * from contacs where name = '{}', email = '{}', cell_number = {}".format(nam, emaill, cel_num))
            q = c.fetchall()
            self.tablee(q)
        elif emaill != "" and code != '' and nam != "":
            c.execute("select * from contacs where name = '{}', email = '{}', contry_code = '{}'".format(nam, emaill, code))
            q = c.fetchall()
            self.tablee(q)
        elif cel_num != 0  and code != '' and nam != "":
            c.execute("select * from contacs where name = '{}', cell_number = {}, contry_code = '{}'".format(nam, code, code))
            q = c.fetchall()
            self.tablee(q)
        elif cel_num != 0  and code != '' and emaill != "":
            c.execute("select * from contacs where email = '{}', cell_number = {}, contry_code = '{}'".format(emaill, code, code))
            q = c.fetchall()
            self.tablee(q)
        else:
            c.execute("select * from contacs where name = '{}', email = '{}', cell_number = {}, contry_code = '{}'".format(nam, emaill, code, code))
            q = c.fetchall()
            self.tablee(q)
        con.commit()
        con.close()
        self.clear()

    def delete_(self):
        '''delete kerden yek item ba estefade he kodam az item haye mojud'''
        nam = self.v1.get()
        code = self.v3.get()
        cel_num = self.v4.get()
        emaill = self.v5.get()
        print(cel_num)
        con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
        c = con.cursor()
        if nam != "":
            c.execute("delete from contacs where name = '{}'".format(nam))
        elif code != "":
            c.execute("delete from contacs where contry_code = '{}'".format(code))
        elif cel_num != 0:
            c.execute("delete from contacs where cell_number = {}".format(cel_num))
        elif emaill != "":
            c.execute("delete from contacs where email = '{}'".format(emaill))
        elif nam != "" and code != "":
            c.execute("delete from contacs where name = '{}', contry_code = '{}'".format(nam, code))
        elif nam != "" and cel_num != 0:
            c.execute("delete from contacs where name = '{}', cell_number = {}".format(nam, cel_num))
        elif nam != "" and emaill != "":
            c.execute("delete from contacs where name = '{}', email = '{}'".format(nam, emaill))
        elif code != "" and cel_num != 0:
            c.execute("delete from contacs where contry_code = '{}', cell_number = {}".format(code, cel_num))
        elif code != "" and emaill != "":
            c.execute("delete from contacs where contry_code = '{}', email = '{}'".format(code, emaill))
        elif emaill != "" and cel_num != 0:
            c.execute("delete from contacs where email = '{}', cell_number = {}".format(emaill, cel_num))
        elif emaill != "" and cel_num != '' and nam != "":
            c.execute("delete from contacs where name = '{}', email = '{}', cell_number = {}".format(nam, emaill, cel_num))
        elif emaill != "" and code != '' and nam != "":
            c.execute("delete from contacs where name = '{}', email = '{}', contry_code = '{}'".format(nam, emaill, code))
        elif cel_num != 0  and code != '' and nam != "":
            c.execute("delete from contacs where name = '{}', cell_number = {}, contry_code = '{}'".format(nam, code, code))
        elif cel_num != 0  and code != '' and emaill != "":
            c.execute("delete from contacs where email = '{}', cell_number = {}, contry_code = '{}'".format(emaill, code, code))
        else:
            c.execute("delete from contacs where name = '{}', email = '{}', cell_number = {}, contry_code = '{}'".format(nam, emaill, code, code))
        con.commit()
        con.close()
        self.clear()
        
    def edit_name(self):
        'edit by name we got name and find it in db and replace the another item'
        lst = r_file()
        nam = self.v1.get()
        if nam != '':
            code = self.v3.get()
            cel_num = self.v4.get()
            emaill = self.v5.get()
            for  i in lst:
                if i.split()[1] != code:
                    pass
                elif i.split()[1] == code and cel_num != 0 and emaill != '':
                    contry = i.split()[0]
                    co_abrivation = i.split()[2]
                    con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
                    c = con.cursor()
                    c.execute("update contacs set email = '{}', cell_number = {}, contry_code = '{}', contry = '{}', contry_abrivision = '{}' where name = '{}'".format(emaill, cel_num, code, contry, co_abrivation, nam))
                    con.commit()
                    con.close()
                    self.clear()
                else:
                    self.clear()
                    self.tablee(())

    def edit_phone(self):
        'edit by phone we got name and find it in db and replace the another items'
        lst = r_file()
        cel_num = self.v4.get()
        if cel_num != 0:
            code = self.v3.get()
            nam = self.v1.get()
            emaill = self.v5.get()
            for  i in lst:
                if i.split()[1] != code:
                    pass
                elif i.split()[1] == code and nam != '' and emaill != '':
                    contry = i.split()[0]
                    co_abrivation = i.split()[2]
                    con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
                    c = con.cursor()
                    c.execute("update contacs set name = '{}' ,email = '{}', contry_code = '{}', contry = '{}', contry_abrivision = '{}' where cell_number = {}".format(nam, emaill, code, contry, co_abrivation, cel_num))
                    con.commit()
                    con.close()
                else:
                    self.clear()
                    self.tablee(())

    def edit_email(self):
        'edit by email we got name and find it in db and replace the another items'
        lst = r_file()
        emaill = self.v5.get()
        if emaill != '':
            code = self.v3.get()
            nam = self.v1.get()
            cel_num = self.v4.get()
            for  i in lst:
                if i.split()[1] != code:
                    pass
                elif i.split()[1] == code and nam != '' and cel_num != 0:
                    contry = i.split()[0]
                    co_abrivation = i.split()[2]
                    con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
                    c = con.cursor()
                    c.execute("update contacs set name = '{}' ,cell_number = {}, contry_code = '{}', contry = '{}', contry_abrivision = '{}' where email = '{}'".format(nam, cel_num, code, contry, co_abrivation, emaill))
                    con.commit()
                    con.close()
                else:
                    self.clear()
                    self.tablee(())

    def clear_db(self):
        '''clear all item in database'''
        con = connect("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\contact\contact.db")
        c = con.cursor()
        c.execute("select name from contacs")
        q = c.fetchall()
        for i in q:
            c.execute("delete from contacs where name = '{}'".format(i[0]))
        con.commit()
        con.close()

w = Tk()
ob = Graphic(w)
w.mainloop()
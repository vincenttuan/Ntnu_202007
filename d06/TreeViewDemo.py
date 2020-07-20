import tkinter
from tkinter import ttk # 匯入資源

win = tkinter.Tk()
tree = ttk.Treeview(win) #表格

tree["columns"]=("姓名", "年齡", "身高")
tree.column("姓名", width=100) # 欄位
tree.column("年齡", width=100)
tree.column("身高", width=100)
tree.heading("姓名", text="姓名-name") # Title
tree.heading("年齡", text="年齡-age")
tree.heading("身高", text="身高-tall")

# insert(parent, index, iid=None, **kw)
# parent is the item ID of the parent item, or the empty string to create a new top-level item
tree.insert("", 0, text="line1" ,values=("A","21","160")) #插入資料，
tree.insert("", 1, text="line1" ,values=("B","22","161"))
tree.insert("", 2, text="line1" ,values=("C","23","162"))
tree.insert("", 3, text="line1" ,values=("D","24","163"))

tree.pack()
win.mainloop()
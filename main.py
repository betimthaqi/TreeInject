from tkinter import *
import os
from tkinter import ttk
import requests


def fill_tree(treeview, node):
    if treeview.set(node, "type") != 'directory':
        return
    path = treeview.set(node, "fullpath")
    treeview.delete(*treeview.get_children(node))

    for p in os.listdir(path):
        p = os.path.join(path, p)
        ptype = None
        if os.path.isdir(p):
            ptype = 'directory'

        fname = os.path.split(p)[1]
        oid = treeview.insert(node, 'end', text=fname, values=[p, ptype])
        if ptype == 'directory':
            treeview.insert(oid, 0, text='dummy')


def update_tree(event):
    treeview = event.widget
    fill_tree(treeview, treeview.focus())


def create_root(treeview, startpath):
    dfpath = os.path.abspath(startpath)
    node = treeview.insert('', 'end', text=dfpath,
                           values=[dfpath, "directory"], open=True)
    fill_tree(treeview, node)


def show_tree():
    newWindow = Toplevel(master)
    newWindow.title("Host Tree Structure")
    newWindow.geometry("500x500")
    treeview = ttk.Treeview(newWindow, columns=(
        "fullpath", "type"), displaycolumns='')
    treeview.pack(fill='both', expand=True)
    create_root(treeview, '.')
    treeview.bind('<<TreeviewOpen>>', update_tree)


def Take_input(inputurl, inputpayload, output):
    url = inputurl.get("1.0", "end-1c")
    payload = inputpayload.get("1.0", "end-1c")
    target = str(url) + payload
    try:
        results = requests.get(url=target)
        if "www-data" in str(results.text):
            output.insert(END, 'OS Command Injection Successfully!')
        else:
            output.insert(END, "Nothing Found!")
    except ConnectionError:
        print("Connection Error. Try Again.")


def os_injection():
    root = Toplevel(master)
    root.title("Os command injection")
    root.geometry("470x300")
    l = Label(root, text="Enter the url like this \nschema://subdomain.domain.tld/path/document.extension?parameter=",
              fg="grey",
              )
    inputtxt = Text(root,
                    height=0,
                    width=55,
                    bg="light yellow")

    l1 = Label(root, text="Enter the url payload",
               fg="grey",
               )

    inputtxt1 = Text(root,
                     height=0,
                     width=25,
                     bg="light yellow")

    Output = Text(root, height=3,
                  width=14,
                  bg="light cyan")

    Display = Button(root, height=2,
                     width=12,
                     text="Test",
                     command=lambda: Take_input(inputtxt, inputtxt1, Output))
    l.pack()
    inputtxt.pack(pady=10)
    l1.pack()
    inputtxt1.pack(pady=10)
    Display.pack(pady=10)
    Output.pack()


if __name__ == '__main__':
    master = Tk()
    master.geometry("300x310")
    master.title("Detyra 13")
    label = Label(master,
                  text="Menu \n Choose the function",
                  fg="white",
                  bg="black",
                  width=50, )

    label.pack(pady=10)

    btn = Button(master,
                 text="HOST FOLDER TREE STRUCTURE", bg="green",
                 width=30,
                 height=5,
                 command=show_tree)

    btn1 = Button(master, bg="red",
                  width=30,
                  height=5,
                  text="OS COMMAND INJECTION TESTER",
                  command=os_injection)

    btn.pack(pady=10)
    btn1.pack(pady=10)
    mainloop()

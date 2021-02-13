# TreeInject

TreeInject is a GUI app python based using module tKinter, that supports 2 functionalities
  - Tree host dir. structure
  - OS Command injection

### Installation

TreeInject requires [Python](https://www.python.org/downloads/) v3+ to run.

Used modules for dev of TreeInject:
- [Tkinter](https://github.com/python/cpython/tree/master/Lib/tkinter/)
- [BeautifulSoup](https://github.com/waylan/beautifulsoup)

**Cloning repository**
```sh
$ git clone https://github.com/durajetz/internetscur
$ cd internetscur
$ python3 main.py
```

#  Functionality
<p align="center"><b><em>For the purpose of testing the program an Vulnerable website offline was used.</em></b></br></p>
<img src="https://media4.giphy.com/media/GijNtQfpydqijSROH7/giphy.gif" alt=""  width="320px">

*Choosing the function we want to implement, pops up new window*

<img src="https://media0.giphy.com/media/jw6Zy69bwWX3a1obDl/giphy.gif" alt="" width="320px">

*The structure of folders on the host where the application is located, which will be open after clicking on the first button*

<img src="https://media4.giphy.com/media/KPRU4rIJbDxUMmjow4/giphy.gif" alt=""  width="350px">

*Injection only giving the payload with the specific expression:*
```
eval(compile("""for x in range(1):\n import subprocess\n subprocess.check_output(r'COMMAND',shell=True)""",'','single'))
```
<img src="https://media4.giphy.com/media/JkzlYa6WGpphEsPr5J/giphy.gif" alt="" width="350px">

*Injection with custom payload expression:*

License
----

MIT

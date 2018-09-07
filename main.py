from tkinter import *

def do_popup(event=None):
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()

def select_all(event=None):
    root.focus_get().event_generate('<<SelectAll>>')

def undo(event=None):
    root.focus_get().event_generate('<<Undo>>')

def redo(event=None):
    root.focus_get().event_generate('<<Redo>>')

def copy(event=None):
    root.focus_get().event_generate('<<Copy>>')

def paste(event=None):
    root.focus_get().event_generate('<<Paste>>')

def cut(event=None):
    root.focus_get().event_generate('<<Cut>>')

def clear(event=None):
    root.focus_get().event_generate('<<Clear>>')

def nextLine(event=None):
    root.focus_get().event_generate('<<SelectNextLine>>')

def nextWord(event=None):
    root.focus_get().event_generate('<<SelectNextWord>>')

root=Tk()
root.title('Luna Editor')
print("\nLuna Editor Alpha")
print("Created by ivan770\n")

menubar = Menu(root)
menubar.add_command(label="Exit", command=root.quit)
root.config(menu=menubar)
print("Generated window menu")

S = Scrollbar(root)
print("Scrollbar ready")
T=Text(root,font='Consolas 11',wrap=WORD)
print("Textarea ready")
popup = Menu(root, tearoff=0)
submenu = Menu(popup, tearoff=0)
select = Menu(popup, tearoff=0)
submenu.add_command(label="Undo", \
                     accelerator="Ctrl+Z", \
                     command=lambda: \
                             undo())
submenu.add_command(label="Redo", \
                     accelerator="Ctrl+Y", \
                     command=lambda: \
                             redo())
submenu.add_separator()
submenu.add_command(label="Select All", \
                     accelerator="Ctrl+A", \
                     command=lambda: \
                             select_all)
submenu.add_command(label="Copy", \
                     accelerator="Ctrl+C", \
                     command=lambda: \
                             copy())
submenu.add_command(label="Paste", \
                     accelerator="Ctrl+V", \
                     command=lambda: \
                             paste())
submenu.add_command(label="Cut", \
                     accelerator="Ctrl+X", \
                     command=lambda: \
                             cut())
submenu.add_command(label="Clear", \
                     command=lambda: \
                             clear())
select.add_command(label="Select Next Line", \
                     accelerator="Ctrl+W", \
                     command=lambda: \
                             nextLine())
select.add_command(label="Select Next Word", \
                     accelerator="Ctrl+Q", \
                     command=lambda: \
                             nextWord())
popup.add_cascade(label="Operations", menu=submenu)
popup.add_cascade(label="Select", menu=select)

T.bind("<Control-q>", nextWord)
T.bind("<Control-w>", nextLine)
T.bind("<Control-x>", cut)
T.bind("<Control-v>", paste)
T.bind("<Control-c>", copy)
T.bind("<Control-z>", undo)
T.bind("<Control-y>", redo)
T.bind("<Control-a>", select_all)
T.bind("<Button-3>", do_popup)

S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=BOTH, expand=YES)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
print(root.winfo_screenheight)
print(root.winfo_screenwidth)
T.pack()
root.mainloop()

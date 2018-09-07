from tkinter import *

def do_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()

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
                             root.focus_get().event_generate('<<Undo>>'))
submenu.add_command(label="Redo", \
                     accelerator="Ctrl+Y", \
                     command=lambda: \
                             root.focus_get().event_generate('<<Redo>>'))
submenu.add_separator()
submenu.add_command(label="Select All", \
                     accelerator="Ctrl+A", \
                     command=lambda: \
                             root.focus_get().event_generate('<<SelectAll>>'))
submenu.add_command(label="Copy", \
                     accelerator="Ctrl+C", \
                     command=lambda: \
                             root.focus_get().event_generate('<<Copy>>'))
submenu.add_command(label="Paste", \
                     accelerator="Ctrl+V", \
                     command=lambda: \
                             root.focus_get().event_generate('<<Paste>>'))
submenu.add_command(label="Cut", \
                     accelerator="Ctrl+X", \
                     command=lambda: \
                             root.focus_get().event_generate('<<Cut>>'))
submenu.add_command(label="Clear", \
                     command=lambda: \
                             root.focus_get().event_generate('<<Clear>>'))
select.add_command(label="Select Next Line", \
                     command=lambda: \
                             root.focus_get().event_generate('<<SelectNextLine>>'))
popup.add_cascade(label="Operations", menu=submenu)
popup.add_cascade(label="Select", menu=select)

T.bind("<Button-3>", do_popup)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=BOTH, expand=YES)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
print(root.winfo_screenheight)
print(root.winfo_screenwidth)
T.pack()
root.mainloop()

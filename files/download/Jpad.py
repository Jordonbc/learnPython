from tkinter import *
import tkinter.dialog
def jpadEditor(file=None):
    global askopenfilename
    """
    Starts Jpad
    """
    global rootJpad
    colour = "#00ff00"

    width = "500"
    height = "400"

    widthHeight = width + "x" + height

    rootJpad = Tk()

    sWidth = rootJpad.winfo_screenwidth()
    sHeight = rootJpad.winfo_screenheight()

    rootJpad.title("Jpad")
    rootJpad.geometry(widthHeight)
    rootJpad.maxsize(sWidth, sHeight)
    rootJpad.minsize("200", "200")

    textPad = Text(rootJpad)
    textPad.configure(bg=colour)
    textPad.focus()

    textPad.pack(expand=YES, fill=BOTH)

    font = ["Arial", "11", "normal"]

    textPad.configure(font=(font[0], int(font[1]), font[2]))

    def chfont():
        def apply():
            try:
                textPad.configure(font=(font1.get(), int(font2.get()), font3.get()))
                font[0] = font1.get()
                font[1] = font2.get()
                font[2] = font3.get()

                rootFont.destroy()
            except:
                msg.configure(text="Whoops, something went wrong while applying your font!")

        rootFont = Tk()
        rootFont.title("Font")
        rootFont.geometry("320x110")

        font1 = Entry(rootFont)
        font2 = Entry(rootFont)
        font3 = Entry(rootFont)

        font1.insert(0, font[0])
        font2.insert(0, font[1])
        font3.insert(0, font[2])

        applyButton = Button(rootFont, text="Apply Font", command=apply)
        msg = Label(rootFont)

        font1.pack()
        font2.pack()
        font3.pack()
        applyButton.pack()
        msg.pack()

        rootFont.mainloop()

    def open_command():
        file =  tkFileDialog.askopenfilename(defaultextension=".txt",
                               filetypes=[("Text Files", ".txt"), ("All Files")])

        rootJpad.title("Jpad Text Editor" + "     File: " + file)
        file = open(file, "r")
        if file != None:
            contents = file.read()
            textPad.delete(0.0, END)
            textPad.insert(0.0, contents)
            file.close()

    def save_command():
        file = asksaveasfilename(defaultextension=".txt",
                                 filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        rootJpad.title("Jpad Text Editor" + "     File: " + file)
        file = open(file, "w")
        if file != None:
            # slice off the last character from get, as an extra return is added
            data = textPad.get(0, 0)
            file.write(data)
            file.close()

    def exit_command():
        closeApp()

    def new():
        rootJpad.title("Jpad Text Editor" + "     File: New File")
        textPad.delete(0.0, END)

    if file != None:
        rootJpad.title("Jpad Text Editor" + "     File: " + str(file))
        file = open(file, "r")
        contents = file.read()
        textPad.delete(0.0, END)
        textPad.insert(0.0, contents)
        file.close()

    menu = Menu(rootJpad)
    rootJpad.config(menu=menu)
    rootJpad.config(bg=colour)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=new)
    filemenu.add_command(label="Open...", command=open_command)
    filemenu.add_command(label="Save", command=save_command)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_command)

    fontMenu = Menu(menu)
    menu.add_cascade(label="Font", menu=fontMenu)
    fontMenu.add_command(label="font", command=chfont)

    rootJpad.mainloop()
jpadEditor()

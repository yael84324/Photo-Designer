
from tkinter import *
from tkinter.filedialog import askopenfilename
from Image import Img
class Window:
    def __init__(self,win):
        self.img=None
        self.input=None
        self.window_design()
        self.btn1 = Button(win,text="open image",command=self.select_image,pady=10,padx=10,width=10,font="Cafe")
        self.btn2 = Button(win, text="effects",command=self.effects,pady=10,padx=10,width=10,font="Cafe")
        self.btn3 = Button(win, text="cut image",command=self.cut_image,pady=10,padx=10,width=10,font="Cafe")
        self.btn4 = Button(win, text="enter text",command=self.enter_text,pady=10,padx=10,width=10,font="Cafe")
        self.btn5 = Button(win, text="draw shapes",command=self.draw_shapes,pady=10,padx=10,width=10,font="Cafe")
        self.btn6 = Button(win, text="save changes",command=self.save,pady=10,padx=10,width=10,font="Cafe")
        self.btn7 = Button(win, text="exit",pady=10,command=self.exit,padx=10,width=10,font="Cafe")
        self.btn8 = Button(win, text="rotate",pady=10,command=self.rotate,padx=10,width=10,font="Cafe")
        self.position()
    def position(self):
        self.btn1.grid(row=0, column=2)
        self.btn2.grid(row=1, column=2)
        self.btn3.grid(row=2, column=2)
        self.btn4.grid(row=3, column=2)
        self.btn5.grid(row=0, column=4)
        self.btn6.grid(row=1, column=4)
        self.btn7.grid(row=2, column=4)
        self.btn8.grid(row=3, column=4)
    def window_design(self):
         win.title("photo design")
         win.configure(bg="#b573bd",borderwidth=10,padx=10,pady=10)
         icon = PhotoImage(file="icon.PNG")
         win.iconphoto(1, icon)
    def effects(self):
        effectwin=Tk()
        effectwin.configure(bg="#b573bd", borderwidth=10, padx=10, pady=10)
        effectwin.title("effects")
        self.img.ImgBeforeEffects()
        Label(effectwin, text="please choose an effect",font="Cafe").grid()
        Button(effectwin,text="black and white",command=self.img.black_white,font="Cafe").grid()
        Button(effectwin, text="show just the edges", command=self.img.just_edges,font="Cafe").grid()
        Button(effectwin, text="blur", command=self.img.blur,font="Cafe").grid()
        Button(effectwin, text="reastart image", command=self.img.show_image,font="Cafe").grid()
        Button(effectwin,text="colorful",command=self.img.colorful,font="Cafe").grid()
        effectwin.geometry("300x400+300+400")
    def select_image(self):
        file_name = askopenfilename()
        self.img=Img("your image!",file_name)
    def enter_text(self):
        textwin=Tk()
        self.input=Entry(textwin,font="Cafe")
        self.input.grid(row=0,column=0)
        Button(textwin,text="put this text", font="Cafe",command=self.text).grid(row=1,column=0)
        textwin.mainloop()
    def text(self):
        global result
        result = str(self.input.get())
        self.img.add_text(result)
    def cut_image(self):
        self.img.cut()
    def draw_shapes(self):
        draw_win = Tk()
        draw_win.title("draw shapes")
        draw_win.geometry("400x200+300+500")
        lbl=Label(draw_win, text="please choose a shape",font="Cafe")
        global listbox
        listbox = Listbox(draw_win,height =4,width = 10,activestyle = 'dotbox',font="Cafe")
        listbox.bind('<ButtonRelease-1>', self.get_list)
        listbox.insert(END, "Rectangle")
        listbox.insert(END, "Circle")
        listbox.insert(END, "Line")
        lbl.pack()
        listbox.pack()
    def get_list(self,event):
        index = listbox.curselection()[0]
        seltext = listbox.get(index)
        if seltext=="Rectangle":
            self.img.rectangle()
        if seltext=="Circle":
            self.img.circle()
        if seltext=="Line":
            self.img.line()
    def save(self):
        self.img.save()
    def exit(self):
        self.img.exit()
        quit()
    def rotate(self):
        self.img.rotate()
win=Tk()
Window(win)
win.mainloop()
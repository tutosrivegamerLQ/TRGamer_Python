from tkinter import * 

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
 
        self.title("Hello World TRG")
        self.minsize(500,400)

root = Root()

root['bg'] = "blue"

count = 0
bg1,bg2,bg3,bg4,bg5,bg6 = "#66ffff","yellow","blue","green","black","#6666ff"

fg1,fg2,fg3,fg4,fg5,fg6 = "#ff6666","#b366ff","#66ff66","#d9ff66","#ffff66","#009999"

def clicked():
    global count
    count = count + 1
    print("Has clicked", count ,"times")

btn1 = Button(root, text = "Click Me!", command = clicked, bg = bg3, fg = fg4)
btn1.pack()
text1 = Label(root, text = "Hello World", bg = "#ff0000")
text1.pack(expand = True)
root.mainloop()
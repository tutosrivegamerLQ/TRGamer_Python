from tkinter import *
import random as rd

class Window():
    def __init__(self, width=None, height=None, bgColor=None, title=None, position=None):
        self.__width=width
        self.__height=height
        self.__bgColor=bgColor
        self.__title=title
        self.__position=position

    def createWindow(self):
        self.__root=Tk()
        self.__root.title(f'{self.__title}')
        self.__root['bg']=self.__bgColor

        self.__winfo_w=self.__root.winfo_screenwidth()
        self.__winfo_h=self.__root.winfo_screenheight()
        __w_win=(self.__winfo_w-self.__width)//2
        __h_win=(self.__winfo_h-self.__height)//2

        __centered=f'{self.__width}x{self.__height}+{__w_win}+{__h_win}' ##
        __centered_left=f'{self.__width}x{self.__height}+{self.__winfo_w*2%2}+{__h_win}' ##
        __centered_right=f'{self.__width}x{self.__height}-{__w_win%2}+{__h_win}' ##

        __top_left=f'{self.__width}x{self.__height}+{self.__winfo_w%2}+{__h_win%2}' ##
        __top_right=f'{self.__width}x{self.__height}-{self.__winfo_w%2}+{__h_win%2}' ##

        __bottom_left=f'{self.__width}x{self.__height}+{self.__winfo_w%2}-{__h_win%40}' ##
        __bottom_right=f'{self.__width}x{self.__height}-{self.__winfo_w%2}-{__h_win%40}' ##

        __random=f'{self.__width}x{self.__height}+{rd.randint(1,self.__winfo_w-self.__width)}+{rd.randint(1, self.__winfo_h-self.__height)}' ##

        if self.__position=='center':
            self.__geometry=__centered
        elif self.__position=='center-right':
            self.__geometry=__centered_right
        elif self.__position=='center-left':
            self.__geometry=__centered_left
        elif self.__position=='top-left':
            self.__geometry=__top_left
        elif self.__position=='top-right':
            self.__geometry=__top_right
        elif self.__position=='bottom-right':
            self.__geometry=__bottom_right
        elif self.__position=='bottom-left':
            self.__geometry=__bottom_left
        elif self.__position=='random':
            self.__geometry=__random

        self.__root.geometry(f'{self.__geometry}')

    def add_widget(self, widget, text=None, bg=None, fg=None):
        if text:
            self.__widget=widget(self.__root, text=text, bg=bg, fg=fg)
            return self.__widget
        else:
            self.__widget=widget(self.__root, bg=bg, fg=fg)
            return self.__widget

    def init_window(self):
        self.__root.mainloop()

class Test1(Window):
    pass

if __name__=='__main__':
    colors=['red', 'purple', 'blue', 'white', 'black', 'green', 'gray', 'yellow', 'orange', '#6600ff', '#00ff4c', '#ff008c', '#d900ff', '#0080ff', '#00ffae', '#a5ff50', '#ff7f50']
    color=rd.choice(colors)
    title='Position Window - Test '
    app=Test1(500, 300, color, title, 'center')
    app.createWindow()
    title=app.add_widget(Label, 'CENTER', 'red', 'white')
    title.place(relx=0.45)
    title.configure(width=12)
    app.init_window()
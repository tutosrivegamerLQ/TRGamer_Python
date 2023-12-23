from tkinter import *
from tkinter import messagebox as ms
import math as mt
import random as rm


limit=[]
from_to=[]

class win:
    def __init__(self):
        self.root() #load root main
        self.widgets_home()
        self.copyright()

    def root(self):
        self.rootWin=Tk() #window Tk
        self.rootWin.resizable(False, False)
        self.win_w=self.rootWin.winfo_screenwidth() #width window
        self.win_h=self.rootWin.winfo_screenheight() #height window
        self.widthWin=550
        self.heightWin=275
        self.width_w=(self.win_w - self.widthWin) // 2 #width window // 2
        self.height_w=(self.win_h - self.heightWin) // 2 #height window // 2
        self.rootWin.title("Guess Number") #title window
        self.rootWin.geometry("%dx%d+%d+%d" % (self.widthWin, self.heightWin, self.width_w, self.height_w)) #geometry window
        self.rootWin['bg'] = "black"

    def widgets_home(self):
        #variables
        self.FROMStr=StringVar()
        self.TOStr=StringVar()
        self.infoSTR=StringVar()
        self.spaceSTR=StringVar()
        
        #Declaration widgets
        self.inp_FROM=Entry(self.rootWin)
        self.inp_TO=Entry(self.rootWin)
        self.lab_info_begin=Label(self.rootWin, textvariable=self.infoSTR, font=("Helvetica", 14), bg="black", fg="white")
        self.lab_FROM=Label(self.rootWin, textvariable=self.FROMStr, bg="black", fg="white")
        self.lab_TO=Label(self.rootWin, textvariable=self.TOStr, bg="black", fg="white")
        self.w_space=Label(self.rootWin, textvariable=self.spaceSTR, font=("Helvetica", 14), bg="black", fg="white")

        #set strings variables
        self.FROMStr.set("DESDE: ")
        self.TOStr.set("HASTA: ")
        self.infoSTR.set("Introduce los límites del juego:")

        #Widgts position
        self.lab_info_begin.place(relx=0.5, y=40, anchor=CENTER)
        self.inp_FROM.place(relx=0.38, y=100, anchor=CENTER)
        self.inp_TO.place(relx=0.75, y=100, anchor=CENTER)

        self.w_space.place(relx=0.5, y=215, anchor=CENTER)
        self.lab_FROM.place(relx=0.2, y=100, anchor=CENTER)
        self.lab_TO.place(relx=0.57, y=100, anchor=CENTER)

    def widgets_game(self):
        # Variable str
        self.titleStr=StringVar() #var to strings labels title
        self.nTypedStr=StringVar() #var to strings labels
        self.liveStr=StringVar()
        self.justtypedStr=StringVar()
        self.number_near=StringVar()

        # Widgets creation
        self.title=Label(self.rootWin, textvariable=self.titleStr, bg="black", fg="white")
        self.inp_main=Entry(self.rootWin)
        self.show_n_typed=Label(self.rootWin, textvariable=self.nTypedStr, wrap=400, font=("Helvetica", 12), bg="black", fg="white")
        self.live=Label(self.rootWin, textvariable=self.liveStr, fg="#ff0000", font=("Helvetica", 14), bg="black")
        self.just_Typed_Number=Label(self.rootWin, textvariable=self.justtypedStr, bg="black", fg="white")
        self.number_near_lb=Label(self.rootWin, textvariable=self.number_near, bg="black", fg="red")

        # Set strings to variable str
        self.titleStr.set(f'Inserte un número entre {from_to[0]} y {from_to[1]}')
        self.nTypedStr.set("Inserta un número para empezar")

        # Widgets position
        self.title.place(relx=0.5, y=20, anchor=CENTER)
        self.inp_main.place(relx=0.5, y=50, anchor=CENTER)
        self.show_n_typed.place(relx=0.5, y=130, anchor=CENTER)
        self.live.place(relx=0.9, y=20, anchor=CENTER)
        self.just_Typed_Number.place(relx=0.5, y=210, anchor=CENTER)
        self.number_near_lb.place(relx=0.5, y=175, anchor=CENTER)

    #put focus text in a entry
    def focusEntry(self, entrY):
        entrY.focus_set()

    def copyright(self):
        self.copySTR=StringVar()
        self.copyTRG=Label(self.rootWin, textvariable=self.copySTR, bg="black", fg="white")
        self.copySTR.set("© 2023 TUTOS RIVE GAMER")
        self.copyTRG.place(relx=0.5, y=260, anchor=CENTER)

class game(win):
    def __init__(self):
        super().__init__()
        self.run_home()

    #To execute logic for begin the game
    def run_home(self):
        self.PLAYstr=StringVar()
        self.btn_play=Button(self.rootWin, textvariable=self.PLAYstr, width=20, command=self.add_F_T, bg="black", fg="white")
        self.PLAYstr.set("JUGAR")
        self.btn_play.place(relx=0.5, y=170, anchor=CENTER)
        self.focusEntry(self.inp_FROM)
        self.rootWin.mainloop()

    #add the limits to list named from_to and run the second window or step
    def add_F_T(self):
        FROM=self.inp_FROM.get()
        TO=self.inp_TO.get()

        if not FROM and not TO:
            self.spaceSTR.set("Los dos campos están vacíos.")
        elif not FROM:
            self.spaceSTR.set("El campo 'DESDE' está vacío.")
        elif not FROM.isdigit() and not TO.isdigit():
            self.spaceSTR.set("Ambos campos deben ser enteros\n(sin decimal).")
        elif not FROM.isdigit():
            self.spaceSTR.set("El campo 'DESDE'\ndebe ser un entero (sin decimal).")
        elif not TO:
            self.spaceSTR.set("El campo 'HASTA' está vacío.")
        elif not TO.isdigit():
            self.spaceSTR.set("El campo El campo 'HASTA'\ndebe ser un entero (sin decimal).")
        elif int(TO) < int(FROM) or int(FROM) == int(TO):
            self.spaceSTR.set("El campo 'HASTA' no puede\n ser menor o igual al campo 'PARA")
        elif int(FROM) == 0 or int(TO) == 0: 
            self.spaceSTR.set("Ninguno de los dos\n números puede ser cero (0)")
        else:
            from_to.append(int(FROM))
            from_to.append(int(TO)) #Append the limits from the game
            print(from_to)
            self.destroy_wid(self.inp_TO) #Destroy this input
            self.destroy_wid(self.btn_play) #Destroy this button
            self.destroy_wid(self.inp_FROM) #Destroy this input
            self.destroy_wid(self.lab_info_begin)
            self.destroy_wid(self.lab_TO)
            self.destroy_wid(self.lab_FROM)
            self.destroy_wid(self.w_space)
            self.widgets_game() #Put the widgets main in the window main
            self.run_game() #Run the main window
        

    def destroy_wid(self, widget):
        return widget.destroy()

    def destroy_window(self, window):
        destroy=window.quit()

    #Run the root window
    def run_game(self):
        self.live_count=5 if from_to[1] < 20 else 10 if from_to[1] < 30 else 15 #live number (try)
        print(self.live_count)
        
        self.btnCheckStr=StringVar()
        self.btn_check=Button(self.rootWin, textvariable=self.btnCheckStr, relief="groove", command=self.getTextBtn, bg="black", fg="white")
        
        self.btnCheckStr.set("Revisar Número")
        self.liveStr.set("LIVE: " + str(self.live_count))

        self.btn_check.place(relx=0.5, y=90, anchor=CENTER)
        self.inp_main.bind("<Return>", self.getText)
        self.focusEntry(self.inp_main)
        
        self.number_win=rm.randint(from_to[0], from_to[1])
        print(self.number_win)
        self.rootWin.mainloop()

    #Get text of entry by enter
    def getText(self, event):
        self.GET=self.inp_main.get()
        self.showGet(self.GET)
        self.win_check(self.GET)
        print(self.GET)
        return self.GET
        
    #Get text of entry by button
    def getTextBtn(self):
        self.GET=self.inp_main.get()
        self.showGet(self.GET)
        self.win_check(self.GET)
        print(self.GET)
        return self.GET
    
    def win_check(self, number):
        if not number:
            pass
        elif not number.isdigit():
            pass
        elif number and int(number) == self.number_win:
            self.rootWin.destroy()
            self.window_win()
        elif int(number) == self.trunc_isclose(self.number_win):
            self.number_near_lb.place(relx=0.5, y=175, anchor=CENTER)
            self.number_near.set("¡CERCA, MUY CERCA!")
            self.rootWin.after(3000, lambda: self.number_near_lb.place_forget())
        elif int(number) == self.trunc_isclose2(self.number_win):
            self.number_near.set("UN POCO LEJOS, PERO ¡ÁNIMO!")
        elif int(number) == self.trunc_isclose3(self.number_win):
            self.number_near.set("YA ESTÁS LEJOS")
        elif self.live_count == 0:
            self.rootWin.destroy()
            self.window_game_over()
    
    def trunc_isclose(self, number):
        truncado=mt.trunc(int(number)/1.002)
        print("TR1: ", truncado)
        return truncado

    def trunc_isclose2(self, number):
        truncado=mt.trunc(int(number)/1.004)
        print("TR2: ", truncado)
        return truncado

    def trunc_isclose3(self, number):
        truncado=mt.trunc(int(number)/1.005)
        print("TR3: ", truncado)
        return truncado

    def showGet(self, get):
        if not get:
            self.just_Typed_Number.place(relx=0.5, y=210, anchor=CENTER)
            self.justtypedStr.set("El campo está vacío")
            self.rootWin.after(2500, lambda: self.just_Typed_Number.place_forget())
        elif not get.isdigit():
            self.just_Typed_Number.place(relx=0.5, y=210, anchor=CENTER)
            self.justtypedStr.set(f"¡Inserta un número entero (sin decimales)!")
            self.rootWin.after(2500, lambda: self.just_Typed_Number.place_forget())
        elif len(limit) > 0 and int(get) in limit:
            self.just_Typed_Number.place(relx=0.5, y=210, anchor=CENTER)
            self.justtypedStr.set("¡Ya se insertó este número!")
            self.rootWin.after(2500, lambda: self.just_Typed_Number.place_forget())
        elif int(get) > from_to[1]:
            self.just_Typed_Number.place(relx=0.5, y=210, anchor=CENTER)
            self.justtypedStr.set(f"¡Inserta un número menor a {from_to[1]}!")
            self.rootWin.after(2500, lambda: self.just_Typed_Number.place_forget())
        else:
            limit.append(int(self.GET))
            self.nTypedStr.set("Números insertados: " + str(limit))
            self.live_count-=1
            self.liveStr.set("LIVE: " + str(self.live_count))

    def window_win(self):
        self.textWin="¡Felicidades has ganado, bien hecho!" if self.live_count > self.live_count/2 else "Buen trabajo"
        
        self.window_win=Tk()
        self.window_win.resizable(False, False)
        self.win_w=self.window_win.winfo_screenwidth() #width window
        self.win_h=self.window_win.winfo_screenheight() #height window
        self.widthWin=350
        self.heightWin=200
        self.width_w=(self.win_w - self.widthWin) // 2 #width window // 2
        self.height_w=(self.win_h - self.heightWin) // 2 #height window // 2
        self.window_win.title("¡Felicidades has ganado!") #title window
        self.window_win.geometry("%dx%d+%d+%d" % (self.widthWin, self.heightWin, self.width_w, self.height_w)) #geometry window
        self.window_win['bg']="lightblue"

        self.winSTR=StringVar()

        self.image_win=Label(self.window_win, textvariable=self.winSTR)
        self.image_win.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.winSTR.set(self.textWin)

        self.window_win.mainloop()


    def window_game_over(self):
        self.textGm="Has perdido"
        self.window_gm=Tk()
        self.window_gm.resizable(False, False)
        self.win_w=self.window_gm.winfo_screenwidth() #width window
        self.win_h=self.window_gm.winfo_screenheight() #height window
        self.widthWin=350
        self.heightWin=200
        self.width_w=(self.win_w - self.widthWin) // 2 #width window // 2
        self.height_w=(self.win_h - self.heightWin) // 2 #height window // 2
        self.window_gm.title("¡Has perdido!") #title window
        self.window_gm.geometry("%dx%d+%d+%d" % (self.widthWin, self.heightWin, self.width_w, self.height_w)) #geometry window
        self.window_gm['bg']="red"

        self.winSTR=StringVar()

        self.image_gm=Label(self.window_gm, textvariable=self.winSTR)
        self.image_gm.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.winSTR.set(self.textGm)

        self.window_gm.mainloop()
        

if __name__ == "__main__":
    app = game()
    print("Limit: ", limit)
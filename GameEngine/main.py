#python3.9
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import sys
from datetime import datetime
import engine as en
import helpengine as engh
import easygui as eg
import easyguihelp as egh



def main():


    def logon(wantlog = "log", logname = "Log"):
        try:
            with open("debug.log", mode = "w") as logfile:
                logfile.writelines("["+logname+"]"+":"+wantlog+"\n")
                logfile.close()
        except:
            print("eR")
            
    
    Start = Tk()
    
    def sm():
        Engine = Tk()
        Engine.geometry("1000x800")
        Engine.title("Scpycon 1.0.0")
        Engine.iconbitmap(Engine, default = "C:\\Users\\tekiw\\Desktop\\GameEngine\\0.ico")#?#?#?#
        
        
        def sae():
            Files = [
                ('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Scratch Project version 3.x', '*.sb3'), 
             ('GameEngine File(Game(Scpycon Game Engine(version1.0)) or Application(Scpycon(Beta)))', '*.ge; *.pe')
             ]
            file = asksaveasfilename(filetypes=Files, defaultextension=Files)
            a = file
            try:
                with open(a, "w") as f:
                    f.write("@Game Engine File next are ")
                    f.close()
            except:
                showerror("Erorr", "OpenErorr")
                logon("showerror open erorr","logErorr")
        
        
        def op():
            filelist = [("GameEngine File"
                         , "*.ge*.pe")
                        , ("Scratch Project Version 3.x"
                           , "*.sb3")
                        , ("Python File"
                           , "*.py")
                        ]
            filed = askopenfilename(defaultextension = filelist
                                    , filetypes = filelist
                                    , title = "Open"
                                    )
        
        
        open_1 = Button(Engine
                        , text = "open"
                        , padx = 0
                        , pady = 0
                        , bd = 0
                        , command = lambda: op()
                        )
        save = Button(Engine
                  , text = "Save"
                  , padx=0
                  , pady=0
                  , bd = 0
                  , command =lambda: sae()
                  )
        run = Button(Engine
                 , text = "Run"
                 , padx = 0
                 , pady = 0
                 , bd = 0 
                 )
        lang = Button(Engine
                  , text = "lang"
                  , padx = 0
                  , pady = 0
                  , bd = 0
                  , command = Erorrh
                  )
        
        
        open_1.pack(side = TOP, padx = 0, pady = 0)
        save.pack(side = LEFT, padx = 0, pady = 0)
        run.pack(side = RIGHT, padx = 0, pady = 0)
        lang.pack(side = BOTTOM, padx = 0, pady = 0)
        Engine.mainloop()
    
    def pp():
        print("Start!")
        
        
    def versi():
        showinfo("version","1.0")
        
        
    def Erorrh():
        showerror("ERORR", "未开放\nNOT OPEN,PLEASE GO TO 1.0.1")#之后实现(v:1.0.1)
        logon("Erorr", "NO start.")
        
    def ex():
        ab = askyesno("exit","确定要退出本GameEngine启动器吗?\nDo you want exit the GAME ENGINE Start?")
        if ab == False:
            pass
        else:
            sys.exit()
            

    Lab = Label(Start
            , anchor = "w"
            , text = "This is GameEngine?\\(like Scratch?)\n\n\nPress Start start it.\n\n\n这是游戏引擎?\\（类似Scratch？）\n\n\n按下start启动它"
            )
    B1_start = Button(Start
                  , activebackground = "white"
                  , activeforeground = "white"
                  , bd = 1
                  , fg = "black"
                  , highlightcolor = "white"
                  , padx = 3
                  , pady = 2
                  , text = "start"
                  , command = sm
                  )
    B2_help = Button(Start
                 , activebackground = "white"
                 , activeforeground = "white"
                 , bd = 1
                 , fg = "black"
                 , highlightcolor = "white"
                 , padx = 3
                 , pady = 2
                 , text = "help"
                 , command = Erorrh
                 )
    B3_exit = Button(Start
                 , activebackground = "white"
                 , activeforeground = "white"
                 , bd = 1
                 , fg = "black"
                 , highlightcolor = "white"
                 , padx = 3
                 , pady = 2
                 , text = "exit"
                 , command = ex
                 )
    B4_version = Button(Start
                 , activebackground = "white"
                 , activeforeground = "white"
                 , bd = 1
                 , fg = "black"
                 , highlightcolor = "white"
                 , padx = 3
                 , pady = 2
                 , text = "version"
                 , command = versi
                 )
    
    Start.title("GameEngineStart")
    Start.geometry("400x300")
    Start.call("wm","iconphoto", Start._w, PhotoImage(file = "asset/exp.png"))
    B1_start.pack()
    B2_help.pack()
    B3_exit.pack()
    B4_version.pack()
    Lab.pack()
    
    Start.mainloop()

main()
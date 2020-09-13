# -----------------------------------------------------------
# "PRINT PDF python"
#
# (C) 2020 M.ROHAN FAROOQUI, Islamabad,Pakistan
# Email   : rohanfarooqui218@gmail.com
# Webiste : http://www.rohanfarooqui.wordpress.com
# Github  : LOL-32
# -----------------------------------------------------------


###Imports

##Gui Libraries
from tkinter import *
import tkinter.ttk as ttk
#MSG dialog box
from tkinter import messagebox
#File Open Dialog Box
from tkinter import filedialog
#Tkinter Theme File
from ttkthemes import ThemedStyle
##Other Libraries
import os
import  win32api 
import  win32print

###Variables
dirpath = os.getcwd()
GHOSTSCRIPT_PATH = dirpath+"\Print_Lib"+"\GHOSTSCRIPT\\"+"bin"+"\gswin32.exe"
GSPRINT_PATH     = dirpath+"\Print_Lib"+"\GSPRINT\\"+"gsprint.exe"

###Code Start HERE###
class Search_Window(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit():
        self.window.destroy()

    def browse_folder(self):
        path =  filedialog.askopenfilename(parent=root,title = "Select file",filetypes = [("PDF files","*.pdf*")])
        self.entry.insert(0, path)
        self.entry.configure(state='disabled')
   
    def search_file_and_print(self):
        input_entry = self.entry.get()
        if(len(input_entry) == 0):
            messagebox.showinfo("Error ⚠", "Please select PDF file .. !!")
        else:
            if(os.path.isfile(input_entry) == True):
                currentprinter = win32print.GetDefaultPrinter()
                win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "'+input_entry+'"', '.', 0)
                messagebox.showinfo("✔✔✔", "File :  "+input_entry+".pdf\n"+"Print Successfully....!!!")
            else:
                messagebox.showinfo("Error ⚠", "There is no file : "+input_entry+".pdf\n"+" on location : "+pathh+"/")



    ###MAIN GUI create
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Print PDF -- Python')
        self.root.geometry("600x250")
        style = ThemedStyle(self.root)
        style.set_theme("radiance")
        self.root.resizable(width=False, height=False)
        try:
            self.root.iconbitmap("Images\print.ico")
        except:
            pass
        
        ##MAIN WINDOW        
        #LOGO AREA & LINE
        self.root.logo_1 =PhotoImage(file = 'Images/logo.png')
        label = Label(self.root,image=self.root.logo_1,width="90",height="90")
        label.place(relx=0.42, rely=0.01,anchor=NW)
        label.image = self.root.logo_1
        h_line = Label(self.root, text="____________________________").place(relx=0.31, rely=0.38)
        
        #BROWSER BUTTON and PATH SHOW ENTRY BOX
        self.root.third_box=Frame(self.root,relief=SOLID,borderwidth=0)
        self.entry  = ttk.Entry(self.root.third_box,width="35",justify = CENTER,font = ('Times', 10, 'bold'))
        self.entry.grid(row=1,column=0,padx=5, pady=2)
        self.button = ttk.Button(self.root.third_box,text=" Browse Folder  ",width="13",command=self.browse_folder).grid(row=1,column=1,padx=5, pady=2)
        self.root.third_box.place(relx=0.15, rely=0.35, y=30)

        #BUTTON TO PRINT PDF FILE 
        self.button_generate= ttk.Button(self.root,text="  Print File  ",command=self.search_file_and_print).place(relx=0.4, rely=0.55, y=30)

        #COPYRIGHTS & WEBSITE LABEL
        self.name    = ttk.Label(self.root,text="M.ROHAN FAROOQUI ©",font = ('Times', 10, 'bold')).place(relx=0.001, rely=0.8, y=30)
        self.webiste = ttk.Label(self.root,text="http://www.rohanfarooqui.wordpress.com",font = ('Times', 9, 'bold')).place(relx=0.64, rely=0.8, y=30)



if __name__ == '__main__':
    root = Tk()
    Search_Window(root)
    root.mainloop()

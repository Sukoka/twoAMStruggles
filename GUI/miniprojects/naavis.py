from tkinter import*
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import ttk
import os   #for getting the path


root= Tk()

root.geometry('600x450')

textHolder= Text(root, font='Tahoma', fg='black', bg='powder blue')
file= None  #no file in the first stage
textHolder.pack(expand=True, fill=BOTH)

#ADDING FUNCTIONALITY TO THE EDIT DROP-DOWN MENU
def delete():
    root.destroy()

def copy():
    textHolder.event_generate('<<Copy>>')

def cut():
    textHolder.event_generate('<<Cut>>')

def paste():
    textHolder.event_generate('<<Paste>>')

#ADDING FUNCTIONALITY TO THE FILE DROP-DOWN MENU
def creat_New():
    global file
    root.title('Untitled   - Notepad') #the title 
    file= None     #no file unless you save
    textHolder.delete(1.0,END)  #delete whatever the fuck you wrote

def file_open():
    global file
    file= fd.askopenfilename(defaultextension='.txt', filetype=[('All file types', '*.*'),('Text Files', '*.txt')])

    #if the file you're trying to open doesn't exist/
    #if you're seleting nothing in the file system
    if file==' ':
        file= None
    else:
        #setting the title of the frame to the thing that you've opened(yk what i'm saying)
        root.title(os.path.basename(file)+'- Notepad')
        #remove the existing text from previous 
        textHolder.delete(1.0,END)
        #opening file as read mode
        f=open(file, 'r')
        textHolder.insert(1.0,f.read())
        

def saveFilee():
    global file
    #checks if the file is complete new(like in untitled state)
    if file==None:
        #the default will be in untitled.txt in its initial stage before we name it
        file= fd.askopenfilename(initialfile='Untitled.txt',defaultextension='.txt', filetype=[('All file types', '*.*'),('Text Files', '*.txt')]) #filetype ka save as type 

        #if we don't give a name to the new file
        if file==' ':
            file=None
        #if we give a name to the new file it will save in that name
        #literally the new file that you've recently given a name to
        else:
            f=open(file,'w')
            f.write(textHolder.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+'- Notepad')

    #if the file is created and saved prior it saves in that name
    else:
        f=open(file,'w')
        f.write(textHolder.get(1.0, END))
        f.close()

def close():
    root.destroy()

def undo():
    pass

def about():
    showinfo('FYI','This is the shittiest notepad I\'ve created from scratch')

#create a fucking menubar
menubar= Menu(root)
#menubar being the master, include tearoff or else you will see ticket_like lines
file_menu=Menu(menubar,tearoff=0)
#add_command adds menu items
'''New Open Save Save as Close || Exit'''
file_menu.add_command(label='New', command=creat_New)
file_menu.add_command(label='Open', command=file_open)
file_menu.add_command(label='Save', command=saveFilee)
file_menu.add_command(label='Save as...', command=saveFilee)
file_menu.add_command(label='Close', command=close)
#like a separate line within the menu
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
#file under menubar 
#file_menu under menu
menubar.add_cascade(label='File', menu=file_menu)

edit_menu=Menu(menubar, tearoff=0)
edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Paste', command=paste)
edit_menu.add_command(label='Delete', command=delete)
edit_menu.add_separator()
edit_menu.add_command(label='Undo', command=undo)
menubar.add_cascade(label='Edit', menu=edit_menu)

about_menu=Menu(menubar,tearoff=0)
about_menu.add_command(label='INfo', command=about)
menubar.add_cascade(label='About', menu=about_menu)

root.config(menu=menubar)
#ADDING SCROLLBAR TO THE TEXT AREA
#initializing the scroll widget
Scroll = Scrollbar(textHolder)
#where you want the scroll to appear
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=textHolder.yview)
textHolder.config(yscrollcommand=Scroll.set)
root.mainloop()
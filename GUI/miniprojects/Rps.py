from tkinter import*
from random import randint
root= Tk()
root.title('Rock Paper Scissors')
root.geometry('450x600')
root.config(bg='white')


#insert pics 
rock= PhotoImage(file='C:\\Users\\LENOVO\\Desktop\\VS\\Python\\GUI shit\\miniprojects\\Rps\\rock.png')
paper=PhotoImage(file='C:\\Users\\LENOVO\\Desktop\\VS\\Python\\GUI shit\\miniprojects\\Rps\\paper.png')
scissors=PhotoImage(file='C:\\Users\\LENOVO\\Desktop\\VS\\Python\\GUI shit\\miniprojects\\Rps\\scissors.png')

img_list=[rock, paper, scissors]
'''
Rock==0
paper==1
scissors=2
'''
#randint==> picks random int in this case from 0 to 2
random_num= randint(0,2)
img_label= Label(root, image=img_list[random_num])
img_label.pack(pady=40)

spin_button= Button(root, )
root.mainloop()

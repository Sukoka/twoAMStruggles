from tkinter import*
root= Tk()  #the window
root.title('Scary Calculator')  #the title
root.configure(bg='powder blue')    #the background i guess

#can make the default size using geology but nah
expression=' '
data= StringVar() #StringVar is used to store string values #default value=' ' 

#root ka parent
'''
bg : The normal background color displayed behind the label and indicator. 
bd : The size of the border around the indicator. Default is 2 pixels. 
font : The font used for the text. 
fg : Text colour 
justify : If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT. 
relief : With the default value, relief=FLAT. You may set this option to any of the other styles like : SUNKEN, RIGID, RAISED, GROOVE 
show : Normally, the characters that the user types appear in the entry. To make a .password. entry that echoes each character as an asterisk, set show=”*”. 
textvariable : In order to be able to retrieve the current text from your entry widget, you must set this option to an instance of the StringVar class.'''
e=Entry(root, width=37, borderwidth=5, textvariable=data)   #Entry box #where the inputs and result will be shown
e.grid(row=0, column=0, columnspan=4, padx=5,pady=10)

def onclick(n): #takes the numbers and the operator signs
    #declare it global to change
    global expression      
    expression= expression+ str(n)
    data.set(expression)    #refer line 8
    
def equalOnClick():     #you show the fucking result by clicking equal
    try:
        global expression
        #eval() takes string as python expression and returns an int
        #eval('1')= 1
        total= str(eval(expression))    
        data.set(total)
        #reset it to empty so that the ex-data gets erased
        expression= ' ' 
    except:
        #it's got to have an except block i guess
        data.set('Error')
        data.set(' ')
  
def clearOnClick():
    global expression
    expression= ' ' 
    data.set(' ')


butt_1=Button(root, text='1', padx=40, pady=20, command=lambda: onclick(1))
butt_1.grid(row=4, column=0)
butt_2=Button(root, text='2', padx=40, pady=20, command=lambda: onclick(2))
butt_2.grid(row=4, column=1)
butt_3=Button(root, text='3', padx=40, pady=20, command=lambda: onclick(3))
butt_3.grid(row=4, column=2)
butt_4=Button(root, text='4', padx=40, pady=20, command=lambda: onclick(4))
butt_4.grid(row=3, column=0)
butt_5=Button(root, text='5', padx=40, pady=20, command=lambda: onclick(5))
butt_5.grid(row=3, column=1)
butt_6=Button(root, text='6', padx=40, pady=20, command=lambda: onclick(6))
butt_6.grid(row=3, column=2)
butt_7=Button(root, text='7', padx=40, pady=20, command=lambda: onclick(7))
butt_7.grid(row=2, column=0)
butt_8=Button(root, text='8', padx=40, pady=20, command=lambda: onclick(8))
butt_8.grid(row=2, column=1)
butt_9=Button(root, text='9', padx=40, pady=20, command=lambda: onclick(9))
butt_9.grid(row=2, column=2)
butt_0=Button(root, text='0', padx=88, pady=20, command=lambda: onclick(0))
butt_0.grid(row=5, column=0, columnspan=2)

butt_add=Button(root, text='+', padx=39, pady=20, command=lambda: onclick('+'))
butt_add.grid(row=1, column=0)
butt_sub=Button(root, text='-', padx=40, pady=20, command=lambda: onclick('-'))
butt_sub.grid(row=1, column=1)
butt_mul=Button(root, text='*', padx=40, pady=20, command=lambda: onclick('*'))
butt_mul.grid(row=1, column=2)
butt_div=Button(root, text='/', padx=40, pady=20, command=lambda:onclick('/'))
butt_div.grid(row=1, column=3)
butt_perc=Button(root, text='%', padx=39, pady=50, command=lambda: onclick('%'))
butt_perc.grid(row=2, column=3, rowspan=2)


butt_equal=Button(root, text='=', padx=39, pady=52, command=equalOnClick)
butt_equal.grid(row=4, column=3, rowspan=2)
butt_clear=Button(root, text='Clear', padx=30, pady=20, command=clearOnClick)
butt_clear.grid(row=5, column=2)



root.mainloop()

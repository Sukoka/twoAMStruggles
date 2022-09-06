#stupid calculator 2.0
from tkinter import*
root=Tk()
root.title('The frame thing')
frame= LabelFrame(root, text='Hey Does it work?', padx=100, pady=100)      #padding inside the frame
frame.pack(padx=100, pady=100)  #outside the frame

word= Button(frame, text='Hip', pady=30, padx=30)
word.pack()


root.mainloop()

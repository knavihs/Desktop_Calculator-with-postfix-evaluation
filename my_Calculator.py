from tkinter import *
from tkinter.messagebox import *
from collections import deque
import math as m
font = ('Verdana',22)

#IMP_funtions
def clearone(event):
    ex= textfeild.get()
    ex=ex[0:len(ex)-1]
    textfeild.delete(0,END)
    textfeild.insert(0,ex)

def click_btn_funtion(event):
    print('button clicked')
    b=event.widget
    text=b['text']
    print(text)
    if text=='x':
        textfeild.insert(END,'*')
        return
    if text=='reset':
        textfeild.delete(0,END)
        return
    if text=='=':
        try:
            ex=textfeild.get()
            answer=eval(ex)
            textfeild.delete(0,END)
            textfeild.insert(0,answer)
            return
        except Exception as e:
            print('Error: ',e)
            showerror('ERROR: ',e)

    textfeild.insert(END,text)

#creating window

window = Tk()
window.title('MY CALCULATOR')
window.geometry('450x630')

pic=PhotoImage(file='img/cal.png')
picturelabel=Label(window,image = pic)
picturelabel.pack(side =TOP,pady=10)

#heading label
heading=Label(window,text='Calculator',font = font)
heading.pack(side=TOP,pady=10)

#TEXTFEILD
textfeild = Entry(window,font =font, justify=CENTER)
textfeild.pack(side=TOP,pady=10,fill=X,padx=5)

#button

button=Frame(window)
button.pack(side=TOP)
#Adding Buttons in the frame
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(button,text= str(temp),font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
        btn.grid(row=i,column=j,padx=2,pady=2)
        temp=temp+1
        btn.bind('<Button-1>',click_btn_funtion)

#Adding DOT, ZERO and '=' ,'+','-','x','/' button
dotbtn=Button(button,text= '.',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
dotbtn.grid(row=3,column=0,padx=2,pady=2)
zerobtn=Button(button,text= '0',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
zerobtn.grid(row=3,column=1,padx=2,pady=2)
equaltobtn=Button(button,text= '=',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
equaltobtn.grid(row=3,column=2,padx=2,pady=2)
plusbtn=Button(button,text= '+',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
plusbtn.grid(row=0,column=3,padx=2,pady=2)
minusbtn=Button(button,text= '-',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
minusbtn.grid(row=1,column=3,padx=2,pady=2)
multbtn=Button(button,text= 'x',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
multbtn.grid(row=2,column=3,padx=2,pady=2)
divbtn=Button(button,text= '/',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
divbtn.grid(row=3,column=3,padx=2,pady=2)

clearbtn=Button(button,text= 'clear',font=font,width=11,relief='ridge',activebackground='orange',activeforeground='white')
clearbtn.grid(row=4,column=0,padx=2,pady=2,columnspan=2)

resetbtn=Button(button,text= 'reset',font=font,width=11,relief='ridge',activebackground='orange',activeforeground='white')
resetbtn.grid(row=4,column=2,padx=2,pady=2,columnspan=2)

#binding all buttons
dotbtn.bind('<Button-1>',click_btn_funtion)
zerobtn.bind('<Button-1>',click_btn_funtion)
equaltobtn.bind('<Button-1>',click_btn_funtion)
plusbtn.bind('<Button-1>',click_btn_funtion)
minusbtn.bind('<Button-1>',click_btn_funtion)
multbtn.bind('<Button-1>',click_btn_funtion)
divbtn.bind('<Button-1>',click_btn_funtion)
resetbtn.bind('<Button-1>',click_btn_funtion)
clearbtn.bind('<Button-1>',clearone)

###########################################################################################
#   MENU BAR for Scientific cal calculator
###########################################################################################
font2=("arial",12,'bold')
# Function for scientific calculator
def sc_cal(event):
    try:
        temp=event.widget
        text=temp['text']
        print(text)
        ex= textfeild.get()
        if text=='√':
            answer=str(m.sqrt(float(ex)))
        elif text=='exp':
            answer=str(m.exp(float(ex)))
        elif text=='X!':
            answer=str(m.factorial(int(ex)))
        elif text=='toRAD':
            answer=str(m.radians(float(ex)))
        elif text=='toDEG':
            answer=str(m.degrees(float(ex)))
        elif text=='SIN':
            answer=str(m.sin(m.radians(float(ex))))
        elif text=='COS':
            answer=str(m.cos(m.radians(float(ex))))
        elif text=='TAN':
            answer=str(m.sin(m.radians(float(ex))))

        textfeild.delete(0,END)
        textfeild.insert(0,answer)
    except Exception as e:
        showerror('ERROR',e)



scFrame=Frame(window)
Sqrtbtn=Button(scFrame,text= '√',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
Sqrtbtn.grid(row=0,column=0,padx=2,pady=2)
expbtn=Button(scFrame,text= 'exp',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
expbtn.grid(row=0,column=1,padx=2,pady=2)
factbtn=Button(scFrame,text= 'X!',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
factbtn.grid(row=0,column=2,padx=2,pady=2)
toradbtn=Button(scFrame,text= 'toRAD',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
toradbtn.grid(row=0,column=3,padx=2,pady=2)

todegbtn=Button(scFrame,text= 'toDEG',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
todegbtn.grid(row=1,column=0,padx=2,pady=2)
sinntm=Button(scFrame,text= 'SIN',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
sinntm.grid(row=1,column=1,padx=2,pady=2)
cosbtn=Button(scFrame,text= 'COS',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
cosbtn.grid(row=1,column=2,padx=2,pady=2)
tanbtn=Button(scFrame,text= 'TAN',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
tanbtn.grid(row=1,column=3,padx=2,pady=2)

normalcal = True
def sc_click():
    global normalcal
    print('clicked')
    if normalcal:
        print("show sc")
        button.pack_forget()
        scFrame.pack(side=TOP,pady=10)
        button.pack(side=TOP)
        window.geometry('450x770')
        normalcal=False
    else:
        print("show normal")
        scFrame.pack_forget()
        window.geometry('450x630')
        normalcal=True

Sqrtbtn.bind('<Button-1>',sc_cal)
expbtn.bind('<Button-1>',sc_cal)
factbtn.bind('<Button-1>',sc_cal)
toradbtn.bind('<Button-1>',sc_cal)
todegbtn.bind('<Button-1>',sc_cal)
sinntm.bind('<Button-1>',sc_cal)
cosbtn.bind('<Button-1>',sc_cal)
tanbtn.bind('<Button-1>',sc_cal)
###########################################################################################
##  POSTFIX EVALUATION ##
####################################################
#Funtions for buttons action
def click_btn_funtion_PE(event):
    print('button clicked')
    b=event.widget
    text=b['text']
    print(text)
    if text=='x':
        textfeild.insert(END,'*')
        return
    if text=='reset':
        textfeild.delete(0,END)
        return
    textfeild.insert(END,text)

def post_eval(event):
    try:

        print('button clicked')
        b=event.widget
        text=b['text']
        print(text)
        ex= textfeild.get()
        if text == "=":
            q = deque()
            for i in ex:
                if i.isdigit():
                    q.append(i)

                else:
                    b = q.pop()
                    a = q.pop()
                    q.append(str(eval(a + i + b)))
        result = q.__getitem__(0)
        textfeild.delete(0, END)
        textfeild.insert(0, result)
    except Exception as e:
        showerror("ERROR",e)
normalcal=True
def pe_click():
    global normalcal
    if normalcal:
        button.pack_forget()
        buttonFrame.pack(side=TOP)
        normalcal=False
    else :
        buttonFrame.pack_forget()
        button.pack(side=TOP)
        normalcal=True




buttonFrame=Frame(window)
#Adding Buttons in the frame
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn11=Button(buttonFrame,text= str(temp),font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
        btn11.grid(row=i,column=j,padx=2,pady=2)
        temp=temp+1
        btn11.bind('<Button-1>',click_btn_funtion_PE)

#Adding DOT, ZERO and '=' ,'+','-','x','/' button
dotbtn1=Button(buttonFrame,text= '.',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
dotbtn1.grid(row=3,column=0,padx=2,pady=2)
zerobtn1=Button(buttonFrame,text= '0',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
zerobtn1.grid(row=3,column=1,padx=2,pady=2)
equaltobtn1=Button(buttonFrame,text= '=',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
equaltobtn1.grid(row=3,column=2,padx=2,pady=2)
plusbtn1=Button(buttonFrame,text= '+',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
plusbtn1.grid(row=0,column=3,padx=2,pady=2)
minusbtn1=Button(buttonFrame,text= '-',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
minusbtn1.grid(row=1,column=3,padx=2,pady=2)
multbtn1=Button(buttonFrame,text= 'x',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
multbtn1.grid(row=2,column=3,padx=2,pady=2)
divbtn1=Button(buttonFrame,text= '/',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
divbtn1.grid(row=3,column=3,padx=2,pady=2)

clearbtn1=Button(buttonFrame,text= 'clear',font=font,width=11,relief='ridge',activebackground='orange',activeforeground='white')
clearbtn1.grid(row=4,column=0,padx=2,pady=2,columnspan=2)

resetbtn1=Button(buttonFrame,text= 'reset',font=font,width=11,relief='ridge',activebackground='orange',activeforeground='white')
resetbtn1.grid(row=4,column=2,padx=2,pady=2,columnspan=2)
## BINDING ALL BUTTONS
dotbtn1.bind('<Button-1>',click_btn_funtion_PE)
zerobtn1.bind('<Button-1>',click_btn_funtion_PE)
equaltobtn1.bind('<Button-1>',post_eval)
plusbtn1.bind('<Button-1>',click_btn_funtion_PE)
minusbtn1.bind('<Button-1>',click_btn_funtion_PE)
multbtn1.bind('<Button-1>',click_btn_funtion_PE)
divbtn1.bind('<Button-1>',click_btn_funtion_PE)
resetbtn1.bind('<Button-1>',click_btn_funtion_PE)
clearbtn1.bind('<Button-1>',clearone)




menubar=Menu(window)
mode = Menu(menubar,font=font2,tearoff=0)
mode.add_checkbutton(label="Scientific Calculator",command=sc_click)

mode.add_checkbutton(label='Postfix_evaluation',command=pe_click)
menubar.add_cascade(label="Mode",menu=mode)
window.config(menu=menubar)




window.mainloop()
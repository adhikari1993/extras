import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import END
import turtle
from turtle import *
import time


outfile=open('guiatm_receipt.txt','w')# opening file 
class ATMGUI:#cretaes ATM class
    
    def __init__(self):#method for initialization
        self.pin_number=0
        self.outfile=outfile
        self.balance=0
        self.balance_new=0
        self.old_pin_number=1234
        self.main_window=tk.Tk()
        self.canvas= tk.Canvas(self.main_window, width=800, height=800, bg='blue') #defining canvas of width 800 and height 800 with blue background
        self.logo=tk.PhotoImage(file="atm.gif")
        self.canvas.create_image(0, 0, image=self.logo, anchor= 'nw')  # adding image in canvas
        self.explain="""WELCOME TO PRASHANT'S ATM"""
        self.outfile.write('...................'+self.explain+'.....................')#writing in file
        self.outfile.write('\n')
        self.outfile.write('\n')
        self.canvas.create_text(780, 200, anchor= 'se', text=self.explain, font=("times", 15),fill='yellow')
        self.canvas.pack() # packing canvas
        self.part1() #calling part1() function
        tk.mainloop()
      
    def part1(self):
        self.prompt_label= tk.Label(self.canvas, text='Enter PIN:',font=("times",12), fg='black', bg='blue') # label to enter pin
        self.pin_entry=tk.Entry(self.canvas, width=20) # text box for pin entry
        
        self.prompt_label.pack(side='left')
        self.pin_entry.pack(side='left')
        self.canvas.create_window(50,550,window=self.prompt_label)# adjusting the position of label in canvas
        self.canvas.create_window(300,550,window=self.pin_entry) # adjusting the position of text box in canvas
        
        self.submit_button=tk.Button(self.canvas, text='SUBMIT',font=("times",12), fg='black', bg='light gray', command=self.submit) # submit button after entering pin
        self.quit_button=tk.Button(self.canvas,text='QUIT', font=("times",12), fg='black', bg='red',command=self.mainwindow) # quit button to exit the program
        
        self.submit_button.pack(side='left')
        self.quit_button.pack(side='bottom')
        
        self.canvas.create_window(500,550,window=self.submit_button)
        self.canvas.create_window(750,750,window=self.quit_button)
       
    def mainwindow(self):
        self.outfile.write('YOUR BALANCE IS------------->$')
        self.outfile.write(str(float(self.balance)))
        self.outfile.write('\n') 
        self.outfile.write('\n')
        self.outfile.write('..............THANK YOU FOR VISITING PRASHANTs ATM.................')
      
        self.outfile.close()# closing file
        self.turtle_canvas=tk.Canvas(self.canvas, width=800, height=230)
        self.turtle_canvas.pack()
        self.canvas.create_window(400,600,window=self.turtle_canvas)
        self.t=turtle.RawTurtle(self.turtle_canvas) # deifining object for RawTurtle to incorporate animation for good bye

        self.t.speed(10) # setting the speed of pen
        self.t.shape('turtle')   #choosing the shape of pen nib
        for i in range(5):
         
             self.t.forward(100)
             self.t.right(144)
             
        self.t.fillcolor('black') #defining fill color for circle
        self.t.begin_fill()
        self.t.circle(10) # circle of radius 10 is drawn
        self.t.end_fill() # cicrel is filled with black color
        
        self.t.setpos(100, 0) 
        self.t.fillcolor('black')
        self.t.begin_fill()
        self.t.circle(10)
        self.t.end_fill()
        self.t.penup()
        
        self.t.setpos(50,36)
        self.t.pendown()
        self.t.fillcolor('black')
        self.t.begin_fill()
        self.t.circle(10)
        self.t.end_fill()
        
    
        self.t.penup()
        self.t.setpos(-220,-90) 
        self.t.pendown()
        self.t.pencolor('black')
        self.t.write('THANK YOU FOR CHOOSING BANK OF PRASHANT', font=("Times New Roman", 16, "italic", "bold")) # displaying text using turtle
        self.t.penup()
        self.t.hideturtle() # hiding turtle
     
        time.sleep(2)#delay of 2 sec
        self.main_window.destroy() #destroying main window
        
    def submit(self):
        flag1=0
        while flag1!=1:#while loop to check if the pin number is integer or  not
            try:
                self.pin_number=int(self.pin_entry.get()) #assign keyboard input to pin_number
                              
            except ValueError:                                                                          
                self.pin_entry.delete(0,END) 
                flag1=1
                
            else:
                break
         
           
        if self.pin_number== self.old_pin_number:
               self.part2()

        else:
               messagebox.showinfo("INVALID PIN!",'INVALID PIN') # pop up message
               self.pin_entry.delete(0,END) 
           
    def part2(self):     
           self.amount_label= tk.Label(self.canvas, text='Amount Deposited:',font=("times",12), fg='black', bg='blue') # defining label to enter amount 
           self.amount_entry=tk.Entry(self.canvas, width=20) # defining text box entry for amount 
           self.amount_label.pack(side='left')
           self.amount_entry.pack(side='left')
           self.canvas.create_window(70,550,window=self.amount_label)
           self.canvas.create_window(300,550,window=self.amount_entry)
           self.deposit_button=tk.Button(self.canvas, text='SUBMIT',font=("times",12), fg='black', bg='light gray', command=self.Deposit)  # defining submit button for deposit 
           self.deposit_button.pack(side='left')
           self.canvas.create_window(500,550,window=self.deposit_button)
           
           self.withdrawn_label= tk.Label(self.canvas, text='Amount Withdrawn:',font=("times",12), fg='black', bg='blue') # deinfing label to withdraw amount
           self.withdrawn_entry=tk.Entry(self.canvas, width=20) # defining text box for withdraw entry
           self.withdrawn_label.pack(side='left')
           self.withdrawn_entry.pack(side='left')
           self.canvas.create_window(70,600,window=self.withdrawn_label)
           self.canvas.create_window(300,600,window=self.withdrawn_entry)
           self.withdrawn_button=tk.Button(self.canvas, text='SUBMIT',font=("times",12), fg='black', bg='light gray', command=self.Withdraw) # defining submit button for withdraw
           self.withdrawn_button.pack(side='left')
           self.canvas.create_window(500,600,window=self.withdrawn_button)
           
           self.balance_label= tk.Label(self.canvas, text='Balance Amount:',font=("times",12), fg='black', bg='blue') # defining label for balance amount
           self.balance_entry=tk.Entry(self.canvas, width=20) # defining text box entry for displaying balance
           self.balance_label.pack(side='left')
           self.balance_entry.pack(side='left')
           self.canvas.create_window(60,650,window=self.balance_label)
           self.canvas.create_window(300,650,window=self.balance_entry) 
           self.Balance() # calling Balance() function
           
           self.changepin_button=tk.Button(self.canvas, text='Change Pin',font=("times",12), fg='black', bg='light gray', command=self.change_pin,height=1, width=7) # defining button for change pin
           self.changepin_button.pack(side='bottom')
           self.canvas.create_window(50,700,window=self.changepin_button)
           
           
       
    
    def Balance(self):
         
         self.balance_entry.insert(0,str(float(self.balance)))
         
    def Deposit(self): # method for deposit
        self.deposit=float(self.amount_entry.get())
        if self.deposit<=0:
            messagebox.showinfo('Invalid!!','Invalid deposit amount')
            self.deposit=0
            self.amount_entry.delete(0,END)
        else:
                self.balance_entry.delete(0,END)
                self.balance=float(self.balance+self.deposit)
                self.amount_entry.delete(0,END)
                self.balance_entry.insert(0,str(float(self.balance))) # updating balance
                self.outfile.write('YOUR DEPOSITED AMOUNT IS-------------->$')
                self.outfile.write(str(self.deposit))
                self.outfile.write('\n')
             
                
    def Withdraw(self): # method for withdraw
        self.withdraw=float(self.withdrawn_entry.get())
        if self.withdraw<=0:
            messagebox.showinfo('Invalid!!','Invalid Withdraw Amount')
            self.withdraw=0
            self.withdrawn_entry.delete(0,END)
       
        elif float(self.balance)<self.withdraw:
            messagebox.showinfo('Invalid!!','Invalid withdraw amount')
            self.withdraw=0
            self.withdrawn_entry.delete(0,END)
            
        else:
            self.balance_entry.delete(0,END)
            self.balance=float(self.balance-self.withdraw)
            self.withdrawn_entry.delete(0,END)
            self.balance_entry.insert(0,str(float(self.balance))) #updating balance
            self.outfile.write('YOUR WITHDRAWN AMOUNT IS-------------->$')
            self.outfile.write(str(self.withdraw))
            self.outfile.write('\n')
            
    def change_pin(self): # method for change pin
        self.balance_entry.destroy() # destroying balance text box
        self.balance_label.destroy()
        self.withdrawn_label.destroy()
        self.withdrawn_entry.destroy()
        self.withdrawn_button.destroy()
        self.amount_entry.destroy()
        self.amount_label.destroy()
        self.prompt_label.destroy()  # destroying label for pin entry
        self.pin_entry.destroy()
        self.submit_button.destroy()
        self.changepin_button.destroy()  # destroying change pin button
                
        self.newpin_label= tk.Label(self.canvas, text='Enter your new pin:',font=("times",12), fg='black', bg='blue')
        self.newpin_entry=tk.Entry(self.canvas, width=20)
        self.newpin_label.pack(side='left')
        self.newpin_entry.pack(side='left')
        self.canvas.create_window(70,550,window=self.newpin_label)
        self.canvas.create_window(300,550,window=self.newpin_entry)
        self.newpinsubmit_button=tk.Button(self.canvas, text='SUBMIT',font=("times",12), fg='black', bg='light gray', command=self.newpin)
        self.newpinsubmit_button.pack(side='left')
        self.canvas.create_window(500,550,window=self.newpinsubmit_button)
        
        self.back_button=tk.Button(self.canvas, text='Back',font=("times",12), fg='black', bg='light gray', command=self.back, height=1, width=7)
        self.back_button.pack(side='bottom')
        self.canvas.create_window(50,700,window=self.back_button)
    
    
     
    def newpin(self): # method for setting new pin
        self.temp_pin=0
        flag2=0
        count=0
        while flag2!=1:   
                try:
                    self.temp_pin=int(self.newpin_entry.get())
                   
                except  ValueError:
                    messagebox.showinfo('Inavlid!!','Invalid Pin Setup')
                    self.newpin_entry.delete(0,END) # deleting the text in text box entry
                    self.newpin_entry.destroy()
                    self.newpin_label.destroy()
                    flag2=1
                    self.change_pin()
                else:
                    break
                    
        
        self.temp_pin=int(self.newpin_entry.get())
        while int(self.temp_pin)>0:
                count=count+1
                self.temp_pin=self.temp_pin/10
        if count==4:
                
                self.old_pin_number=int(self.newpin_entry.get())
                messagebox.showinfo('SUCCESS!!!','Your Pin has been Changed')
                self.back_button.destroy()
                self.newpin_label.destroy()
                self.newpin_entry.destroy()
                self.flag2=1
                self.outfile.write('YOUR PIN HAS BEEN CHANGED')
                self.outfile.write('\n')
                self.part1()
        else:
                 messagebox.showinfo('Invalid','Invalid Pin Setup')
                 self.newpin_entry.delete(0,END) 
                 self.newpin_entry.destroy()
                 self.newpin_label.destroy()
                 
                 flag2=1
                 self.change_pin()
            
            
    def back(self):# method for back
        self.back_button.destroy()
        self.newpin_label.destroy()
        self.newpin_entry.destroy()
        self.part2() # part2() function call
        
    
        
    
my_gui=ATMGUI()# making object my_gui for ATMGUI() class

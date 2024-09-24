from distutils.util import change_root
from io import text_encoding
import tkinter as tk
from customtkinter import *

set_appearance_mode('dark')
mode = 'dark'

def double_letter_numbers(numerical_input):
    answer = 0
    if "CM" in numerical_input:
        answer += 900
        numerical_input = numerical_input.replace("CM", "")
    if "CD" in numerical_input:
        answer += 400
        numerical_input = numerical_input.replace("CD", "")
    if "XC" in numerical_input:
        answer += 90
        numerical_input = numerical_input.replace("XC", "")
    if "XL" in numerical_input:
        answer += 40
        numerical_input = numerical_input.replace("XL", "")
    if "IX" in numerical_input:
        answer += 9
        numerical_input = numerical_input.replace("IX", "")
    if "IV" in numerical_input:
        answer += 4
        numerical_input = numerical_input.replace("IV", "")
        
    return numerical_input, answer

def roman_to_int(numerical_input):
    
    numerical_input, answer = double_letter_numbers(numerical_input)
    
    for i in numerical_input:
        
        match i:
            case 'M':
                answer += 1000
            case 'D':
                answer += 500
            case 'C':
                answer += 100
            case 'L':
                answer += 50
            case 'X':
                answer += 10
            case 'V':
                answer += 5
            case 'I':
                answer += 1
            case _: 
                answer = 0
                # print('The was a letter that is not a roman number')
                break
            
    return answer

def center_window(window, width = 440, height = 200):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' %(width, height, x, y))

class App():
    def __init__(self):
        self.root = CTk()
        center_window(self.root)
        self.root.title('Converting Roman Numbers into Arabic numbers')
        
        self.root.iconbitmap('icons/coin.ico')
        self.frame = CTkFrame(self.root)
        self.frame.pack(pady = 0, padx = 0, expand = True, fill = 'both')
          
        # roman number
        self.romanlabel = CTkLabel(self.frame, text= 'Roman number', font=('calibri', 18))
        self.romanlabel.place(relx = 0.1, rely = 0.2)  
        self.romannumber = CTkEntry(self.frame, placeholder_text= "Enter roman number", font=('calibri', 14))
        self.romannumber.place(relx = 0.43, rely = 0.2)
        
        # arabic number
        self.arabiclabel = CTkLabel(self.frame, text = 'Arabic number', font=('calibri', 18))
        self.arabiclabel.place(relx=0.1, rely = 0.4)
        self.arabicnumber = CTkLabel(self.frame, text = '', font=('calibri', 16))
        self.arabicnumber.place(relx=0.43, rely = 0.4)
        

        # switch for appearance mode
        self.switch = CTkSwitch(self.frame, text = 'Mode', font = ('calibri', 13), command = self.switch_event)
        self.switch.place(relx = 0.8, rely = 0.05)
        
        # button
        self.button = CTkButton(self.frame, text = 'Submit', command = self.click_handler,
                           font=("calibri", 16), corner_radius = 9, fg_color='#3E78B2', 
                           hover_color= '#4A525A', text_color='#000000')
        self.button.place(relx = 0.33, rely = 0.7)
        
        self.root.mainloop()
        return
    
    def change_button_color(self):
        if mode == 'dark':
            self.button.configure(fg_color='#004BA8', hover_color= '#24272B', text_color='#E3FFE0')
        else:
            self.button.configure(fg_color='#3E78B2', hover_color= '#4A525A', text_color='#000000')
            
    def switch_event(self):
        global mode
        if mode == 'dark':
            set_appearance_mode('light')
            self.change_button_color()
            mode = 'light'
        else:
            set_appearance_mode('dark')
            self.change_button_color()
            mode = 'dark'
        
    def click_handler(self):
        newtext = roman_to_int(self.romannumber.get().upper())
        if newtext == 0:
            newtext = 'The input is incorrect.'
        self.arabicnumber.configure(text = newtext)
               

if __name__ == '__main__':
    App()




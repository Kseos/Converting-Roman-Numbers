from ast import Lambda
from customtkinter import *
from converting_numbers import roman_to_int

set_appearance_mode('dark')
mode = 'dark'

class App():
    def __init__(self):
        self.root = CTk()
        self.center_window(self.root)
        self.root.title('Converting Roman Numbers into Arabic numbers')     
        self.root.iconbitmap('icons/coin.ico')
        self.frame = CTkFrame(self.root)
        self.frame.pack(pady = 0, padx = 0, expand = True, fill = 'both')
          
        self.roman_number()
        self.arabic_number()

        self.create_switch()
        self.create_button() 
        self.root.bind('<Return>', lambda event: self.click_handler())
             
        self.root.mainloop()
        return
    
    def roman_number(self):
        self.romanlabel = CTkLabel(self.frame, text= 'Roman number', font=('calibri', 18))
        self.romanlabel.place(relx = 0.1, rely = 0.2)  
        self.romannumber = CTkEntry(self.frame, placeholder_text= "Enter roman number", font=('calibri', 14))
        self.romannumber.place(relx = 0.43, rely = 0.2)
        
    def arabic_number(self):
        self.arabiclabel = CTkLabel(self.frame, text = 'Arabic number', font=('calibri', 18))
        self.arabiclabel.place(relx=0.1, rely = 0.4)
        self.arabicnumber = CTkLabel(self.frame, text = '', font=('calibri', 16))
        self.arabicnumber.place(relx=0.43, rely = 0.4)
        
    def create_switch(self):
        self.switch = CTkSwitch(self.frame, text = 'Mode', font = ('calibri', 13), command = self.switch_event)
        self.switch.place(relx = 0.8, rely = 0.05)
        
    def create_button(self):
        self.button = CTkButton(self.frame, text = 'Submit', command = self.click_handler,
                           font=("calibri", 16), corner_radius = 9, fg_color='#3E78B2', 
                           hover_color= '#4A525A', text_color='#000000')
        self.button.place(relx = 0.33, rely = 0.7)
    
    def center_window(self, window, width = 440, height = 200):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
    
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry('%dx%d+%d+%d' %(width, height, x, y))
    
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




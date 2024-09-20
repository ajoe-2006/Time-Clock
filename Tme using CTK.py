import customtkinter
from time import strftime

window=customtkinter.CTk()
window.title("Digital Clock")

def time():
    hours = strftime("%H")
    mins = strftime("%M")
    secs = strftime("%S")
    am_pm = strftime("%p")
    time_text = hours + ":" + mins + ":" + secs + ":" + am_pm
    di_clock_lbl.configure(text=time_text)
    di_clock_lbl.after(1000, time)

di_clock_lbl=customtkinter.CTkLabel(window,font=('ds-digital',40,'bold'),fg_color='purple',text_color='white')
di_clock_lbl.grid(padx=10,pady=10)

time()

window.mainloop()

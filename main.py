from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
#colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
#
FONT_NAME = "Courier"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg= YELLOW)

#Label
time_label = Label(text='Timer',fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
time_label.grid(column=1, row=0)

check_mark_label = Label(text='✔', fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


#Button
start_button = Button(text='Start', bg='white')
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg='white')
reset_button.grid(column=2, row=2)

window.mainloop()
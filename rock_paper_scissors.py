import random
from tkinter import PhotoImage, Tk
from tkinter.ttk import Label, Button, Style

win = Tk()
win.title('Game')
win.geometry('750x550')
win.config(background='black')

obj = {
    'r':'Rock',
    'p':'Paper',
    's':'Scissors'
}

user_score = 0
ai_score = 0

def scorebord(user_choice):
    global user_score, ai_score, obj
    ai_choice = random.choice(list(obj.keys()))
    lbl_status['text'] = f'You: {obj[user_choice]}\nAI: {obj[ai_choice]}'
    lbl_status.grid(row=1, column=4, pady=20)

    if (user_choice == 'r' and ai_choice == 's') or (user_choice == 's' and ai_choice == 'p') or (user_choice == 'p' and ai_choice == 'r'):
        user_score += 1
        lbl_win['text'] = f'Win : {user_score}'
        lbl_win.grid(row=1, column=2, pady=20)
        lbl_status['text'] = f'You : {obj[user_choice]}\nAI    : {obj[ai_choice]}\n* You Won *'
        lbl_status['foreground'] = 'light green'
        lbl_status.grid(row=1, column=4, pady=20)
    elif user_choice != ai_choice:
        ai_score += 1
        lbl_ai['text'] = f'AI : {ai_score}'
        lbl_ai.grid(row=1, column=7, pady=20)
        lbl_status['text'] = f'You : {obj[user_choice]}\nAI    : {obj[ai_choice]}\n* You Lost *'
        lbl_status['foreground'] = 'red'
        lbl_status.grid(row=1, column=4, pady=20)
    else:
        lbl_status['text'] = f'You : {obj[user_choice]}\nAI    : {obj[ai_choice]}\n* Draw *'
        lbl_status['foreground'] = 'white'
        lbl_status.grid(row=1, column=4, pady=20)


lbl_title = Label(
    master=win,
    text='Rock Paper Scissors',
    font=('Times new roman', 40),
    background='black',
    foreground='white',
)
lbl_title.grid(row=0, column=0, columnspan=10, pady=(3, 37))

lbl_win = Label(
    master=win,
    text='Win :',
    font=('Arial', 25),
    background='black',
    foreground='white',
)
lbl_win.grid(row=1, column=2, pady=20)

lbl_ai = Label(
    master=win,
    text='AI :',
    font=('Arial', 25),
    foreground='white',
    background='black',
)
lbl_ai.grid(row=1, column=7, pady=20)

lbl_status = Label(
    master=win,
    text='Status',
    font=('Times new roman', 25),
    foreground='red',
    background='black',
)
lbl_status.grid(row=1, column=4, pady=20)

style = Style()
style.theme_use('alt')
style.configure('TButton')
style.configure('TButton', width = 20, borderwidth=4, focusthickness=0, focuscolor='none',)
style.map('TButton', background=[('active','green')]) 

img_paper = PhotoImage(
    file='paper.jpg',
    height=215,
)
Button(master=win, image=img_paper, command=lambda: scorebord('p')).grid(row=4, column=0, rowspan=3, columnspan=3, padx=10)

img_rock = PhotoImage(
    file='rock.png',
)
Button(master=win, image=img_rock, command=lambda: scorebord('r')).grid(row=4, column=3, rowspan=3, columnspan=3, padx=10)

img_scissors = PhotoImage(
    file='scissors.png',
    height=215,
)
Button(master=win, image=img_scissors, command=lambda: scorebord('s')).grid(row=4, column=7, rowspan=3, columnspan=3, padx=10)



win.mainloop()

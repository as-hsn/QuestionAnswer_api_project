from tkinter import *
from quiz_brain import QuizBrain


FONT_NAME = "Georgia"
THEME_COLOR = "#375362"

class Interface:
    def __init__(self, data: QuizBrain):
        self.data = data
        self.window = Tk()
        self.icon_image = PhotoImage(file='images/hi.png')
        self.window.iconphoto(True, self.icon_image)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title('Quiz api project')
        self.score = self.label = Label(text=f'Score : {self.data.score}', bg=THEME_COLOR, fg='white', font=(FONT_NAME,
                                                                                                          17))
        self.label.grid(row=0, column=1)


        self.canvas = Canvas(height=250, width=300, bg='white', highlightthickness=0)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=40)
        self.text =  self.canvas.create_text(150, 125, text='Question text',width=300,
            fill='black', font=(FONT_NAME, 20, "italic"))

        self.right_image = PhotoImage(file='images/true.png')
        self.right_button = Button(image=self.right_image, border=0, highlightthickness=0, command=self.right)
        self.right_button.grid(row=5, column=0)

        self.wrong_image = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=self.wrong_image, border=0, highlightthickness=0, command=self.wrong)
        self.wrong_button.grid (row=5,
                                column=1)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.data.still_has_questions():
            self.canvas.config(bg='white')
            self.score.config (text=f'Score : {self.data.score}')
            self.q_text = self.data.next_question()
            self.canvas.itemconfig(self.text, text=self.q_text)
        else:
            self.canvas.itemconfig(self.text, text=f'You have reached the end')
            self.canvas.config (bg='white')
            self.right_button.config(state='disabled')
            self.wrong_button.config (state='disabled')


    def right(self):
        true = self.data.check_answer('True')
        self.reset(true)

    def wrong(self):
        false = self.data.check_answer('False')
        self.reset (false)

    def reset(self, right):

        if right:
            self.colour = self.canvas.config(bg='green')

        else:
            self.colour = self.canvas.config (bg='red')

        self.window.after(1000, self.next_question)




    #     self.window.after (1000, self.canvas.itemconfig (self.text,
    #     text=self.data.next_question), self.canvas.config (bg='white'))
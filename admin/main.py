from tkinter import *
from tkinter import ttk

from admin.db_manager import DBManager as dbm

root = Tk()
root.geometry("600x450")
root.resizable(height=False, width=False)
font = ("Arial", 12)
# question forms
qFrame = Frame(root).place(x=10, y=10, width=580, height=150)
ttk.Label(qFrame, text="Текст запитання", font=font).place(x=240, y=10)
qText = Text(qFrame, font=("Arial", 10), height=3)
qText.place(x=50, y=40, width=500)

ttk.Label(qFrame, text="Категорія", font=font).place(x=50, y=110)
qRank = ttk.Entry(qFrame)
qRank.place(x=150, y=110, width=50)

# question type
qType = IntVar()
qType.set(1)

answerFrame = Frame(root, bd=0)

answerFrame.place(x=10, y=170, width=580, height=210)

# simple answer
simpleAnswerFrame = Frame(answerFrame)
simpleAnswerFrame.place(x=10, y=40, width=540, height=160)
an_1 = BooleanVar()
an_2 = BooleanVar()
an_3 = BooleanVar()
an_4 = BooleanVar()

al_1 = Label(answerFrame, text="A:", font=font)
al_1.place(x=40, y=50)
al_2 = Label(answerFrame, text="B:", font=font)
al_2.place(x=40, y=90)
al_3 = Label(answerFrame, text="C:", font=font)
al_3.place(x=40, y=130)
al_4 = Label(answerFrame, text="D:", font=font)
al_4.place(x=40, y=170)

sal_1 = Text(answerFrame, height=1)
sal_1.place(x=70, y=50, width=200, height=25)
sal_2 = Text(answerFrame, height=1, width=30)
sal_2.place(x=70, y=90, width=200, height=25)
sal_3 = Text(answerFrame, height=1, width=30)
sal_3.place(x=70, y=130, width=200, height=25)
sal_4 = Text(answerFrame, height=1, width=30)
sal_4.place(x=70, y=170, width=200, height=25)

sacb_1 = Checkbutton(simpleAnswerFrame,
                     text="Правильна відповідь",
                     variable=an_1,
                     font=font
                     )
sacb_1.place(x=320, y=10)
sacb_2 = Checkbutton(simpleAnswerFrame,
                     text="Правильна відповідь",
                     variable=an_2,
                     font=font
                     )
sacb_2.place(x=320, y=50)
sacb_3 = Checkbutton(simpleAnswerFrame,
                     text="Правильна відповідь",
                     variable=an_3,
                     font=font
                     )
sacb_3.place(x=320, y=90)
sacb_4 = Checkbutton(simpleAnswerFrame,
                     text="Правильна відповідь",
                     variable=an_4,
                     font=font
                     )
sacb_4.place(x=320, y=130)
answersLabel = Label(answerFrame, text="Варіанти відповідей", font=font).place(x=230, y=10)
answerFrame.config(highlightbackground="white", highlightcolor="white", highlightthickness=2)

# confirmLabel = Label(root, text="Додано нове запитання", font=("Arial", 12), fg="green")


def add_question():
    question_text = qText.get('1.0', END)[:-1]
    question_rank = int(qRank.get())
    question_type = int(qType.get())
    question_id = dbm.add_question(q_text=question_text,
                                   q_rank=question_rank,
                                   q_type=question_type)

    answer_1_text = str(sal_1.get('1.0', END))[:-1]
    answer_2_text = sal_2.get('1.0', END)[:-1]
    answer_3_text = sal_3.get('1.0', END)[:-1]
    answer_4_text = sal_4.get('1.0', END)[:-1]

    if question_type == 1:
        answer_1_status = an_1.get()
        answer_2_status = an_2.get()
        answer_3_status = an_3.get()
        answer_4_status = an_4.get()
        dbm.add_answer(a_text=answer_1_text,
                       a_is_correct=answer_1_status,
                       question_id=question_id)
        dbm.add_answer(a_text=answer_2_text,
                       a_is_correct=answer_2_status,
                       question_id=question_id)
        dbm.add_answer(a_text=answer_3_text,
                       a_is_correct=answer_3_status,
                       question_id=question_id)
        dbm.add_answer(a_text=answer_4_text,
                       a_is_correct=answer_4_status,
                       question_id=question_id)
    if question_type == 2:
        dbm.add_positional_answer(a_text=answer_1_text,
                                  a_rank=1,
                                  question_id=question_id)
        dbm.add_positional_answer(a_text=answer_2_text,
                                  a_rank=2,
                                  question_id=question_id)
        dbm.add_positional_answer(a_text=answer_3_text,
                                  a_rank=3,
                                  question_id=question_id)
        dbm.add_positional_answer(a_text=answer_4_text,
                                  a_rank=4,
                                  question_id=question_id)
    # confirmLabel.place(x=50, y=400)


confirmButton = Button(root, text="Додати запитання", font=font, command=add_question)
confirmButton.place(x=230, y=400)


def get_answers_form():
    if qType.get() == 1:
        simpleAnswerFrame.place(x=10, y=40, width=540, height=160)
        al_1['text'] = 'A:'
        al_2['text'] = 'B:'
        al_3['text'] = 'C:'
        al_4['text'] = 'D:'
    if qType.get() == 2:
        simpleAnswerFrame.place_forget()
        al_1['text'] = '1'
        al_2['text'] = '2'
        al_3['text'] = '3'
        al_4['text'] = '4'


qTypeLabel = ttk.Label(qFrame, text="Тип запитання", font=font).place(x=250, y=110)
# choise type of question
Radiobutton(qFrame,
            text="Обрати відповідь",
            variable=qType,
            value=1,
            command=get_answers_form,
            font=("Arial", 9)
            ).place(x=380, y=105)
Radiobutton(qFrame,
            text="Встановити послідовність",
            variable=qType,
            value=2,
            command=get_answers_form,
            font=("Arial", 9)
            ).place(x=380, y=125)

root.mainloop()

from tkinter import *
from tkinter import ttk
import glob, os
from PIL import Image

root = Tk()
root.title("Щасливчик (автор Якимчук Олександр)")
root.winfo_screenwidth()
root.winfo_screenheight()
root.resizable(width=False, height=False)

# bg color
bg_color = "#02C4CB"  # FFD700"  # 0000C3"
fg_color = "#000080"
success_color = "#00FF00"
fail_color = ""
# main background
bg_image_main = Image.open("static\\image\\background_main.gif")
rWidth = root.winfo_screenwidth()
rHeight = root.winfo_screenheight()
bg_image_main = bg_image_main.resize((rWidth, rHeight), Image.ANTIALIAS)
bg_image_main.save("static\\image\\background_main.gif", "gif")
root.geometry('%sx%s' % (rWidth, rHeight))
photo_main = PhotoImage(file="static\\image\\background_main.gif")
bg_label = Label(root, image=photo_main, compound=CENTER, bd=0)
bg_label.place(x=0, y=0)

# second background (used)
bg_image_q = Image.open("static\\image\\second_background.gif")
rWidth = root.winfo_screenwidth()
rHeight = root.winfo_screenheight()
bg_image_q = bg_image_q.resize((rWidth, rHeight), Image.ANTIALIAS)
bg_image_q.save("static\\image\\second_background.gif", "gif")
root.geometry('%sx%s' % (rWidth, rHeight))
photo_q = PhotoImage(file="static\\image\\second_background.gif")

# rules background
bg_image_r = Image.open("static\\image\\rules_background.gif")
rWidth = root.winfo_screenwidth()
rHeight = root.winfo_screenheight()
bg_image_r = bg_image_r.resize((rWidth, rHeight), Image.ANTIALIAS)
bg_image_r.save("static\\image\\rules_background.gif", "gif")
root.geometry('%sx%s' % (rWidth, rHeight))
photo_r = PhotoImage(file="static\\image\\rules_background.gif")
# menu buttons
play_button = Button(root, text="Розпочати гру", font=("Arial", 15), bg="#4169E0")
rules_button = Button(root, text="Правила гри", font=("Arial", 15), bg="#4169E0")
return_button = Button(root, text="Головне меню", font=("Arial", 15), bg="#4169E0")


def show_menu_buttons():
    play_button.place(relx=0.30, rely=0.75, relwidth=0.15)
    rules_button.place(relx=0.55, rely=0.75, relwidth=0.15)


def hide_menu_buttons():
    play_button.place_forget()
    rules_button.place_forget()


rules = """1. На екран виводиться запитання і 4 варіанти відповідей, з яких тільки одна правильна.\n
2. Кожна правильна відповідь  - 1 бал.\n
3. Всього запитань 12.\n
4. Можна дійти до кінця, або можна зупинитися і вийти з гри після кожного запитання.\n
5. Є 2 неспалимі суми балів 4 та 8.\n
6. Якщо відповідь не вірна – гра закінчується, але якщо у вас є неспалимі бали, вам зараховується найбільший з них.\n
7. Один раз можна скористатися підказкою 50/50.\n
"""
# question label

f_relwidth = 0.5
f_s = rWidth // 70
q_frame = Frame(root,
                bg=bg_color,
                bd=0,
                highlightbackground="black",
                highlightcolor="black",
                highlightthickness=2,
                relief=SUNKEN
                )

q_label = Label(q_frame,
                font=("Arial", f_s, "bold"),
                bg=bg_color,
                fg=fg_color,
                padx=10,
                justify="center",
                wraplength=f_relwidth * rWidth
                )

q_label.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)


def show_q_label():
    q_frame.place(relx=0.25, rely=0.45, relwidth=f_relwidth, relheight=0.2)


def hide_q_label():
    q_frame.place_forget()


# answers
f_s = rWidth // 91
answer_button_1 = Button(root, font=("Arial", f_s), bg=bg_color, fg=fg_color)
answer_button_2 = Button(root, font=("Arial", f_s), bg=bg_color, fg=fg_color)
answer_button_3 = Button(root, font=("Arial", f_s), bg=bg_color, fg=fg_color)
answer_button_4 = Button(root, font=("Arial", f_s), bg=bg_color, fg=fg_color)

answer_buttons = [answer_button_1, answer_button_2, answer_button_3, answer_button_4]


def show_answer_buttons():
    answer_button_1.place(relx=0.25, rely=0.7, relwidth=0.2)
    answer_button_2.place(relx=0.55, rely=0.7, relwidth=0.2)
    answer_button_3.place(relx=0.25, rely=0.8, relwidth=0.2)
    answer_button_4.place(relx=0.55, rely=0.8, relwidth=0.2)
    answer_button_1.config(state="normal", bg=bg_color)
    answer_button_2.config(state="normal", bg=bg_color)
    answer_button_3.config(state="normal", bg=bg_color)
    answer_button_4.config(state="normal", bg=bg_color)


def hide_answer_buttons():
    answer_button_1.place_forget()
    answer_button_2.place_forget()
    answer_button_3.place_forget()
    answer_button_4.place_forget()


# range question labels

rq_labels = []

for i in range(4):
    rq_labels.append(Label(root, bg="#0000E5", font=("Arial", 17)))


def hide_rq_labels():
    for i in rq_labels:
        i.place_forget()


# success scale labels
success_labels = []
for i in range(0, 12):
    success_labels.append(Label(root,
                                text=str(i + 1),
                                bg="#6A5ACD",  # cool color #E6E6FA
                                highlightbackground="black",
                                fg="yellow",
                                font=("Arial", 12, "bold")))


def show_success_labels():
    for i in range(0, 12):
        success_labels[i].place(relx=0.94 - (i * 0.006), rely=(11 - i) * 0.05 + 0.3, relwidth=0.05 + (i * 0.006))


def set_standart_bg_on_success_labels():
    for i in success_labels:
        i.config(bg="#6A5ACD")


def hide_success_labels():
    for i in range(0, 12):
        success_labels[i].place_forget()


# stop and continue buttons

choice_label = Label(root, bg=bg_color, font=("Arial", 15), fg="snow")
stop_button = Button(root, text="Завершити", font=("Arial", 13), bg="red")
continue_button = Button(root, text="Продовжити", font=("Arial", 13), bg=success_color)

# help buttons

help_color ="#00FA9A"
button_50x50 = Button(root, text="50x50", bg=help_color, font=("Arial", 15))
button_hall_assistance = Button(root, text="Допомога залу", bg=help_color, font=("Arial", 12))
percent_labels = []
for i in range(4):
    percent_labels.append(Label(root, font=("Arial", 15), bg="#0000E5", fg="limegreen"))


def show_help_buttons():
    button_50x50.place(relx=0.1, rely=0.3, width=130, height=50)
    button_hall_assistance.place(relx=0.1, rely=0.5, width=130, height=50)


def make_enable_help_buttons():
    button_50x50.config(bg=help_color, state="normal")
    button_hall_assistance.config(bg=help_color, state="normal")


def hide_help_buttons():
    button_50x50.place_forget()
    button_hall_assistance.place_forget()


def show_percent_labels():
    percent_labels[0].place(relx=0.2, rely=0.7, width=40)
    percent_labels[1].place(relx=0.5, rely=0.7, width=40)
    percent_labels[2].place(relx=0.2, rely=0.8, width=40)
    percent_labels[3].place(relx=0.5, rely=0.8, width=40)


def hide_percent_labels():
    for i in percent_labels:
        i.place_forget()


# game_over_label
end_label_text = ["На жаль, Ви не пройшли відбірковий тур", "Гру завершено, ви набрали %s балів",
                  "Вітаємо, Ви перемогли!!!\nВаш результат 12 балів"]

# "Ви завершили гру з результатом %s балів" % mark
end_label = Label(font=("Arial", 20),
                  bg="#0000C3",
                  fg=fg_color,
                  padx=10,
                  justify="center",
                  wraplength=rWidth * 0.6
                  )

# full screen
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())


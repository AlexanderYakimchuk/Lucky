from lucky_game.main_view import *
from lucky_game.db_manager import DBManager
import random

# questions
question_number = -1
question = None

rq_answers = []  # sequence of rank-question's answers


def set_next_question():
    global question_number, question
    if question_number == 12:
        return
    question_number += 1
    if question_number == 0:
        question = DBManager.get_question(range=1, type=2)
    elif question_number <= 12:
        range = question_number // 4 if question_number % 4 == 0 else question_number // 4 + 1
        question = DBManager.get_question(range=range)


def show_next_question(event):
    set_next_question()
    if question_number > 0:
        show_success_labels()
        success_labels[question_number - 1].config(bg="white")
        if question_number > 1:
            if (question_number - 1) % 4 != 0:
                success_labels[question_number - 2].config(bg=success_color)
            else:
                success_labels[question_number - 2].config(bg="#FFA500")
        show_help_buttons()

    hide_choice_buttons(event)
    answer_button_1.config(text=question.answers[0].text)
    answer_button_2.config(text=question.answers[1].text)
    answer_button_3.config(text=question.answers[2].text)
    answer_button_4.config(text=question.answers[3].text)
    show_answer_buttons()
    show_q_label()
    q_label.config(text=question.text)


def game_over(event, reason=1):
    DBManager.clean_question()
    global question_number
    hide_answer_buttons()
    hide_help_buttons()
    hide_choice_buttons(event)
    hide_q_label()
    hide_success_labels()
    # show_q_label()
    mark = 0
    if reason == 1:
        if question_number < 12:
            mark = question_number // 4 * 4
        else:
            mark = 8
    elif reason == 2:
        mark = question_number
    if question_number == 0:
        if reason == 1:
            end_label.config(fg="snow", text=end_label_text[0])
        elif reason == 2:
            end_label.config(fg="snow", text=end_label_text[1] % mark)
    if 0 < question_number <= 12:
        end_label.config(fg="snow", text=end_label_text[1] % mark)

    if question_number == 12 and reason == 2:
        end_label.config(fg="snow", text=end_label_text[2])

    end_label.place(relx=0.22, rely=0.5, relwidth=0.6)
    return_button.place(relx=0.42, rely=0.8, relwidth=0.16)
    question_number = -1


def show_choice_buttons(event):

    hide_percent_labels()
    if question_number == 12:
        hide_choice_buttons(event)
        game_over(event=None, reason=2)
        return
    for b in answer_buttons:
        b.config(state="disabled")
    continue_button.place(relx=0.34, rely=0.9, relwidth=0.15)
    stop_button.place(relx=0.52, rely=0.9, relwidth=0.15)


def hide_choice_buttons(event):
    choice_label.place_forget()
    continue_button.place_forget()
    stop_button.place_forget()


# show rules button
def show_rules(event):
    hide_menu_buttons()
    return_button.place(relx=0.009, rely=0.94, relwidth=0.15)
    bg_label.config(image=photo_r)
    # bg_label.config(text=rules, font=("Arial", 18), foreground="yellow", wraplength=rWidth - rWidth * 0.3)
    # bg_label.config(compound=CENTER)
    # bg_label.config(justify='left')


def main_menu(event):
    show_menu_buttons()
    return_button.place_forget()
    end_label.place_forget()
    bg_label["image"] = photo_main
    bg_label["text"] = ""


rules_button.bind("<Button-1>", show_rules)
return_button.bind("<Button-1>", main_menu)


# play button
def play(event):
    bg_label.config(image=photo_q)
    hide_menu_buttons()
    show_q_label()
    make_enable_help_buttons()
    set_standart_bg_on_success_labels()
    show_next_question(event)
    global question


play_button.bind("<Button-1>", play)


# answer button bind
def after_pause(function, event, widget=None):
    # if widget:
    #     widget.config(bg=bg_color)
    hide_rq_labels()
    function(event)


def show_correct_seq(numb=0):
    color = success_color
    if question.answers[rq_answers[numb]].range != numb + 1:
        color = "red"
    rq_labels[numb].place(relx=0.3, rely=0.7 + 0.05 * numb)
    rq_labels[numb].config(fg=color, text=question.answers[rq_answers[numb]].text)
    if numb == 3:
        rq_answers.clear()
        return
    root.after(1000, lambda: show_correct_seq(numb + 1))


def answer_action(event, answer_number):
    widget = event.widget
    if widget["state"] == "disabled":
        return
    if question.type == 1:
        if question.answers[answer_number].is_correct:
            widget.config(bg=success_color)
            root.after(1000, lambda: after_pause(show_choice_buttons, event, widget))
        else:
            widget.config(bg="red")
            success_labels[question_number - 1].config(bg="red")
            root.after(1000, lambda: after_pause(game_over, event, widget))
    elif question.type == 2:
        rq_answers.append(answer_number)
        widget.config(state="disabled", bg="#F0E68C")
        if len(rq_answers) == 4:
            hide_answer_buttons()
            show_correct_seq()
            result = True
            for i in range(4):
                if question.answers[rq_answers[i]].range != i + 1:
                    result = False
            if result:
                root.after(5000, lambda: after_pause(show_choice_buttons, event))
            else:
                success_labels[question_number].config(bg="red")
                root.after(5000, lambda: after_pause(game_over, event))


answer_button_1.bind("<Button-1>",
                     lambda event, answer_number=0: answer_action(event, answer_number))
answer_button_2.bind("<Button-1>",
                     lambda event, answer_number=1: answer_action(event, answer_number))
answer_button_3.bind("<Button-1>",
                     lambda event, answer_number=2: answer_action(event, answer_number))
answer_button_4.bind("<Button-1>",
                     lambda event, answer_number=3: answer_action(event, answer_number))


# choice buttons bind
def stop_game(event):
    success_labels[question_number].config(bg=success_color)
    game_over(event, reason=2)


continue_button.bind("<Button-1>", show_next_question)
stop_button.bind("<Button-1>", stop_game)


# help buttons bind

def tip_50x50(event):
    if event.widget["state"] == "disabled":
        return
    flag = 0
    b = None
    while flag < 2:
        a = random.choice([0, 1, 2, 3])
        if not question.answers[a].is_correct and a != b:
            b = a
            flag += 1
            answer_buttons[a].place_forget()
    button_50x50.config(state="disabled", bg="#FFE4C4")


def tip_hall_assistance(event):
    if event.widget["state"] == "disabled":
        return
    results = [0, 0, 0, 0]
    percent = 100
    for a in range(4):
        if question.answers[a].is_correct:
            results[a] = random.randint(39, 90)
            percent -= results[a]
            break
    for a in range(4):
        if results[a] == 0:
            results[a] = random.randint(0, percent) if a < 3 else percent
            percent -= results[a]
        if a == 3:
            results[a] += percent
        percent_labels[a].config(text="%s%%" % results[a])
    show_percent_labels()

    button_hall_assistance.config(state="disabled", bg="#FFE4C4")

button_50x50.bind("<Button-1>", tip_50x50)
button_hall_assistance.bind("<Button-1>", tip_hall_assistance)

main_menu(None)
# play(None)
# game_over(event=None)

root.mainloop()

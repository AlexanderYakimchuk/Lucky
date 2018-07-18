import sqlite3
import random
from lucky_game.models import Question, Answer

db = sqlite3.connect("../Lucky.sqlite")
cursor = db.cursor()


class DBManager:
    questions = []

    @staticmethod
    def get_question(range, type=1):
        cursor.execute("""SELECT * FROM question WHERE q_rank = ? AND q_type = ?""", (range, type))
        questions = cursor.fetchall()
        question = random.choice(questions)
        while question[0] in DBManager.questions:
            question = random.choice(questions)
        DBManager.questions.append(question[0])
        question = Question(id=question[0],
                            text=question[1],
                            range=question[2],
                            type=question[3],
                            answers=DBManager.get_answers(question[0], question[3]))
        return question

    @staticmethod
    def get_answers(q_id, q_type=1):
        answers = []
        if q_type == 1:
            cursor.execute("""SELECT a.a_id, a_text, a_is_correct FROM answer AS a 
                              JOIN answer_to_question AS atq
                              ON a.a_id = atq.a_id
                              WHERE atq.q_id = ?
                              """, (q_id,))
            answers_ = cursor.fetchall()

            for a in answers_:
                answers.append(Answer(id=a[0], text=a[1], is_correct=a[2]))
        elif q_type == 2:
            cursor.execute("""SELECT a.a_id, a_text, a_rank  FROM answer AS a 
                                          JOIN answer_to_question AS atq
                                          ON a.a_id = atq.a_id
                                          JOIN answers_rank AS ar
                                          ON a.a_id = ar.a_id
                                          WHERE atq.q_id = ?
                                          """, (q_id,))
            answers_ = cursor.fetchall()

            for a in answers_:
                answers.append(Answer(id=a[0], text=a[1], range=a[2]))

        random.shuffle(answers)

        return answers

    @staticmethod
    def clean_question():
        DBManager.questions.clear()




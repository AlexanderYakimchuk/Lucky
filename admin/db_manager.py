import sqlite3

db = sqlite3.connect("../Lucky.sqlite")
cursor = db.cursor()


class DBManager:

    @staticmethod
    def add_question(q_text, q_rank, q_type=None):
        cursor.execute("""INSERT INTO question(q_text, q_rank)
                                  VALUES (?, ?)""", (q_text, q_rank))
        cursor.execute("""SELECT MAX(q_id) FROM question""")
        question_id = cursor.fetchone()[0]

        if q_type is not None:
            cursor.execute("""UPDATE question
                              SET q_type = ?
                              WHERE q_id = ?""", (q_type, question_id))

        db.commit()
        return question_id

    @staticmethod
    def add_answer(question_id, a_text, a_is_correct=None):
        cursor.execute("""INSERT INTO answer(a_text, a_is_correct)
                          VALUES (?, ?)""", (a_text, a_is_correct))

        cursor.execute("""SELECT MAX(a_id) FROM answer""")

        answer_id = cursor.fetchone()[0]

        if a_is_correct is not None:
            cursor.execute("""UPDATE answer
                              SET a_is_correct = ?
                              WHERE a_id = ?""", (a_is_correct, answer_id))

        cursor.execute("""INSERT INTO answer_to_question(a_id, q_id)
                          VALUES (?, ?)""", (answer_id, question_id))
        db.commit()
        return answer_id

    @staticmethod
    def add_positional_answer(question_id, a_text, a_rank):
        answer_id = DBManager.add_answer(question_id, a_text)

        cursor.execute("""INSERT INTO answers_rank(a_id, a_rank)
                          VALUES (?, ?)""", (answer_id, a_rank))

        db.commit()


class Answer:
    def __init__(self, id, text, is_correct=None, range=None):
        self.id = id
        self.text = text
        self.is_correct = is_correct
        self.range = range


class Question:
    def __init__(self, id, text, range, type, answers=None):
        self.id = id
        self.text = text
        self.range = range
        self.type = type
        self.answers = answers

    def set_answers(self):
        pass



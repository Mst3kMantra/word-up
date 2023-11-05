
class Word:
    def __init__(self, name, meanings):
        self.name = name
        self.meanings = meanings
        self.length = len(name)


class Game:
    def __init__(self, words):
        self.score = 0
        self.round = 1
        self.words = words
        self.streak = 0


class Round:
    def __init__(self):
        self.guesses = 10
        self.correct_count = 0
        self.guess_strings = []

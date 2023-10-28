
class Word:
    def __init__(self, name, meanings, synonyms, antonyms):
        self.name = name
        self.meanings = meanings
        self.synonyms = synonyms
        self.antonyms = antonyms
        self.length = len(name)


class Game:
    def __init__(self, words):
        self.score = 0
        self.round = 1
        self.words = []


class Round:
    def __init__(self):
        self.guesses = 10
        self.correct_count = 0
        self.hints = []

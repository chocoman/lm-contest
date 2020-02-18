from .language_model import LanguageModel

class ContestInterface:
    def __init__(self):
        self.model = LanguageModel()
        self.model.load('bigram/contest_model/')

    def predict_next_character(self, prefix):
        return self.model.predict(prefix)

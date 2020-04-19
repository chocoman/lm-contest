from .language_model import LanguageModel
from .language_model import LetterTrie

class ContestInterface:
    def __init__(self):
        self.model = LanguageModel()
        self.model.load('ondrej/contest_model/')

    def predict_next_character(self, prefix):
        return self.model.predict(prefix)

ci = ContestInterface()

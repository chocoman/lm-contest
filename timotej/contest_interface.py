from .language_model import LanguageModel

class ContestInterface:
    def __init__(self, statistics_mode = False):
        self.model = LanguageModel()
        self.model.load('timotej/')
        self.statistics_mode=statistics_mode
        if statistics_mode:
            self.last_prediction = None
            self.last_way = None
            self.words={"correct":0, "all":0}
            self.interpunction={"correct":0, "all":0}
            self.groups={"correct":0, "all":0}
        
    def statistics(self):
        words = f"{self.words['correct']}/{self.words['all']} {self.words['correct']/self.words['all']*100}%"
        interpunction = f"{self.interpunction['correct']}/{self.interpunction['all']} {self.interpunction['correct']/self.interpunction['all']*100}%"
        groups = f"{self.groups['correct']}/{self.groups['all']} {self.groups['correct']/self.groups['all']*100}%"
        print("statistics:")
        print(f" interpunction accuracy: {interpunction}")
        print(f" words accuracy: {words}")
        print(f" groups accuracy: {groups}")
        
    def predict_next_character(self, prefix):
        if self.statistics_mode:
            if len(prefix) == 0:
                pass
            else:
                self.last_way["all"] +=1
                if self.last_prediction == prefix[-1]:
                    self.last_way["correct"] += 1
            prediction =  self.model.predict(prefix, True)
            way = prediction[1]
            prediction = prediction[0]
            self.last_prediction = prediction
            if way == "word":
                self.last_way = self.words
            elif way == "group":
                self.last_way = self.groups
            elif way == "interpunction":
                self.last_way = self.interpunction
        else:
            prediction =  self.model.predict(prefix)
        return(prediction)


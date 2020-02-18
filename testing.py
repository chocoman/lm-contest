class Testing:
    def test_model(self, language_model, dataset):
        total_correct = 0
        total_count = 0
        for line in dataset.walk():
            total_correct += self.test_line(language_model, line)
            total_count += len(line)
        return total_correct / total_count

    def test_line(self, language_model, line):
        correct_count = 0
        for i in range(len(line)):
            pred = language_model.predict_next_character(line[:i])
            if pred == line[i]:
                correct_count += 1
        return correct_count
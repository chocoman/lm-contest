import json
import os

from os.path import join
from datetime import datetime
from language_model import LanguageModel

VERSION = '1.2'
NAME = 'Tomas'

class Training:
    def __init__(self):
        self.language_model = LanguageModel()

    def train(self, dataset_iterator):
        for line in dataset_iterator:
            self.language_model.train_batch(line)

    def save(self, directory):
        os.makedirs(directory, exist_ok=True)

        data = self.language_model.export()
        json.dump(
            data,
            open(join(directory, 'model.json'), 'w'),
            indent = 4,
            sort_keys = True,
            ensure_ascii = True,
        )

        info = {
            'version': VERSION,
            'name': NAME,
            'date': datetime.today().isoformat(timespec='seconds'),
        }
        json.dump(
            info,
            open(join(directory, 'info.json'), 'w'),
            indent = 4,
        )

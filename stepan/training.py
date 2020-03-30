import json
import os
import time

from os.path import join
from datetime import datetime
from language_model import LanguageModel

VERSION = '0.1'
NAME = 'Stepan'

class Training:
    def __init__(self):
        self.language_model = LanguageModel()

    def train(self, dataset_iterator):
        line_number = 0
        target_time = 60 * 0.2  
        start_time = time.time()
        for line in dataset_iterator:
            self.language_model.train_batch(line)
            line_number=line_number+1
            duration = time.time() - start_time
            if line_number%200==0:
                print("line: " + str(line_number) + " current time: " + str(duration) + " target time: " + str(target_time))
            if duration >= target_time:
                return
            
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

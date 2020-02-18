import argparse
from example.contest_interface import ContestInterface

interface = ContestInterface()

print('type a part of a sentence and press enter to see prediction of the next character')
prefix = ''
while True:
    prefix += input(prefix)
    predicted = interface.predict_next_character(prefix)
    print(prefix + predicted)
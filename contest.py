import argparse
import traceback
from testing import Testing
import example.contest_interface
import mateju.contest_interface
import milan.contest_interface
import ondrej.contest_interface
import stepan.contest_interface
import timotej.contest_interface
import tomas.contest_interface
from dataset import Dataset

parser = argparse.ArgumentParser()
parser.add_argument(
    'dataset',
    help='directory with the testing dataset',
    type=str,
)
args = parser.parse_args()

models = [
    (
        'example',
        example.contest_interface
    ),
    (
        'mateju',
        mateju.contest_interface
    ),
    (
        'milan',
        milan.contest_interface
    ),
    (
        'ondrej',
        ondrej.contest_interface
    ),
    (
        'stepan',
        stepan.contest_interface
    ),
    (
        'timotej',
        timotej.contest_interface
    ),
    (
        'tomas',
        tomas.contest_interface
    ),
]

testing = Testing()
dataset = Dataset(args.dataset)
output = []
for name, interface in models:
    print(f'testing {name}...')
    try:
        model = interface.ContestInterface()
        accuracy = testing.test_model(model, dataset)
    except Exception as e:
        print('crashed')
        print(e)
        traceback.print_exc()
        accuracy = 0
    print(f'accuracy {accuracy}')
    output.append((name, accuracy))

print('results:')
for name, accuracy in output:
    print(f'{name}\t{accuracy}')

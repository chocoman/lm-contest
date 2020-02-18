import argparse
from testing import Testing
import example.contest_interface
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
]

testing = Testing()
dataset = Dataset(args.dataset)
output = []
for name, interface in models:
    print(f'testing {name}...')
    model = interface.ContestInterface()
    accuracy = testing.test_model(model, dataset)
    print(f'accuracy {accuracy}')
    output.append((name, accuracy))

print('results:')
for name, accuracy in output:
    print(f'{name}\t{accuracy}')

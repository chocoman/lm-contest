import argparse
import os
import sys
from training import Training

sys.path.append('..')
from dataset import Dataset

parser = argparse.ArgumentParser()
parser.add_argument(
    'dataset',
    help='directory with the training dataset',
    type=str,
)
parser.add_argument(
    '--savedir',
    help='directory to save the trained model',
    type=str,
    default = 'output',
)
parser.add_argument(
    '--force',
    help='overwrite content of savedir',
    action='store_true',
)
args = parser.parse_args()

if (not args.force and os.path.exists(args.savedir)):
    if (not os.path.isdir(args.savedir) or len(os.listdir(args.savedir)) != 0):
        print(args.savedir, 'specified as savedir already exists and is nonempty.')
        print('Aborting training to prevent overwriting the data.')
        sys.exit(1)

training = Training()

dataset = Dataset(args.dataset)

training.train(dataset.walk())
training.save(args.savedir)
